<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <a class="navbar-brand" href="/#/">THE EMILY DICKINSON COLLECTIVE</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="/#/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/#/poems">Poems</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/#/macros">Macros</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/#/about">About</a>
          </li>
        </ul>
      </div>
    </nav>
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
  /*-webkit-font-smoothing: antialiased;*/
  -moz-osx-font-smoothing: grayscale;
/*  text-align: center;*/
  /*background-color: #2c3e50;*/
  /*color: #2c3e50;*/
  /*margin-top: 20px;*/
  /*margin-left: 20px;*/

}
@import'bootstrap.css'
</style>
