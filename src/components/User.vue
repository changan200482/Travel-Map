<template>
    <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
      <div id="userBox">
        <icon-menu-fold @click="selfInfoClick" v-if="ISLOGOIN" class="userCard"/>
        <icon-user v-else @click="loginClick" class="userCard" title="个人信息"/>   
        <!--登陆界面对话框-->
          <a-modal v-model:visible="loginVisible" 
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
          title="添加路线">
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

        <a-tooltip content="旅行足迹" position="right" >
            <a-switch id="switch" type="line" v-model="isDist" @change="addDist"/>
        </a-tooltip>
    </div>
</template>

<style scoped>
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
  import { reactive,onMounted, onUnmounted, ref, } from 'vue';                 //引入reactive和ref
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

  const isDist=ref(false)
  let map = ref(null);
  let dist = ref(null)

  const initMapListeners = () => {
    if (map.value) {
      function addDist(isDist){
        if(isDist){
          map.value.addDistrictLayer(dist)
        }
        else{
          map.value.removeDistrictLayer(dist)
        }
      }
    }
    else {
      console.warn("Map instance not ready yet.");
    }
  }

  const receiveMapInstance = (data) => {
      map.value = data;
  };

  const receiveDistInstance = (data) =>{
      dist.value =data;
  }
  const removeMapListeners = () => {
    if (map.value) {
      map.value.removeEventListener("click", initMapListeners); // 修正：移除正确的监听器
    }
  };

  onMounted(() => {
    bus.on(EVENTS.SENDTOBROTHER, receiveMapInstance);
    bus.on(EVENTS.SEND_DIST, receiveDistInstance);
  });

  onUnmounted(() => {
    bus.off(EVENTS.SENDTOBROTHER, receiveMapInstance);
    bus.off(EVENTS.SEND_DIST, receiveDistInstance);
    removeMapListeners();
  });

</script>