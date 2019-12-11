<template>
  <div id="app">
    <img id="emily_img" style="width: 100%;" v-bind:src="'/static/img/emily3.jpg'">
    <h1 id="master_title">THE <br> 
      <div id="master_title_scarlet">SCARLET</div> 
      EXPERIMENT
    </h1>
    <blockquote class="blockquote text-right" id="block_quote">
      <p class="dickinson_poem" style="color:#ffffff"><b>
        Split the lark and you'll find the music, <br>
        Bulb after bulb, in silver rolled, <br>
        Scantily dealt to the summer morning, <br>
        Saved for your ear when lutes be old. <br>
        <br>
        Loose the flood, you shall find it patent, <br>
        Gush after gush, reserved for you; <br>
        Scarlet experiment! sceptic Thomas, <br>
        Now, do you doubt that your bird was true?
      </b></p>

      <footer class="blockquote-footer" style="color:#ffffff"> <cite title="Source Title">Emily Dickinson</cite></footer>
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
  height: 720px;
  width: 350px;
}
#master_title {
  font-size: 100px;
  position: absolute;
  bottom: 0px;
  color: #ffffff;
}
#master_title_scarlet {
  font-size: 100px;
  color: #ff0321;
  position: absolute;
  bottom: 60px;
}
#block_quote {
  position: absolute;
  top: 90px;
  right: 16px;
}
</style>

<!-- CSS libraries -->
<style src="./bootstrap.css"></style>


