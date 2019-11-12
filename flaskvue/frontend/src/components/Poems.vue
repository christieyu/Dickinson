<template>
	<div>
		<p>Poems</p>
		{{ poems }}
	</div>
</template>

<script>
export default {
  name: 'Poems',
  data: () => ({
	  poems: '',
	}),
  methods: {

  },
  async beforeMount() {
  	let poemUrl = new URL("http://127.0.0.1:5000/poems");
  	let response = await fetch(poemUrl);
  	let data = await response.json();
  	this.poems = data;
  	console.log(this.poems);
  },
}
</script>
