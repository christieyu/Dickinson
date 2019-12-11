<template>
  <div id="app">
    <h1 id="master_title">THE <br> 
      <div id="master_title_scarlet">SCARLET</div> 
      EXPERIMENT
    </h1>
    <blockquote class="blockquote text-right">
      <p class="dickinson_poem">
        Split the lark and you'll find the music, <br>
        Bulb after bulb, in silver rolled, <br>
        Scantily dealt to the summer morning, <br>
        Saved for your ear when lutes be old. <br>
        <br>
        Loose the flood, you shall find it patent, <br>
        Gush after gush, reserved for you; <br>
        Scarlet experiment! sceptic Thomas, <br>
        Now, do you doubt that your bird was true?
      </p>

      <footer class="blockquote-footer"> <cite title="Source Title">Emily Dickinson</cite></footer>
      <img id="emily_img" v-bind:src="'/static/img/dickinson.png'">
    </blockquote>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  // src: require('../assets/logo.png')
  data () {
    return {
      // imageURL: require("emily.png"),
      // myImage: require('./assets/emily.png'),
      msg: 'This is the Emily Dickinson Collective!'
    }
  }
}
</script>


<style>
#dickinson_poem {
  margin-right: 20px;
}
#emily_img {
  margin-top: 20px;
  margin-right: 20px;
  height: 500px;
  width: 350px;
}
#master_title {
  font-size: 100px;
  position: absolute;
  bottom: 0px;
}
#master_title_scarlet {
  font-size: 100px;
  color: #ff0321;
  position: absolute;
  bottom: 60px;
}
#lark_poem {
  padding-left: 20px;
}
</style>

<!-- CSS libraries -->
<style src="./bootstrap.css"></style>


