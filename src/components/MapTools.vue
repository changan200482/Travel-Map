<template>
  <div :style="{ display: 'flex',flexDirection: 'column',gap: '1rem' }">
        <a-tooltip content="旅行足迹" position="right">
            <a-switch id="switch"></a-switch>
        </a-tooltip>

        <div class="toolbox">
            <a-popover position="right" trigger="click" default-popup-visible="true">               
                <icon-apps id="toolsIcon"/>
                    <template #content>
                        <a-button @click="abc()">驾车路线规划</a-button>
                            
                        <a-button>步行路线规划</a-button>
                        <a-button>公交、地铁路线规划</a-button>
                    </template>
            </a-popover>
        </div>
  </div>
 
</template>


<style scoped>
#userBox {
      display: flex;
      flex-direction:row;
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
  
  #r-result,#r-result table{
      width:100%;
      height:100%;
  }
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

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import bus from '@/utils/eventBus';
import EVENTS from '@/utils/EVENTS';

export default {
  setup() {
    let map = ref(null);
    let walking = null; // 新增：用于存放WalkingRoute实例
    let startMarker = null;
    let endMarker = null;
    let geocoder = new BMapGL.Geocoder();

    const initMapListeners = () => {
      if (map.value) {
        
        map.value.addEventListener("click", function(e) {
          var latlng = e.latlng;

          if (!startMarker) {
              startMarker = new BMapGL.Marker(latlng);
              map.value.addOverlay(startMarker);
              alert("已设置起点，请点击地图设置终点");

              // 将起点坐标转换为地址
              geocoder.getLocation(latlng, function(rs){
                  var addComp = rs.addressComponents;
                  var startAddress = addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber;
                  console.log(startAddress);
                  console.log(rs.addressComponents);
                  
                  // 仅当起点和终点都设置后，才执行搜索
                  if (endMarker) {
                      searchRoute(startAddress, endMarker.getPosition());
                  }
              });
          } 
          else if (!endMarker) {
              endMarker = new BMapGL.Marker(latlng);
              map.value.addOverlay(endMarker);
              alert("已设置终点，开始搜索路线");

              // 将终点坐标转换为地址
              geocoder.getLocation(latlng, function(rs){
                  var addComp = rs.addressComponents;
                  var endAddress = addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber;
                  console.log(endAddress);
                  console.log(rs.addressComponents);
                  
                  // 确保startMarker已被设置，然后执行搜索
                  if (startMarker) {
                      searchRoute(startMarker.getPosition(), endAddress);
                  }
              });
          }
        });
      } 
      else {
        console.warn("Map instance not ready yet.");
      }
    };
    function searchRoute(startAddress, endPositionOrAddress) {
            // 确保传入的参数是正确的类型，如果是字符串（地址），则需要先进行地理编码
          
            if (typeof endPositionOrAddress === 'string') { 
                geocoder.getPoint(endPositionOrAddress, function(point) {
                    if (point) {
                        walking.search(startAddress, point);
                    } else {
                        console.error("无法解析终点地址为坐标");
                    }
                });
            } else {
              
                walking.search(startAddress, endPositionOrAddress); 
            }
        }
    const setupWalkingRoute = () => {
      if (map.value) {
        walking = new BMapGL.WalkingRoute(map.value, { renderOptions: { map: map.value, panel: "r-result", autoViewport: true } });
      }
    };

    const removeMapListeners = () => {
      if (map.value) {
        map.value.removeEventListener("click", initMapListeners); // 修正：移除正确的监听器
      }
    };

    // 从事件总线接收地图实例
    const receiveMapInstance = (data) => {
      map.value = data;
      
    };

    onMounted(() => {
      bus.on(EVENTS.SENDTOBROTHER, receiveMapInstance);
    });

    onUnmounted(() => {
      bus.off(EVENTS.SENDTOBROTHER, receiveMapInstance);
      removeMapListeners();
    });

    // 移除abc方法调用，因为它不再必要
    function abc(){
      initMapListeners(); // 地图实例接收到后初始化监听器
      setupWalkingRoute(); // 同时初始化 WalkingRoute
    }
    return {
      searchRoute, // 确保searchRoute逻辑正确且依赖于walking.value
      abc,
      initMapListeners
    };
  },
};
</script>