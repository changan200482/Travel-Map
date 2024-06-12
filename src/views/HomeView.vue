<script setup>
import MapView from '../components/Map.vue'
import MapTools from '../components/MapTools.vue'
import User from '../components/User.vue'
</script>

<template>
	<MapTools id="maptools"/>
	<User id="user"/>
	<MapView/>
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
</style>

