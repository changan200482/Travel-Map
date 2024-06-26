<template>
    <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
      <div id="userBox">
        <icon-menu-fold @click="selfInfoClick" v-if="ISLOGOIN" class="userCard"/>
        <icon-user v-else @click="loginClick" class="userCard" title="个人信息"/>   
        <!--登陆界面对话框-->
          <a-modal v-model:visible="loginVisible" 
          mask="false"
          title="账号登入"
          width="520px"
          ok-text="登录"
          @ok="login"
          draggable>
              <a-form :model="loginForm">
                  <a-form-item field="acount" label="邮箱：">
                    <a-input 
                    v-model="loginForm.acount"
                    placeholder="请输入邮箱" allow-clear />
                  </a-form-item>

                  <a-form-item field="password" label="密码：">
                    <a-input-password
                    v-model="loginForm.password"
                    placeholder="请输入密码"
                    allow-clear
                    />
                  </a-form-item>
                  <a-form-item>
                    <a-link @click="newAcount">注册新用户</a-link>
                    <a-link @click="forgetPassword">忘记密码</a-link>
                  </a-form-item>
                  <a-form-item no-style="true">
                    <a-button type="primary" @click="login">登录</a-button>
                  </a-form-item>
              </a-form>
              <template #footer>
                  <a-form formItemLayout="{ wrapperCol: { span: 24 }, labelCol: { span: 0 } }">
                  </a-form>
              </template>
          </a-modal>
          <!--注册界面对话框-->
          <a-modal 
          mask="false"
          v-model:visible="registerVisible" 
          title="注册" 
          @ok="register"
          ok-text="注册"
          width="550px"
          draggable>
            <a-form :model="registerForm">
              <a-form-item field="name" label="用户名：">
                  <a-input 
                  v-model="registerForm.name"
                  placeholder="请输入您的用户名"/>
              </a-form-item>
              <a-form-item field="acount" label="邮箱：">
                  <a-input 
                  v-model="registerForm.acount"
                  placeholder="请输入您的邮箱"/>
              </a-form-item>
              <a-form-item field="password" label="密码：">
                  <a-input-password
                  v-model="registerForm.password" 
                  placeholder="请输入您的密码"/>
              </a-form-item>
              <a-form-item field="confirmPassword" label="确认密码">
                  <a-input-password
                  v-model="registerForm.confirmPassword"
                  placeholder="请确认您的密码"
                  />
              </a-form-item>
              <a-form-item no-style="true">
                    <a-button type="primary" @click="register">注册</a-button>
              </a-form-item>
            </a-form>
            <template #footer>
                  <a-form formItemLayout="{ wrapperCol: { span: 24 }, labelCol: { span: 0 } }">
                  </a-form>
            </template>
          </a-modal>

          <!--个人信息对话框-->
          <a-modal 
          v-model:visible="selfInfoVisible"
          title="个人信息"
          width="520px">
          <a-space :style="{display:'flex',flexDirection:'column',gap:'0.6rem'}">
            <img
            id="avator"
            :style="{width:'4.5rem'}"
            src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp" alt="头像">
            <h2>textname</h2>
            <h3>email</h3>
            <a-space >
              <a-tabs default-active-key="1" :style="{height:'16rem'}">
                <a-tab-pane key="1" title="帖子">
                  Content of Tab Panel 1
                </a-tab-pane>
                <a-tab-pane key="2" title="规划">
                  Content of Tab Panel 2
                </a-tab-pane>
              </a-tabs>
            </a-space>
          </a-space>
          <template #footer>
            <a-form formItemLayout="{ wrapperCol: { span: 24 }, labelCol: { span: 0 } }">
            </a-form>
          </template>
          </a-modal>


          <hr>


          <a-tooltip content="路线规划" position="left">
              <icon-check-square @click="roadPlanClick" class="iconBox" title="路线规划"/>
          </a-tooltip>
          <a-modal 
          v-model:visible="roadPlanVisible"
          title="添加路线"
          mask="false"
          hide-cancel="true"
          ok-text="查看路线"
          @ok="setPlace">
            <a-form>
              <a-form-item label="添加地点：">
                
                <a-space>
                  <a-input
                  :style="{width:'200px'}" 
                  placeholder="请输入需要查询的地点" 
                  button-text="查询" 
                  search-button
                  v-model="searchInput"
                  id="suggestId"/>
                  <a-button type="primary" @click="locationView(searchInput)" >查询</a-button>

                </a-space>

              </a-form-item>
              <a-form-item label="检索列表：">
                <a-space>
                  <a-select
                    :style="{width:'250px'}"
                    placeholder="点击查看"
                    @dropdown-scroll="handleScroll"
                    @dropdown-reach-bottom="handleReachBottom"
                    v-model="selectElement"
                  >
                    <a-popover position="right" v-for="item in searchResult" key="item.title">
                      <a-option>{{ item.title }}</a-option>
                      <template #content>
                        {{ item.address }}
                      </template>
                    </a-popover>

                  </a-select>
                  <a-button type="primary" @click="addResult">
                    <template #icon>
                      <icon-plus />
                    </template>
                  </a-button>
                </a-space>

              </a-form-item>

              <a-form-item label="地点：">
                <a-space direction="vertical" size="large">
                  <a-space wrap>
                    <template v-for="(item,index) in selectedPlaces" :key="item.title">
                      <a-tag size="large" closable 
                      :color="index === 0 ? 'red' : index === selectedPlaces.length - 1 ? 'blue' : ''"
                      @close="removeResult(item)">{{ item.title }}</a-tag>
                    </template>
                  </a-space>
                  <a-space>
                    <a-input :style="{width:'220px'}" placeholder="描述路线" default-value="默认路线" allow-clear :model-value="addInfoInput"/>
                    <a-button type="primary" @click="savePlace">添加路线</a-button>
                  </a-space>
                </a-space>
              </a-form-item>

            </a-form>
          </a-modal>
        </div>


        <div class="functionalModule">
          <a-tooltip content="发布讨论" position="left">
            <a-space>
              <icon-plus @click="addTalkClick" class="iconBox" title="添加留言" />
            </a-space>
            <a-modal 
            title="发布讨论"
            v-model:visible="addTalkVisible"
            ok-text="发布"
            @ok="talk"
            >
              <a-form :model="addTalkForm">
                <a-form-item field="location" label="标题：">
                  <a-input 
                  :style="{width:'320px'}"/>
                </a-form-item>
                <a-form-item field="location" label="地点：">
                  <a-input 
                  :style="{width:'320px'}"/>
                </a-form-item>
                <a-form-item 
                id="talkContent"
                field="location" 
                label="内容：" 
                >
                <a-textarea 
                  auto-size="true"
                  placeholder="添加回复" 
                  allow-clear
                  :style="{width:'320px',height:'140px'}"/>
                </a-form-item>
              </a-form>
            </a-modal>
          </a-tooltip>
        </div>
        <div class="functionalModule">
          <a-popover position="left">
            <a-space>
              <icon-more class="userCard"/>
            </a-space>
              <template #content>
                <h4>开发者信息</h4>
                <a-space>
                  <a-link href="C:\Users\王\Desktop\网页\HTML\w.html" >Mr.W</a-link>
                </a-space>
              </template>
          </a-popover>
        </div>

        <a-tooltip content="工作范围" position="right" >
            <a-switch id="switch" type="line" v-model="isDist" @change="addDist"/>
        </a-tooltip>
    </div>
