<template>
  <div>
    <div class="jumbotron">
      <h1>Splitting the Lark</h1>
      <p class="lead">A closer look into Emily Dickinson's published works.</p>
      <hr class="my-4">
    </div>
    <div class="card border-danger mb-3" id="card-one" style="max-width: 23rem;">
      <div class="card-header"></div>
      <div class="card-body">
        <h4 class="card-title">Introduction</h4>
        <p class="card-text">What Dickinson (somewhat derogatorily) refers to as a "Scarlet Experiment!" is an unnecessarily intrusive analysis of her poetry — exactly our project's exercise. The aim of our project was to analyse several versions of 1799 Emily Dickinson poems, from her bound fascicles, unbound sets, and miscellaneous pieces. <br> <br> Also unique about Emily Dickinson's poetry is its poorly documented publication history and achronological storage. Much of her work was published posthumously, curated by family members (especially her sister Lavinia) without Dickinson's advice. <br> <br> As such, we hope that our project provides the ability to compare versions of Dickinson's texts on a mass scale, through digital natural language processing analysis. We also dedicated focus to analysing her poetry as an aggregate, noticing normal and deviating sentiments, lengths and other characteristics of her poems. With this baseline literary digestion in play, hopefully we can provide a computational outlook on her poetry analysis.</p>
        <br><br><br><br><br><br><br>
      </div>
    </div>
     <div class="card border-danger mb-3" id="card-two" style="max-width: 23rem;">
      <div class="card-header"></div>
      <div class="card-body">
        <h4 class="card-title">Data Scraping</h4>
        <p class="card-text">We sourced our data from three set points: <a href="https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems">Wikisource,</a> <a href="https://www.bartleby.com/113/indexlines.html">Bartleby,</a> and Cristanne Miller’s <a href="https://www.amazon.com/Emily-Dickinsons-Poems-Preserved-Them/dp/0674737962/ref=pd_sbs_14_img_0/144-2972906-9739845?_encoding=UTF8&pd_rd_i=0674737962&pd_rd_r=82dab485-497b-4e70-930b-7e44522eef82&pd_rd_w=XXvON&pd_rd_wg=GCJnu&pf_rd_p=5cfcfe89-300f-47d2-b1ad-a4e27203a02a&pf_rd_r=K6M04AVBFXTV4VN6KCD2&psc=1&refRID=K6M04AVBFXTV4VN6KCD2"><i>Emily Dickinson’s Poems: As She Preserved Them </i>(ISBN: 978-0674737969).</a>
<br><br>
We found that <a href="https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems">Wikipedia </a> had the most complete and well-documented list of metadata for each poem, including alphabetically poem’s title (usually its first line), position in fascicles or sets, first publication date (if any), and approximation in sequence according to two Dickinson scholars, Thomas H. Johnson and R. W. Franklin. We used <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup </a> to scrape the table for those columns of information, and also scraped for links to each individual poem’s text, which we could find in Wikisource as Emily Dickinson’s work is currently in the public domain.
<br><br>
Since Wikisource had several poems missing from its list, we manually typed text for certain poems, reading from Cristanne Miller’s complete collection. We noticed that in Cristanne Miller’s collection she references a few versions of each poem, inspiring us to look online for more collections of Emily Dickinson’s poetry. We found another set at Bartleby, which we again used the same scraping method to access each poem’s text and store it in our MongoDB database.</p><br><br><br><br>
      </div>
    </div>
     <div class="card border-danger mb-3" id="card-three" style="max-width: 23rem;">
      <div class="card-header"></div>
      <div class="card-body">
        <h4 class="card-title">Meta-Analysis</h4>
        <p class="card-text">We have performed linguistic analysis across several axes. Using the <a href="https://github.com/hyperreality/Poetry-Tools">poetrytools</a> NLP package, we analyzed each poem’s rhyme scheme, estimated meter, scansion, and stanza lengths. These are computed guesses, not definitive. Additionally we computed a “readability” score that can serve as a proxy for how complex— mostly in terms of sentence structure— each poem is. Finally, we used <a href="https://www.nltk.org/">NLTK</a> and <a href="https://scikit-learn.org/stable/">SciKit-Learn</a> to analyze each poem and identify similes and alliterations (borrowing from Halley Young’s <a href="https://github.com/HalleyYoung/Poetry_Analysis">Poetry Analysis repo</a>), and we used the <a href="https://stanfordnlp.github.io/CoreNLP/">Stanford CoreNLP</a> package for computing a “sentiment” guess of how positive or negative each poem is. <br><br> On a higher level, we also pulled out the 100 most common “unique” words, and provided a sentiment analysis of these poems as well. We graphed this meta-analysis data and it’s visible under the “Macros” tab. </p>
        <h4 class="card-title">About Us</h4>
        <p class="card-text">We are Christie, Greta, Xiu and Yoyo, four students taking CPSC 376 at Yale University, taught and advised by Professor Benedict Brown. For this project, we were challenged to consider uses of web applications for the digital humanities. After considering the many difficulties of analysing a catalog as diverse and broad as Emily Dickinson's, we decided that it would be helpful to create a consolidated and visual database of her work, organised and filterable with useful parameters.</p>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'About',
  data () {
    return {
    }
  },
}
</script>


<style>
#card-one {
  display: inline-block;
  margin: 0px 25px 25px 25px;
}
#card-two {
  display: inline-block;
  margin: 0px 25px 25px 25px;
}
#card-three {
  display: inline-block;
  margin: 0px 25px 25px 25px;
}
</style>

<!-- CSS libraries -->
<style src="./bootstrap.css"></style>

