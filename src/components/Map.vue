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
        //const point = new BMapGL.Point(116.404, 39.915);
       // map.centerAndZoom(point, 10);
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
            e.currentTarget.setFillColor('#618bf8');
        });

        dist.addEventListener('click', function (e) {
           // 遍历所有区划，重置非当前点击区划的透明度，保持它们不透明
            // dist.getDistricts().forEach((district) => {
            //     if (district !== e.currentTarget) {
            //         district.setFillColor(district.style.fillColor); // 重置颜色
            //         district.setFillOpacity(1); // 设置为不透明
            //     }
            // });

            // 设置当前点击区划为透明
            e.currentTarget.setFillOpacity(0); // 设置透明度，例如0.5为半透明
            
        });

        function sendNumber() {
            bus.emit(EVENTS.SENDTOBROTHER, map) // 更改此处为 map，而非 ref(map)
        }  // 传值，自定义事件向兄弟组件传递数据
        sendNumber();
    }
    catch (error) {
        console.error('脚本加载失败:', error);
    }

// map.addEventListener('click',function(e){
//     var latlng = e.latlng;
//     Marker = new BMapGL.Marker(latlng);
//     var geoc = new BMapGL.Geocoder();
//     console.log(latlng);
//     geoc.getLocation(latlng, function(rs){
//                   var addComp = rs.addressComponents;
//                   var startAddress = addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber;
//                   console.log(startAddress);
//                 });            
// });



});

</script>