<template>
    <div class="container" ref="mapContainer"></div>
</template>
  
<style scoped>
    .container {
        width: 100vh;
        height: 100vh;
    }
</style>
  
<script setup>
import { ref, onMounted } from 'vue';

const mapContainer = ref(null);

onMounted(() => {
    try {
        // 确保地图已加载
        const { BMapGL } = window;

        if (typeof window.BMapGL === 'undefined') {
        throw new Error('BMapGL 未定义， 请检查百度地图API脚本是否正确加载');
        }
        // 初始化百度地图
        const map = new BMapGL.Map(mapContainer.value);
        const point = new BMapGL.Point(116.404, 39.915);
        map.centerAndZoom(point, 10);
        map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放

        map.setMapStyleV2({ styleJson: darkStyle });
        var fillLayer = null;


        function addFillLayer() {
        fetch("https://mapopen-pub-jsapigl.bj.bcebos.com/svgmodel/fillLayerData.json").then(res => {
            return res.json();
        }).then(testFillData => {
            if (!fillLayer) {
                fillLayer = new BMapGL.FillLayer({
                    crs: 'GCJ02',
                    enablePicked: true,
                    autoSelect: true,
                    pickWidth: 30,
                    pickHeight: 30,
                    selectedColor: 'green', // 悬浮选中项颜色
                    border: true,
                    style: {
                        fillColor: ['case', ['boolean', ['feature-state', 'picked'], false], 'red', ['match', ['get', 'name'], '海淀区', '#ce4848', '朝阳区', 'blue', '通州区', 'blue', '丰台区', '#6704ff', '房山区', '#6704ff', 'orange']],
                        fillOpacity: .3,
                        strokeWeight: 1,
                        strokeColor: 'blue',
                    }
                });

                fillLayer.addEventListener('click', function (e) {
                    if (e.value.dataIndex !== -1 && e.value.dataItem) {
                        console.log('click', e.value.dataItem);
                        // 使用样式配置，实现单选或多选效果
                        // this.updateState(e.value.dataIndex, { picked: true }, true);
                    }
                })

            }
            map.addNormalLayer(fillLayer);
            fillLayer.setData(testFillData);
        })
        }
        // 移除图层
        function removeFillLayer() {
            map.removeNormalLayer(fillLayer);
        }

        addFillLayer();
    }
   
    catch (error) {
        console.error('脚本加载失败:', error);
    }
});
</script>