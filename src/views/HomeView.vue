<script setup>
import MapView from '../components/Map.vue'
import MapTools from '../components/MapTools.vue'
import User from '../components/User.vue'
import Forum from '../components/Forum.vue'
</script>

<template>
	<MapTools id="maptools"/>
	<User id="user"/>
	<MapView/>
	<Forum id="forum"/>
</template>

<style scoped>
	#user{
		position: absolute;
		top: 0;
		right: 0;
		z-index: 1000;
		padding: 35px;
	}
	#maptools {
		position: absolute;
		bottom: 0;
		left: 0;
		z-index: 1000;
		padding: 35px;
	}
	#forum {
		position: absolute;
		top: 0;
		left: 0;
		z-index: 1000;
		padding: 35px;
	}
</style>

