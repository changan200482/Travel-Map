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

const container = ref(null);

onMounted(() => {
    try {
        // 确保地图已加载
        const { BMapGL } = window;
    const map = new BMapGL.Map(container.value);
    const point = new BMapGL.Point(116.404, 39.915);
        map.centerAndZoom(point, 10);
        map.enableScrollWheelZoom(true);
    var zoomCtrl = new BMapGL.ZoomControl();
    map.addControl(zoomCtrl);

    // --- 添加行政区划 ---
    var dist = new BMapGL.DistrictLayer({
        name: '(山东省)',
        kind: 1,
        fillColor: '#618bf8',
        fillOpacity: 1,
        strokeColor: '#daeafa',
        viewport: true
    });
    map.addDistrictLayer(dist);

    // --- 行政区划添加鼠标事件 ---
    dist.addEventListener('mouseover', function (e) {
        e.currentTarget.setFillColor('#9169db');
    });
    dist.addEventListener('mouseout', function (e) {
        e.currentTarget.setFillColor(e.currentTarget.style.fillColor);
    });
    }
   
    catch (error) {
        console.error('脚本加载失败:', error);
    }
});
</script>