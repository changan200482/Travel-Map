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
            var geoc = new BMapGL.Geocoder();
        // --- 添加行政区划 --- 
            var dist = new BMapGL.DistrictLayer({
                name: '(山东省)',
                kind: 1,
                fillColor: '#FCF5EB',
                fillOpacity: 0.3,
                strokeColor: '#000000',
                strokeWeight:'0.3',
            });
            var bdary = new BMapGL.Boundary();
            bdary.get('山东省', function (rs) {
                // 绘制行政区
                for (var i = 0; i < rs.boundaries.length; i++) {
                    var path = [];
                    var xyArr = rs.boundaries[i].split(';');
                    var ptArr = [];
                    for (var j = 0; j < xyArr.length; j++) {
                        var tmp = xyArr[j].split(',');
                        var pt = new BMapGL.Point(tmp[0], tmp[1]);
                        ptArr.push(pt);
                    }
                    var mapmask = new BMapGL.MapMask(ptArr, {
                        isBuildingMask: true,
                        isPoiMask: true,
                        isMapMask: true,
                        showRegion: 'inside',
                        topFillColor: '#5679ea',
                        topFillOpacity: 0.5,
                        sideFillColor: '#5679ea',
                        sideFillOpacity: 0.9
                    });
                    //map.addOverlay(mapmask); //只显示山东区域
                    var border = new BMapGL.Polyline(ptArr, {
                        strokeColor: '#4ca7a2',
                        strokeWeight: 3,
                        strokeOpacity: 1
                    });
                    map.addOverlay(border);
                }
            });

            
        // --- 行政区划添加鼠标事件 ---
            dist.addEventListener('mouseover', function (e) {
                e.currentTarget.setFillColor('#FCF5EB');
            });
            dist.addEventListener('mouseout', function (e) {
                e.currentTarget.setFillColor('#FCF5EB');
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
                bus.emit(EVENTS.SEND_DIST,dist)
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
