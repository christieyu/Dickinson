from pymongo import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
import string
from collections import defaultdict, OrderedDict
import operator
import word as wd

'''
This program accesses all poems from database and performs linguistic analysis on them, 
including computing the most common words, finding similes, and identifying alliterations.
It then uploads the linguistic analysis data to the database. We do not recommend running this 
code as it may result in re-uploading of duplicate data to the database. It was written to be 
run once. 
'''

# connect to database
client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")
db = client.DickinsonDB
col = db.DickinsonCOLL
poems = {}
# build dictionary of poems
for entry in col.find():
	if (entry['poems']):
		i = entry['_id']
		poems[i] = entry['poems'][0]

# -------------------------------------------------------
# COMPUTING MOST FREQUENT WORDS (some code borrowed from https://medium.com/@cristhianboujon/how-to-list-the-most-common-words-from-text-corpus-using-scikit-learn-dad4d0cab41d)
# use scikit-learn's CountVectorizer
v = CountVectorizer(stop_words="english").fit(poems)
words = v.transform(poems)
sum_words = words.sum(axis=0)
words_freq = [(word.encode("UTF8"), sum_words[0, i]) for word, i in vec.vocabulary_.items()]
words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
words_coll = db.wordsFrequency
# load in 100 most common words to collection in database(skipping two that should be considered stopwords)
for word in words_freq[:102]:
	if word[0] != "ll" and word[0] != "like":
		word_dict = { "word": word[0], "freq": word[1]}
		x = words_coll.insert_one(word_dict)

# -------------------------------------------------------
# FINDING ALLITERATIONS IN POEMS (much of this script is borrowed from https://stackoverflow.com/questions/42125088/finding-alliterative-word-sequences-with-python)
alliteration_coll = db.newalliterationCOLL
# loop through all poems
for key in poems:
	raw = poems[key].replace("\n", ". ")
	allit_words = []

	# get set of alphabet letters
	letters = [letter for letter in string.ascii_lowercase] 

	# add alliterative phonemes
	sounds = ["ch", "ph", "sh", "th"] + letters 

	# Use NLTK's built in stopwords and add "'s" to them
	stopwords1 = stopwords.words('english') + ["'s"] 
	stopwords2 = set(stopwords1) 

	# use nltk's tokenization
	sents = sent_tokenize(raw)

	for sent in sents:
	    tokenized_sent = word_tokenize(sent)

	    # list of alliterating word sequences
	    alliterating_words = []
	    previous_initial_sound = ""
	    for word in tokenized_sent:
	    	# test alliteration for sounds, not just letters
	        for sound in sounds:
	            if word.lower().startswith(sound):
	                initial_sound = sound
	                if initial_sound == previous_initial_sound:
	                	# if continuing chain of alliteration
	                    if len(alliterating_words) > 0:
	                    	# doesn't add previous word to alliteration because it's repetitive (only if already in a chain)
	                        if previous_word == alliterating_words[-1]: # (comment from the stackoverflow source): prevents duplication in chains of more than 2 alliterations, but assumes repetition is not alliteration)
	                            alliterating_words.append(word)
	                        # add the matching sound words to list
	                        else:
	                            alliterating_words.append(previous_word)
	                            alliterating_words.append(word)
	                    # we're at the start of alliteration, so don't consider repetitive case
	                    else:
	                        alliterating_words.append(previous_word)
	                        alliterating_words.append(word)                
	                break # Allows us to treat sh/s distinctly

	        # don't consider stopwords as breaking alliteration
	        if word not in stopwords2: 
	            previous_initial_sound = initial_sound
	            previous_word = word

	    if len(alliterating_words) >= 2:
	    	# append all the alliteration words for that sentence in a list
			allit_words.append(alliterating_words)

	# store full set of alliteration phrases in database
	allit_dict = {"poem_id": key, "alliterations": allit_words}
  	x = alliteration_coll.insert_one(allit_dict)

# -------------------------------------------------------
# FINDING SIMILES
# We experimented with using the below grammar to find valid parses after tokenizing, with the idea that similes occur with the following sentence 
# structures more often, but actually got better results with a much simpler method so we abandoned this strategy. 
# This grammar was from https://github.com/HalleyYoung/Poetry_Analysis
#     grammar = nltk.CFG.fromstring("""
#     S -> NP "like" NP | "ADJ" "like" "NP" | NP VERB "like" NP | "X" "like" "NP" | NP "as" "ADJ" "as" NP | VERB "as" "ADJ" "as" NP |OTH
#     NP -> NOUN | "ADJ" NOUN | "DET" NP 
#     NOUN -> "NP" | "PRON" | "NOUN"
#     VERB -> "VD" | "VERB" | "VG"
#     OTH -> "OTH" "PUNC" "FW" "WH" "TO" "NUM" "ADV" "VD" "VG" "L" "VN" "NOUN" "P" "S" "EX" "VERB" "CONJ" "UH" "PRON" "MOD" "ADP" "X" "PRT"
#     """)  

# We realized most of the false positives we got were in lines where there was a common non-simile phrase that used "as". So we just removed any 
# lines containing one of the below from consideration. 
non_simile_phrases = ["as if", "if as", "as well", "as it", "much as", "as our own", "far as"]
isValid = True
simile_coll = db.simileCOLL
for key in poems:
 	similes = []
 	# split poem into lines
 	lines = poems[key].split("\n")
	for line in lines:
		isValid = True
		words = line.split(" ")
		# don't consider lines that have one of the non-simile constructions
		for phrase in non_simile_phrases:
			if phrase in line.lower():
				isValid = False
				break
		for word in words:
			if (word == "like" or word == "as") and isValid:
				# case sensitive on purpose, b/c most instances of Like or As as starting lines were not found to be similes
				# add whole line as simile
				similes.append(line)
	if len(similes) > 0:
		similes_dict = {"poem_id": key, "similes": similes}
		x = simile_coll.insert_one(similes_dict)    
