<template>
  <div>
    <div id="frequent_words" style="display:inline-block;">
      <h1>FREQUENT WORDS</h1>
      <div style="overflow: auto; height:700px;">
        <ul class="list-group">
          <li style="font-size: 20px;" class="list-group-item d-flex justify-content-between align-items-center" v-for="item in frequent_words">
            {{item.word}}
            <span class="badge badge-warning badge-pill">{{item.frequency}}</span>
          </li>
        </ul>
      </div>
    </div>
      <!-- GRAPHS: SENTIMENTS -->
      <div class="card mb-3" style="display:inline-block; width: 400px;">
        <h3 class="card-header"">Analysis #1</h3>
        <div class="card-body">
          <h5 class="card-title">Readability</h5>
          <h6 class="card-subtitle text-muted">By Year and Fascicle</h6>
        </div>
        <img style="height: 250px; width: 100%; display: block;" v-bind:src="'/static/img/readability_graph.jpeg'" alt="Card image">
        <div class="card-body" style="font-size: 15px">
          This graph displays the readability of Emily Dickinson's poems, organized by year and fascicle.
          The Coleman-Liau index was used to determine the readability of a poem (The Coleman–Liau index is a readability test designed to gauge the understandability of a text as an approximation the U.S. grade level thought necessary to comprehend the text. The formula is:  CLI=0.0588{L}-0.296{S}-15.8, where L is the average number of letters per 100 words and S is the average number of sentences per 100 words.)<br><br> As displayed on the graph and according the Coleman index, Emily Dickinson's poems are readable by young audiences.<br>
        </div>
        <div class="card-body">
          <a href="#" class="card-link"></a>
          <a href="#" class="card-link"></a>
        </div>
      </div>

      <div class="card mb-3" style="display:inline-block; width: 400px; margin-left:25px;">
        <h3 class="card-header"">Analysis #2</h3>
        <div class="card-body">
          <h5 class="card-title">Sentiment</h5>
          <h6 class="card-subtitle text-muted">By Year and Fascicle</h6>
        </div>
        <img style="height: 250px; width: 100%; display: block;" v-bind:src="'/static/img/sentiment_graph.jpeg'" alt="Card image">
        <div class="card-body" style="font-size: 15px">
          <p class="card-text">This graph displays the sentiment of Emily Dickinson's poems across the years and fascicles.  Note that the year is recorded by the first publication of the poem, and some of these poems were published after her death. The fascicles are denoted with an F in the y-axis markers. Set information, which starts with an S is also included as well. Overall, the sentiments of her poems appear to be higher on the negative scale.<br><br><br><br></p>
        <div class="card-body">
          <a href="#" class="card-link"></a>
          <a href="#" class="card-link"></a>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Macros',
  data: () => ({
    frequent_words: "",
  }),
  async beforeMount() {
    let frequentWordsURL = new URL("http://127.0.0.1:5000/frequent_words");
    let response = await fetch(frequentWordsURL);
    let data = await response.json();
    this.frequent_words = data;
  },
}
</script>


<style>
#frequent_words {
  margin: 20px;
  width: 350px;
}
</style>

<!-- CSS libraries -->
<style src="./bootstrap.css"></style>


