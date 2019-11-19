<template>
	<div id="app">
    <div id="titles">
      <div id="single_title" v-for="poem in poems" @click="getPoemDetails(poem['title'])">{{poem['title']}}</div>
    </div>
    <!-- {{details}} -->
    <div id="single_poem"><div>{{details}}</div></div>
 
	</div>
</template>

<script>
export default {
  name: 'Poems',
  data: () => ({
	  poems: '',
    details: '',
	}),
  methods: {
    getPoemDetails: function(title) {
      for (let i = 0; i < this.poems.length; i++) {
        if (this.poems[i]['title'] === title) {
          this.details = this.poems[i].poems;
          return;
        }
      }
    }
  },
  async beforeMount() {
  	let poemUrl = new URL("http://127.0.0.1:5000/poems");
  	let response = await fetch(poemUrl);
  	let data = await response.json();
  	this.poems = data;
  },
}
</script>


<style>
#app {
  /*display: inline-block;*/
}
#single_title {
  margin-top: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid;
  font-size: 18px;
}
#titles {
  /*display: inline-block;*/
  margin-top: 10px;
  border: 1px solid;
  border-color: #edeef4;
  width: 550px;
  height: 400px;
  background-color: #f4f5f8;
  overflow: auto;
}
#single_poem {
  /*display: inline-block;*/
  margin-top: 10px;
  margin-bottom: 10px;
  border: 1px solid;
  border-color: #edeef4;
  background-color: #fbfcfd;
  width: 550px;
  height: 300px;
}
</style>
