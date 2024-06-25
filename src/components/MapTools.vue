<template>
  <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
    <a-tooltip content="旅行足迹" position="right">
      <a-switch id="switch"></a-switch>
    </a-tooltip>
    <div class="toolbox">
      <icon-compass id="toolsIcon" title="路线规划" @click="showPopup = true" />
    </div>
    <!-- <div v-show="showPopup" class="popup" :style="{ top: `${popupTop}px`, right: `${popupRight}px` }"> -->

	<div id="r-result" :style="{ height:'300px' }">请输入:<input type="text" id="suggestId" size="20"  style="width:150px;" /></div>
  <div id="searchResultPanel" style="border:1px" ></div>
    
  </div> 

</template>

<style scoped>
  #r-result {
    width: 100%;
  }

  #userBox {
    display: flex;
    flex-direction: row;
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

  .toolbox {
    background-color: aliceblue;
    border-radius: 0.5rem;
    width: 2.5rem;
    height: 2rem;
    display: grid;
    grid-template-columns: 1fr;
  }

  #toolsIcon {
    margin: auto;
    width: 1.5rem;
    height: 1.5rem;
    cursor: pointer;
  }

  .popup {
    position: fixed; /* 固定定位，使其脱离文档流 */
    top: 80px; /* 默认距离顶部20px，实际值由data中的popupTop控制 */
    right: 100px; /* 默认距离右边20px，实际值由data中的popupRight控制 */
    background-color: white;
    padding: 200px;
    border: 1px solid #ccc;
    z-index: 1000; /* 确保弹窗在最上层 */
  }
  </style>
  <script>
import { ref } from 'vue';
import bus from '@/utils/eventBus';
import EVENTS from '@/utils/EVENTS';

export default {
  setup() {
    let map = ref(null);
    let myValue = null;
    let selectedPlaces = [];
    let promises = []; 
    let waypoints=[];
    // 从事件总线接收地图实例
    bus.on(EVENTS.SENDTOBROTHER, (data) => {
      map.value = data;

      if (!map.value) {
        console.error('地图实例尚未准备好');
        return;
      }
      // 创建 Autocomplete 实例
        var ac = new BMapGL.Autocomplete({ "input": "suggestId", "location": map.value });
      
        ac.addEventListener("onconfirm", function(e) {
            var _value = e.item.value;
            console.log(_value)
            myValue = _value.province + _value.city + _value.district + _value.street + _value.business;

            console.log("2222")
            G("searchResultPanel").innerHTML = "onconfirm<br />index = " + e.item.index + "<br />myValue = " + myValue.value;
            selectedPlaces.push(myValue); // 将选择的地点添加到数组中
            console.log("已选择的地点:", selectedPlaces);
            console.log(myValue);
            setPlace();
        });
        ac.addEventListener("onhighlight", function(e) {  // 鼠标放在下拉列表上的事件
          console.log("我是天子");
            var str = "";
            var _value = e.fromitem.value;
            var value = "";
            if (e.fromitem.index > -1) {
              value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
            }    
            str = "FromItem<br />index = " + e.fromitem.index + "<br />value = " + value;
            
            value = "";
            if (e.toitem.index > -1) {
              _value = e.toitem.value;
              value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
            }    
            str += "<br />ToItem<br />index = " + e.toitem.index + "<br />value = " + value;
            G("searchResultPanel").innerHTML = str;
        });
        function G(id) {
          return document.getElementById(id);
        }
        function calculateRoute(startPoint, endPoint) {
          var driving = new BMapGL.DrivingRoute(map.value, {
            renderOptions: {map: map.value, autoViewport: true}
          });
          if (selectedPlaces.length >= 2) {
          driving.search(startPoint, endPoint,{
              waypoints:[waypoints]
              });
          }
          else{
              driving.search(startPoint, endPoint);
          }
	      }
        function getAddressCoordinate(address) {
    return new Promise((resolve, reject) => {
        var geocoder = new BMapGL.Geocoder();
        geocoder.getPoint(address, function(point) {
            if (point) {
                resolve(point);
            } else {
                reject("未能解析地址为坐标");
            }
        }, "北京市"); // 最后一个参数为城市名，提高解析精度
    });
}
    function setPlace() {
  map.value.clearOverlays(); // 清除地图上所有覆盖物

  // 如果 selectedPlaces 中有两个及以上的地点，开始查询路线
  if (selectedPlaces.length >= 2) {
    for (let i = 1; i < selectedPlaces.length - 1; i++) {
      waypoints.push(selectedPlaces[i]);
  }

    // 现在，waypoints 数组包含了除首尾之外的所有地点
    console.log("中间途径点:", waypoints);

    for (let i = 0; i < selectedPlaces.length - 1; i++) {
      promises.push(
        getAddressCoordinate(selectedPlaces[i])
          .then((start) =>
            getAddressCoordinate(selectedPlaces[i + 1]).then((end) => calculateRoute(start, end))
          )
          .catch((err) => console.error(err))
      );
    }

    // 使用 Promise.all 来等待所有路线查询完成
    Promise.all(promises)
      .then(() => console.log("所有路线查询完成"))
      .catch((err) => console.error(err));

    G("suggestId").value = ""; // 无论成功还是失败，都清空输入框
  } else {
    // 使用 Promise 处理单个地点的搜索逻辑，保持原有功能
    new Promise((resolve, reject) => {
      var local = new BMapGL.LocalSearch(map.value, {
        onSearchComplete: function (results) {
          if (local.getStatus() === BMAP_STATUS_SUCCESS) {
            resolve(results);
          } else {
            reject("搜索失败，状态码：" + local.getStatus());
          }
        },
      });
      console.log("2222")
      local.search(myValue);
    })
      .then((results) => {console.log(results);console.log(results.getNumPois())
        if (results.getNumPois() > 0) {
          var pp = results.getPoi(0).point; // 获取第一个智能搜索的结果
          console.log(pp)
          map.value.centerAndZoom(pp, 18);
          map.value.addOverlay(new BMapGL.Marker(pp)); // 添加标注
        } else {
          alert("没有找到匹配的地点");
        }
      })
      .catch((errorMessage) => {
        alert("搜索过程中出现问题：" + errorMessage);
      })
      .finally(() => {
        G("suggestId").value = ""; // 无论成功还是失败，都清空输入框
      });
  }
}
    });

    const showPopup = ref(false);
    const popupTop = 80; // 距离顶部20px
    const popupRight = 100; // 距离右边20px
    //const inputRef = ref('');

    // 切换弹窗显示状态的方法
    const togglePopup = () => {
      showPopup.value = !showPopup.value;
    };
    return {
      showPopup,
      popupTop,
      popupRight,
      //inputRef,
      togglePopup,
    };
  },
};
</script>