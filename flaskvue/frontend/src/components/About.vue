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
      </div>
    </div>
     <div class="card border-danger mb-3" id="card-two" style="max-width: 23rem;">
      <div class="card-header"></div>
      <div class="card-body">
        <h4 class="card-title">Data Scraping</h4>
        <p class="card-text">TO-DO: Christie</p>
        <h4 class="card-title">Meta-Analysis</h4>
        <p class="card-text">TO-DO: Greta and Yoyo</p>
      </div>
    </div>
     <div class="card border-danger mb-3" id="card-three" style="max-width: 23rem;">
      <div class="card-header"></div>
      <div class="card-body">
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
  margin: 25px;
}
#card-two {
  display: inline-block;
  margin: 25px;
}
#card-three {
  display: inline-block;
  margin: 25px;
}
</style>

<!-- CSS libraries -->
<style src="./bootstrap.css"></style>

