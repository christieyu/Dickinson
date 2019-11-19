<template>
  <div id="app">
    <h1>THE EMILY DICKINSON COLLECTIVE</h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
/*  text-align: center;*/
  /*background-color: #2c3e50;*/
  color: #2c3e50;
  margin-top: 20px;
  margin-left: 20px;

}
</style>
