<template>
    <div :style="{ display: 'flex',flexDirection: 'column',gap: '1rem' }">
        <a-tooltip content="旅行足迹" position="right">
            <a-switch id="switch"></a-switch>
        </a-tooltip>

        <div class="toolbox">
            <a-tooltip content="更多工具" position="bottom">
                <icon-double-right id="toolsIcon"/>
            </a-tooltip>
        </div>
  </div>

</template>

<style scoped>
    .toolbox {
        background-color: aliceblue;
        border-radius: 0.5rem;
        width: 2.5rem;
        height: 2rem;
        display: grid;
        grid-template-columns: 1fr;
    }
    #toolsIcon{
        margin: auto;
        width: 1.5rem;
        height: 1.5rem;
        cursor: pointer;
    }
</style>

<script setup>

</script>