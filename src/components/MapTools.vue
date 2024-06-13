<template>
    <div :style="{ display: 'flex' }">
        <a-card id="buttonCard">
            <a-space>
                <a-button type="primary" class="button" >添加图层</a-button>
                <a-button type="primary" class="button">删除图层</a-button>
            </a-space>
        </a-card>
  </div>

</template>

<style scoped>
    .button {
        border-radius: 4px;
    }
    #buttonCard {
        border-radius: 1rem;
    }
</style>

<script setup>

</script>