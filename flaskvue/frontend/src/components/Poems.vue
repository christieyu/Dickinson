<template>
	<div>
    <!-- CARD ONE: ALL POEMS -->
    <div class="card bg-secondary mb-3" id="titles" style="max-width: 30rem;">
      <div class="card-header"><h1 id="card_titles">All poems</h1></div>
      <div class="card-body" id="card_body">
        <p class="card-text">
          *Dates indicate year of publication.
          <div id="single_title" v-for="poem in poems" @click="getPoemDetails(poem['title'])"><b>{{poem['title']}}</b><span class="badge badge-info" style="margin-left:20px">{{ poem["pubdate"] }}</span></div>
        </p>
      </div>
    </div>
    <!-- CARD TWO: POEM VERSIONS -->
    <div id="versions">
      <ul class="nav nav-tabs">
        <li class="nav-item" id="myTabs" v-if="details_length == 0">
          <a class="nav-link active" id="nav_bar_tab" data-toggle="tab" href="#home"><b>Version {{1}}</b></a>
        </li>
        <li class="nav-item" id="myTabs">
          <a class="nav-link active" data-toggle="tab" v-if="details_length != 0">Version 1</a>
        </li>
      </ul>
      <div id="myTabContent" class="tab-content">
        <div class="tab-pane active show" v-if="details_length == 0 " id="home">
            <p>Select a poem on the left panel.</p>
        </div>
        <div v-else>
          <!-- <div v-for="k in details.length">
            {{k}} -->
            <div class="tab-pane active show" v-for="j in details[0].length" v-bind:id="k">
              <p v-if="details_similies.includes(details[0][j-1]) && show_similies" style="color: #c33c75"><b>{{details[0][j-1]}}</b></p>
              <p v-else><b>{{details[0][j-1]}}</b></p>
            </div>
          <!-- </div> -->
        </div>
      </div>
    </div>
    <!-- CARD THREE: ANALYSIS -->
    <div class="card border-success mb-3" id="titles" style="max-width: 30rem;">
    <div class="card-header"><h1 id="card_titles">Analysis</h1></div>
      <div class="card-body">
        <p class="card-text">
          <h6>{{ details_title }}</h6>
          <!--   <div class="custom-control custom-switch">
              <input style="font-size: 15px" type="checkbox" class="custom-control-input" id="customSwitch1" @click="toggle_alliterations()">
              <label class="custom-control-label" for="customSwitch1">Show Alliterations</label>
            </div>
            <ul class="list-group" v-if="show_alliterations == true">
              <br>
              <li class="list-group-item d-flex justify-content-between align-items-center" v-for="i in details_alliterations.length">
                <div v-for="j in details_alliterations[i-1].length">
                  {{ details_alliterations[i-1][j-1] }}
                </div>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
              </li>
            </ul>
            <br> -->
            <div class="custom-control custom-switch">
              <input style="font-size: 15px" type="checkbox" class="custom-control-input" id="customSwitch2" @click="toggle_similies()">
              <label class="custom-control-label" for="customSwitch2">Show Similies</label>
            </div>
        </p>
        <ul class="list-group">
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Meter
            <span class="badge badge-primary badge-pill badge-success">{{ details_analysis["meter_guess"] }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Rhyme Scheme
            <span class="badge badge-primary badge-pill badge-danger">{{ details_analysis["rhyme_scheme"] }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Stanza Lengths
            <span class="badge badge-primary badge-pill badge-warning">{{ details_analysis["stanza_lengths"] }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Readibility
            <span class="badge badge-primary badge-pill badge-dark">{{ details_readability["coleman"] }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Words
            <span class="badge badge-primary badge-pill badge-info">{{ details_readability["words"] }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Sentences
            <span class="badge badge-primary badge-pill badge-success">{{ details_readability["sentences"] }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Sentiment*
            <span class="badge badge-primary badge-pill badge-danger">{{ sentiment_analysis }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center" style="font-size:10px">
            *on a scale from 0-4, with 4 the most positive
          </li>
        </ul>
        <br>
        <div class="custom-control custom-switch">
            <input style="font-size: 15px" type="checkbox" class="custom-control-input" id="customSwitch3" @click="toggle_scanscion()">
            <label class="custom-control-label" for="customSwitch3">Show Scanscion</label>
        </div>
        <ul class="list-group" v-if="show_scanscion == true">
          <br>
          <li class="list-group-item"">
            <div v-for="line in details_scanscion"> {{line}}</div>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
          </li>
        </ul>
        <br>
          <div class="custom-control custom-switch">
              <input style="font-size: 15px" type="checkbox" class="custom-control-input" id="customSwitch1" @click="toggle_alliterations()">
              <label class="custom-control-label" for="customSwitch1">Show Alliterations</label>
            </div>
            <ul class="list-group" v-if="show_alliterations == true">
              <br>
              <li class="list-group-item d-flex justify-content-between align-items-center" v-for="i in details_alliterations.length">
                <div v-for="j in details_alliterations[i-1].length">
                  {{ details_alliterations[i-1][j-1] }}
                </div>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
              </li>
            </ul>
      </div>
    </div>
  </div>



	</div>
</template>

<script>
export default {
  name: 'Poems',
  data: () => ({
	  poems: '',
    poem_analysis: '',
    poem_readibility: '',
    poem_alliterations: '',
    poem_similies: '',
    details_objectID: 0,
    details_length: 0,
    details: '[]',
    details_title: '',
    details_analysis: '',
    details_readability: '',
    details_scanscion: [],
    details_alliterations: '',
    details_similies: [],
    show_alliterations: false,
    show_similies: false,
    show_scanscion: false,
    sentiment_analysis: '', 
    poem_sentiment: '',
	}),
  methods: {
    getPoemDetails: function(title) {
      for (let i = 0; i < this.poems.length; i++) {
        if (this.poems[i]['title'] === title) {
          this.details_title = title;
          this.details = this.poems[i].poems;
          console.log("poem details:", this.details)
          this.details_objectID = this.poems[i].objectID;
          if (this.poems[i].poems == null) {
            this.details_length = 0;
          } else {
            this.details_length = this.poems[i].poems.length;
          }
          // console.log(this.details_objectID)
        }
      }
      for (let i = 0; i < this.poem_analysis.length; i++) {
        if (this.details_objectID == this.poem_analysis[i].poem_id) {
          this.details_analysis = this.poem_analysis[i];
          this.details_scanscion = this.poem_analysis[i]["scanscion"];
          // console.log(this.details_analysis)
        }
      }
      for (let i = 0; i < this.poem_sentiment.length; i++) {
        if (this.details_title == this.poem_sentiment[i].title) {
          this.sentiment_analysis = this.poem_sentiment[i].sentiment;
        }
      }
      for (let i = 0; i < this.poem_alliterations.length; i++) {
        let alliteration_words = []
        if (this.details_objectID == this.poem_alliterations[i].poem_id) {
          for (let j = 0; j < this.poem_alliterations[i]["alliterations"].length; j++) {
            for (let k = 0; k < this.poem_alliterations[i]["alliterations"][j].length; k++) {
              alliteration_words.push(this.poem_alliterations[i]["alliterations"][j][k])
            }
          }
        console.log("before filtering: ", alliteration_words)
        let alliteration_words_filtered = []
        for (let a = 0; a < alliteration_words.length; a++) {
          console.log(alliteration_words[a])
          if (alliteration_words[a] == "—" || alliteration_words[a] == "," ) {
            a = a + 1;
          } else {
            alliteration_words_filtered.push(alliteration_words[a])
          }
        }
        let alliteration_words_pairs = []
        let new_pair = []
        for (let a = 0; a < alliteration_words_filtered.length; a++) {
          if (a % 2 != 0) {
            new_pair.push(alliteration_words_filtered[a])
            alliteration_words_pairs.push(new_pair)
            new_pair = []
          } else {
            new_pair.push(alliteration_words_filtered[a])
          }
        }
          this.details_alliterations = alliteration_words_pairs;
          console.log("ALLITERATIONS", this.details_alliterations)
        }
      }
      for (let i = 0; i < this.poem_similies.length; i++) {
        if (this.details_objectID == this.poem_similies[i].poem_id) {
          this.details_similies = this.poem_similies[i]["similies"];
        }
      }
      for (let i = 0; i < this.poem_readibility.length; i++) {
        // console.log(this.poem_readibility[i].poem_id)
        if (this.details_objectID == this.poem_readibility[i].poem_id) {
          this.details_readability = this.poem_readibility[i];
        }
      }
    },
    toggle_similies: function() {
      this.show_similies = !this.show_similies;
    },
    toggle_scanscion: function() {
      this.show_scanscion = !this.show_scanscion;
    },
    toggle_alliterations: function() {
      console.log(this.details_alliterations)
      this.show_alliterations = !this.show_alliterations;
    }
  },
  async beforeMount() {
  	let poemUrl = new URL("http://127.0.0.1:5000/poems");
  	let response = await fetch(poemUrl);
  	let data = await response.json();
  	this.poems = data;

    let poemAnalysis = new URL("http://127.0.0.1:5000/analysis");
    response = await fetch(poemAnalysis);
    data = await response.json();
    this.poem_analysis = data;
    // console.log(this.poem_analysis)

    let poemSentiment = new URL("http://127.0.0.1:5000/sentiment");
    response = await fetch(poemSentiment);
    data = await response.json();
    this.poem_sentiment = data;

    let poemAlliterations = new URL("http://127.0.0.1:5000/alliterations");
    response = await fetch(poemAlliterations);
    data = await response.json();
    this.poem_alliterations = data;
    // console.log(this.poem_alliterations)

    let poemSimilies = new URL("http://127.0.0.1:5000/similes");
    response = await fetch(poemSimilies);
    data = await response.json();
    this.poem_similies = data;
    console.log("ALL SIMILIES", this.poem_similies)

    let poemReadability = new URL("http://127.0.0.1:5000/readability");
    response = await fetch(poemReadability);
    data = await response.json();
    this.poem_readibility = data;
    console.log("ALL READIBILITY", this.poem_readibility)
  },
}
</script>


<style>
#card_titles {
  /*margin: 10px;*/
}
#single_title {
  /*margin-top: 10px;*/
  /*margin-left: 10px;*/
  /*margin-right: 10px;*/
  margin-bottom: 10px;
  border-bottom: 1px solid;
  font-size: 16px;
}
#titles {
  display: inline-block;
  margin-top: 30px;
  margin-left: 20px;
/*  border: 1px solid;*/
/*  border-color: #edeef4;*/
  width: 400px;
  height: 645px;
/*  background-color: #f4f5f8;*/
  overflow: auto;
}
#versions {
  display: inline-block;
  /*margin-top: 10px;*/
  /*border: 1px solid;*/
  /*border-color: #edeef4;*/
  width: 400px;
  height: 658px;
  background-color: #ffffff;
  overflow: auto;
}
#analysis {
  display: inline-block;
  /*margin-top: 10px;*/
  border: 1px solid;
  border-color: #edeef4;
  width: 400px;
  height: 645px;
  background-color: #f4f5f8;
  overflow: auto;
}
#single_poem {
  display: inline-block;
  margin-top: 10px;
  margin-bottom: 10px;
  border: 1px solid;
  border-color: #edeef4;
  background-color: #fbfcfd;
  width: 550px;
  height: 300px;
}
#second_box {
  display: inline-block;
}
#myTabs {
  font-size: 25px;
}
#myTabContent {
  display: inline-block;
  margin-top: 20px;
  margin-left: 10px;
  font-size: 15px;
}
#nav-tabs {
  display: inline-block;
}
#nav_bar_tabs {
  font-size: 300px;
}
</style>

<!-- CSS libraries -->
<style src="./bootstrap.css"></style>
