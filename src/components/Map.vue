<template>
    <div class="container" ref="container"></div>
</template>
  
<style scoped>
    .anchorBL {
        display: none;
    }
    html,body,#container {
            width: 100%;
            height: 100%;
            overflow: hidden;
            margin: 0;
            padding: 0
        }
        .info {
            z-index: 999;
            width: auto;
            padding: 10px;
            margin-left: 10px;
            position: fixed;
            top: 10px;
            background-color: #fff;
            border-radius: 5px;
            font-size: 14px;
            color: #666;
            box-shadow: 0 2px 6px 0 rgba(27, 142, 236, 0.5);
        }
        .selbox {
            margin: 8px 0;
        }
        select {
            width: 180px;
            height: 30px;
            border: 1px solid #ddd;
        }
</style>
    
<script setup>
    import { ref, onMounted } from 'vue';
    import bus from '@/utils/eventBus'
    import EVENTS from '@/utils/EVENTS'
    const container = ref(null);
    onMounted(() => {
        try {
            const { BMapGL } = window;
            const map = new BMapGL.Map(container.value);
            map.enableScrollWheelZoom(true);
            map.centerAndZoom('山东省', 9);
            
            function sendNumber() {
                bus.emit(EVENTS.SENDTOBROTHER, map)
            }  // 传值，自定义事件向兄弟组件传递数据
            sendNumber();

        }
        catch (error) {
            console.error('脚本加载失败:', error);
        }
});

</script>
