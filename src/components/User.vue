<template>
    <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
        <div id="userBox">
            <icon-user class="userCard" title="个人信息"/>
            <hr>
            <icon-more class="userCard" title="更多信息"/>
        </div>
        <div class="functionalModule">
            <a-tooltip content="添加留言" position="left">
                <icon-plus class="iconBox" title="添加留言"/>
            </a-tooltip>
        </div>
        <div class="functionalModule">
            <a-tooltip content="历史记录" position="left">
                <icon-clock-circle class="iconBox" title="历史记录"/>
            </a-tooltip>
        </div>

    </div>
</template>

<style scoped>
    hr{
        width: 2rem;
        margin: auto;
    }
    #userBox {
        display: flex;
        flex-direction: column;
        background-color: aliceblue;
        border-radius: 0.8rem;
    }
    .userCard {
        margin: 0.7rem;
        width: 2rem;
        height: 2rem;
        cursor: pointer;
    }
    .functionalModule {
        background-color: aliceblue;
        border-radius: 0.8rem;
    }
    .iconBox {
        display: flex;
        text-align: center;
        margin: 0.6rem;
        width: 2.2rem;
        height: 2.1rem;
        cursor: pointer;
    }
</style>

<script setup>

</script>