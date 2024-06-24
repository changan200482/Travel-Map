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
        var zoomCtrl = new BMapGL.ZoomControl();
        map.addControl(zoomCtrl);
        var geoc = new BMapGL.Geocoder();
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
            e.currentTarget.setFillColor('#618bf8');
        });

        dist.addEventListener('click', function (e) {
            console.log(dist);
           // 遍历所有区划，重置非当前点击区划的透明度，保持它们不透明
            //  dist.getDistricts().forEach((district) => {
            //     if (district !== e.currentTarget) {
            //         district.setFillColor(); // 重置颜色
            //         district.setFillOpacity(1); // 设置为不透明
            //     }
            // });

            // 设置当前点击区划为透明
           e.currentTarget.setFillOpacity(0); // 设置透明度，例如
        });
        //dist.addEventListener('click', function (e) {
    // 假设e.currentTarget.getBounds()可以获取到当前点击行政区划的边界
    
    // var bounds = e.currentTarget.getBounds();
    // console.log(bounds);
    // // 创建一个半透明的遮罩层
    // var maskLayer = new BMapGL.GroundOverlay(
    //     bounds.getSouthWest(), // 西南角坐标
    //     bounds.getNorthEast(),
    //     console.log("我是天子！"),
    //     {
    //         opacity: 0, // 设置遮罩层的透明度
    //         bounds: bounds // 设置遮罩层显示的边界范围
    //     }
    // );
    // map.addOverlay(maskLayer); // 将遮罩层添加到地图上

    // 如果需要，你可以存储这个遮罩层的引用，以便于后续操作，比如移除或调整透明度
    // ...
//});
        function sendNumber() {
            bus.emit(EVENTS.SENDTOBROTHER, map) 
        }  // 传值，自定义事件向兄弟组件传递数据
        sendNumber();

        // map.addEventListener('click',function(e){
        //     var latlng = e.latlng;
        //     console.log(latlng);
        //     var startAddress = null;
        //     geoc.getLocation(latlng, function(rs){
        //         if(!startAddress){
        //             var addComp = rs.addressComponents;
        //            startAddress =  addComp.city;
        //           console.log(startAddress);
        //           map.centerAndZoom(startAddress, 10);
        //         }
        //     });
        // });
    }
    catch (error) {
        console.error('脚本加载失败:', error);
    }
});

</script>
