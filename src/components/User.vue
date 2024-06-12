<template>
    <div :style="{ display: 'flex' }">
        <div id="userBox">
            <icon-user class="userCard"/>
            <icon-more class="userCard"/>
        </div>
    </div>
</template>

<style scoped>
    #userBox {
        display: flex;
        flex-direction: column;
        background-color: aliceblue;
    }

</style>

<script setup>

</script>