</template>

<style scoped>
    #roadView{
      display: flex;
      justify-content: flex-end;
    }
    hr{
      width: 2rem;
      margin: auto;
    }
    #avator{
      border-radius: 3rem;
    }

    #talkContent{
      height: 100px
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
  import { Notification, Radio } from '@arco-design/web-vue';  //引入通知组件
  import axios from 'axios'                             //引入axios
  import { reactive,onMounted, onUnmounted, ref} from 'vue';                 //引入reactive和ref
  import bus from '@/utils/eventBus';
  import EVENTS from '@/utils/EVENTS';


  const loginVisible = ref(false);
  const ISLOGOIN = ref(false)

  const loginClick = () => {
    loginVisible.value = true;
  };                                                    //点击函数visible.value = true;来让绑定visible的对话框显示
                                          
                                            
  const loginForm = reactive({
    acount: '',
    password: '',
  });                                      

  //登录函数，通过axios.post()来向后端发送请求，根据后端返回的数据来判断登录是否成功

  const login = (event) => {

    event.preventDefault(); // 防止表单的默认提交行为

    if(loginForm.acount === '' || loginForm.password === ''){
      Notification.error({
        title: '登录失败',
        content: '邮箱或密码不能为空'
      })
    }

    else{
      axios.post('http://localhost:5000/login', {
      acount: loginForm.acount,
      password: loginForm.password
      })
      .then(function(response){
        console.log(response.data)
        //根据后端返回的数据来判断登录是否成功
        if(response.data == 'loginfail'){     
          Notification.error({
            title: '登录失败',
            content: '密码错误'
          })
        }
        else if(response.data == 'notfound'){
          Notification.error({
            title: '登录失败',
            content: '邮箱不存在'
          })
        }
        else{
          Notification.info({
            title: '登陆成功',
            content: `欢迎回来,` + response.data
          });
          loginVisible.value = false;
          ISLOGOIN.value = true;
        }
      })
      .catch(function(error){
        console.log(error)
      })
    }
  };

  const registerVisible= ref(false);

  const newAcount = () => {
    registerVisible.value = true;
    loginVisible.value = false;
  };

  const registerForm = reactive({
    name : '',
    acount: '',
    password: '',
    confirmPassword: ''
  });     


  const register = (event) => {
    event.preventDefault(); // 防止表单的默认提交行为

    const isValidEmail = (email) => {
        email = registerForm.acount;
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return emailPattern.test(email);
    };

    const isValidUsername = (name) => {
        name =registerForm.name;
        const usernamePattern = /^[a-zA-Z0-9_\u4e00-\u9fa5]+$/;
        return usernamePattern.test(name);
    };

    console.log(isValidUsername)

    if (registerForm.acount === '' || registerForm.password === '') {
        Notification.error({
            title: '注册失败',
            content: '邮箱或密码不能为空'
        });
    } 
    else if (!isValidEmail(registerForm.acount)) {
        Notification.error({
            title: '注册失败',
            content: '无效的邮箱格式'
        });
    } 
    else if (!isValidUsername(registerForm.acount.split('@')[0])) {
        Notification.error({
            title: '注册失败',
            content: '用户名只能包含中文、字母、下划线或数字'
        });
    } 
    else if (registerForm.password !== registerForm.confirmPassword) {
        Notification.error({
            title: '注册失败',
            content: '两次密码不一致'
        });
    } 
    else {
        axios.post('http://localhost:5000/register', {
            acount: registerForm.acount,
            password: registerForm.password,
            name: registerForm.name
        })
        .then(function(response) {
            console.log(response.data);
            if (response.data === 'Success') {
                Notification.info({
                    title: '注册成功'
                });
                registerVisible.value = false;
            } 
            else if (response.data === 'Registered') {
                Notification.error({
                    title: '注册失败',
                    content: '邮箱已被注册'
                });
            }
            else if (response.data === 'Error') {
                Notification.error({
                    title: '注册失败'
                });
            }
        })
        .catch(function(error) {
            console.log(error);
        });
    }
  };

  const selfInfoVisible =ref(false)
  const selfInfoClick = () =>{
    selfInfoVisible.value = true
  }
  const selfInfoForm = reactive({
    avator:'',
    name:'',
    todoList:'',
    ralkList:''
  })

  const roadPlanVisible = ref(false)
  const roadPlanClick = () =>{
    roadPlanVisible.value = true
  }
  const roadPlanForm = reactive({
    title:'',
    startPoint:'',
    endPoint:''
  })

  const addTalkVisible= ref(false);
  const addTalkClick = () => {
    addTalkVisible.value =true
  }
  const addTalkForm = reactive({
    location:'',
    title:'',
    content:''
  })

  const talk = (event) =>{
      event.preventDefault(); // 防止表单的默认提交行为
      if (ISLOGOIN.value) {

      }
      else{
        Notification.error({
            title: '发布失败',
            content: '请登陆后重试'
        });
      }
  }

  //地图服务
  const isDist=ref(false)
  let addInfoInput = ref(null)
  const searchInput = ref(null)
  let local = ref(null);
  let searchResult = ref(null)
  let selectElement = ref(null)
  const selectedPlaces = ref([]);
  let wayPointsArray=ref([]);
  //let wayPointsStr = ref(null)
  let map = ref(null);
  let mapDistrict = ref(null);
  let mapBoundary = ref(null);
  let mapBorder = ref(null);

  var locationView
  var addResult
  var removeResult
  var setPlace
  var savePlace
  var addDist


  bus.on(EVENTS.SENDTOBROTHER, (data) => {
    map.value = data;

    if (!map.value) {
      console.error('地图实例尚未准备好');
      return;
    }

    mapDistrict.value = new BMapGL.DistrictLayer({
      name: '(山东省)',
      kind: 1,
      fillColor: '#FCF5EB',
      fillOpacity: 0.3,
      strokeColor: '#000000',
      strokeWeight: '0.3',
    }); 

    mapBoundary.value = new BMapGL.Boundary();

    // 绘制行政区-----存在问题：边界线很乱
    mapBoundary.value.get('山东省', function (rs) {
      var pointArray = [];
      for (let i =0; i< rs.boundaries.length; i++) {
        var xyArray = rs.boundaries[i].split(';');
        for (let j = 0; j < xyArray.length; j++) {
          var tmp = xyArray[j].split(',');
          var point = new BMapGL.Point(tmp[0], tmp[1]);
          pointArray.push(point);
        }
      }
      mapBorder.value = new BMapGL.Polyline(pointArray, {
        strokeColor: '#4ca7a2',
        strokeWeight: 3,
        strokeOpacity: 1
      });
    })


    locationView = (loc) =>{
      try{
        if (!loc) {
          Notification.error({
            title: '查询失败',
            content: "未输入任何地点"
          })
        }
        var options = {
          onSearchComplete: function(results){
          // 判断状态是否正确
            if (local.value.getStatus() == BMAP_STATUS_SUCCESS){
              const searchData = [];
              for (var i = 0; i < results.getCurrentNumPois(); i ++){
                const poi = results.getPoi(i);
                searchData.push({
                  title: poi.title,
                  address: poi.address,
                  point: poi.point,
                });
              }
              searchResult.value = searchData.filter((place, index, self) =>index === self.findIndex(p =>p.title === place.title));
            }

          }
        };
        local.value = new BMapGL.LocalSearch(map.value, options);
        local.value.setLocation("山东省")
        local.value.search(loc);

        Notification.info({
          title: '查询成功',
        })
      }
      catch (error){
        Notification.error({
            title: '添加失败',
            content: error.message
        })
        return;
      }
    }
    // 创建 Autocomplete 实例


    addResult = () => {
      try {

        selectedPlaces.value.push(searchResult.value.find(item => item.title === selectElement.value))
        if (!selectedPlaces.value) {
          Notification.error({
            title: '添加失败',
            content: "未选择任何地点"
        })
        }
        console.log(selectedPlaces.value) ;
        Notification.info({
            title: '添加成功',
        })

      } catch (error) {
        Notification.error({
            title: '添加失败',
            content: error.message
        })
        return;
      }
    }

    removeResult = (item) => {
      selectedPlaces.value = selectedPlaces.value.filter(place => place.title !== item.title);
    }

    setPlace = () => {
      map.value.clearOverlays(); // 清除地图上所有覆盖物
      const driving1 = new BMapGL.DrivingRouteLine('山东省', { 
        renderOptions: { 
            map: map.value, 
            autoViewport: true,
        }
      });
      const driving2 = new BMapGL.DrivingRoute('山东省', { 
        renderOptions: { 
            map: map.value, 
            autoViewport: true,
        }
      })
      wayPointsArray.value = selectedPlaces.value.map((place) => place.point);
      const startPoint = wayPointsArray.value[0];
      const endPoint = wayPointsArray.value[wayPointsArray.value.length - 1];
      if (wayPointsArray.value.length < 2) {
        Notification.error({
          title: '添加失败',
          content: "地点数量不足"
        })
        return;
      }
      else if (wayPointsArray.value.length > 2){
        let middleWayPointsArray = wayPointsArray.value.slice(1, wayPointsArray.value.length - 1); // 排除第一个和最后一个元素
        //wayPointsStr.value  = `'${wayPointsArray.value.map(point => `${point.lat},${point.lng}`).join('|')}'`;
        //注：这段str格式转换自一开始就有问题，最后使用数组形式传入
        try {
          driving1.search(startPoint, endPoint, {
            waypoints: middleWayPointsArray
          });
        } catch (error) {
          console.error("Error during driving1.search:", error);
        }
      }
      else{
        driving2.search(startPoint, endPoint);
      }
      console.log(selectedPlaces.value)
    }

    savePlace = (event) => {
      event.preventDefault();
      console.log(selectedPlaces.value)
      if(ISLOGOIN.value){
          axios.post('http://localhost:5000/savePlace', {
          roadInfo: addInfoInput.value,
          acount: loginForm.acount,
          place: selectedPlaces.value
          })
          .then(function(response){
            console.log(response.data)
            if(response.data == 'Success'){
              Notification.info({
                title: '添加成功',
                content: '已成功添加地点'
              })
            }
            else{
              Notification.error({
                title: '添加失败',
              })
            }
          })
      }
      else{
        Notification.error({
          title: '添加失败',
          content: '请登陆后重试'
        });
      }
    }
    
    addDist = () => {
      console.log(isDist.value)
        if(mapDistrict.value){
          if(isDist.value){
            if(!map.value){
              Notification.error({
              title: '添加失败',
              })
              return;
            }
            map.value.addDistrictLayer(mapDistrict.value)
            //map.value.addOverlay(mapBorder.value)
            console.log(mapDistrict.value)
          }
          else{
            map.value.removeDistrictLayer(mapDistrict.value)
            //map.value.removeOverlay(mapBorder.value)
          }
        }
    }
  });

</script>