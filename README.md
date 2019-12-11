Hello!
====================

### User instructions

1. Clone this Github repo onto your own computer.
2. Once inside the Dickinson folder, open two Terminal windows.
3. In the first, run `pip install flask_pymongo` to download the package necessary to connect to our database, and then run `flask run`. This should be all you need, but on the off chance you are missing something like `pip` or `npm` on your computer, install it as needed. 
4. In the second, `cd` into `flaskvue`, then `frontend`, and run `npm install` to install all packages needed to run our frontend. Then run `npm run dev`. Do not ctrl-C or quit either Terminal window. 
5. Go to the localhost address indicated in the **first** terminal window (likely /5000, NOT /8080!) to see our website. Feel free to explore the "Poems", "Macros", and "About Us" tabs to learn more! 

If you'd like to experiment with our NLP analysis, you can view those files as `commonwords.py` (which includes our common words analysis, alliteration, and similes) and `prosodic-analysis.py` (where we worked with rhyme scheme, meter, scansion, and stanzas) in the `Poetry-Tools-Master` repo (forked from [Poetry-Tools](https://github.com/hyperreality/Poetry-Tools)). You can read more about how we performed these analyses on our About Me page, but in short the packages we used are [this Poetry-Analysis repo](https://github.com/HalleyYoung/Poetry_Analysis/), [NLTK](https://www.nltk.org/), [Sci-Kit Learn](https://scikit-learn.org/stable/), [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) and the poetrytools package mentioned earlier. We ask that you do not run this code without modifying it for your own purposes first, as it is connected to our MongoDB database and may result in alteration or duplication of data. If you do want to connect to your own database or test out different data, you can run these files with `python commonwords.py` or `python prosodic-analysis.py`. 

If you'd like to see our code for web-scraping using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), you can view those files as `scraper-wiki.py` for data from Wikipedia and `scraper-bartleby.py` for data from Bartleby.

---

### About the project

We named our project after a line in Emily Dickinson's poem, *Split the Lark — and you'll find the Music —*

>Split the Lark — and you'll find the Music —\
>Bulb after Bulb, in Silver rolled —\
>Scantilly dealt to the Summer Morning\
>Saved for your Ear when Lutes be old.\
>\
>Loose the Flood — you shall find it patent —\
>Gush after Gush, reserved for you —\
>**Scarlet Experiment!** Sceptic Thomas!\
>Now, do you doubt that your Bird was true? *[Source](https://en.wikisource.org/wiki/Split_the_Lark_%E2%80%94_and_you%27ll_find_the_Music_%E2%80%94)*

As you can see, what Dickinson (somewhat derogatorily) refers to as a "Scarlet Experiment!" is an unnecessarily intrusive analysis of her poetry — exactly our project's exercise. The aim of our project was to analyse several versions of 1799 Emily Dickinson poems, from her bound fascicles, unbound sets, and miscellaneous pieces.

> Dickinson preserved about 2/3 of her poems in "manuscript books" or "packets" of two types. Fascicles are composed of sheets folded in half (yielding one signature of 2 leaves and 4 pages), laid on top of each other (not nested), and bound with string. Other poems are preserved in what R. W. Franklin calls Sets which are groups of folded signatures appropriate for, and possibly intended for, similar binding, but never actually bound. The code in the table below indicates "F" for fascicle or "S" for set, then the fascicle number 01-40 or set number 01-15, then the order of the 4-page signature (or occasionally unfolded 1-leaf 2-page sheet), finally the order of the poem within the fascicle or set. An asterisk indicates that this poem, or part of this poem, occurs elsewhere in the fascicles or sets but its subsequent occurrences are not noted. Thus "F01.03.016*" indicates the 16th poem within fascicle #1, which occurs on the 3rd signature or sheet bound in that fascicle; and that this poem (or part of it) also recurs elsewhere in the fascicles or sets. *[Source](https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems)*

Also unique about Emily Dickinson's poetry is its poorly documented publication history and achronological storage. As seen from the visual below, much of her work was published posthumously, curated by family members (especially her sister Lavinia) without Dickinson's advice.

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Dickinson_progress_of_publication.png/740px-Dickinson_progress_of_publication.png "Dickinson chart 1")

> Nearly a dozen new editions of Dickinson's poetry, whether containing previously unpublished or newly edited poems, were published between 1914 and 1945. Martha Dickinson Bianchi, the daughter of Susan and Austin Dickinson, published collections of her aunt's poetry based on the manuscripts held by her family, whereas Mabel Loomis Todd's daughter, Millicent Todd Bingham, published collections based on the manuscripts held by her mother. These competing editions of Dickinson's poetry, often differing in order and structure, ensured that the poet's work was in the public's eye. *[Source](https://en.wikipedia.org/wiki/Emily_Dickinson#Posthumous)*

Versions of her poetry in this project were scraped from:
* [Wikisource](https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems)
* [Bartleby](https://www.bartleby.com/113/indexlines.html)
* [*Emily Dickinson’s Poems: As She Preserved Them*, edited by Cristanne Miller](https://www.amazon.com/Emily-Dickinsons-Poems-Preserved-Them/dp/0674737962/ref=pd_sbs_14_img_0/144-2972906-9739845?_encoding=UTF8&pd_rd_i=0674737962&pd_rd_r=82dab485-497b-4e70-930b-7e44522eef82&pd_rd_w=XXvON&pd_rd_wg=GCJnu&pf_rd_p=5cfcfe89-300f-47d2-b1ad-a4e27203a02a&pf_rd_r=K6M04AVBFXTV4VN6KCD2&psc=1&refRID=K6M04AVBFXTV4VN6KCD2)

With this digitalization, we hope that our project provides the ability to compare versions of Dickinson's texts en masse, using natural language processing protocols. We also dedicated focus to analysing her poetry as an aggregate, noticing normal and deviating sentiments, lengths and other characterizing metadata of her poems. In creating this baseline literary digestion we hope we can provide a foundational computational outlook on her poetry analysis.

---

### About us

We are Christie, Greta, Xiu and Yoyo, four students taking CPSC 376 at Yale University, taught and advised by Professor Benedict Brown. For this project, we were challenged to consider uses of web applications for the digital humanities. After considering the many difficulties of analysing a catalog as diverse and broad as Emily Dickinson's, we decided that it would be helpful to create a consolidated and visual database of her work, organised and filterable with useful parameters.
