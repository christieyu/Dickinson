## Christie Yu

import poetrytools
import unicodedata

poems = [
    {
        'title': 'A brief but patient illness',
        'texts': [u'A brief, but patient illness \u2014\nAn hour to prepare \u2014\nAnd one below, this morning\nIs where all the angels are \u2014\nIt was a short procession \u2014\nThe Bobolink was there \u2014\nAn aged Bee addressed us \u2014\nAnd then we knelt in prayer \u2014\nWe trust that she was willing \u2014\nWe ask that we may be \u2014\nSummer \u2014 Sister \u2014 Seraph!\nLet us go with thee!']
	},

	{	
		'title': 'A chastened Grace is twice a Grace',
		'texts': [u'A chastened Grace is twice a Grace \u2014\nNay, \'tis a Holiness.']
	}
]

for poem in poems:
    # print(poem["texts"][0])
    mypoem = poetrytools.tokenize(poem["texts"][0])

    # rhyme_scheme returns "X a b X X a X a b c X c"
    rhyme_scheme = ' '.join(poetrytools.rhyme_scheme(mypoem))
    print(rhyme_scheme)

    # scanscion returns "0 1 1 10 10 / 1 10 1 01 / 0 1 01 1 10 / 1 1 1 0 10 1 / 1 1 0 1 010 / 0 100 1 1 / 1 1 1 01 1 / 0 1 1 1 0 1 / 1 1 1 1 1 10 / 1 1 1 1 1 1 / 10 10 10 / 1 1 1 1 1"
    for item in poetrytools.scanscion(mypoem):
        scanscion = ' '.join(item)
        print(scanscion)

    # stanza_lengths returns "12"
    stanza_lengths = poetrytools.stanza_lengths(mypoem)
    print(stanza_lengths)

    # meter_guess returns "iambic trimeter"
    meter_guess = poetrytools.guess_metre(mypoem)[3]
    print(meter_guess)
