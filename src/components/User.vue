<template>
    <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
      <div id="userBox">
          <icon-user @click="handleClick" class="userCard" title="个人信息"/>   
          <!--登陆界面对话框-->
            <a-modal v-model:visible="loginVisible" title="账号登入" @cancel="handleCancel" @before-ok="handleBeforeOk" width="520px" >
                <a-form :model="loginForm">
                    <a-form-item field="acount">
                      <a-input :style="{width:'320px'}" 
                      v-model="loginForm.acount"
                      placeholder="请输入邮箱" allow-clear />
                    </a-form-item>

                    <a-form-item field="password">
                      <a-input-password
                      v-model="loginForm.password"
                      placeholder="密码"
                      :style="{width:'320px'}"
                      :defaultVisibility="false"
                      allow-clear
                      />
                    </a-form-item>

                    <a-button type="primary" @click="login">登录</a-button> 
                </a-form>
                <a-link @click="zhuce">注册新用户</a-link>               
            </a-modal>
            <!--注册界面对话框-->
            <a-modal v-model:visible="visible1" title="注册" @cancel="handleCancel1" @before-ok="handleBeforeOk1" width="550px">
                    <a-form :model="form1">
                        <a-form-item field="name" label="请输入您的邮箱">
                            <a-input v-model="form1.name" ></a-input>
                        </a-form-item>
                        <a-form-item field="post" label="请输入您的密码">
                            <a-input v-model="form1.post" ></a-input>
                        </a-form-item>
                        <a-form-item field="post1" label="请再次确认您的密码">
                            <a-input v-model="form1.post1" ></a-input>
                        </a-form-item>
                        <a-button type="primary" @click="zhuce1">注册 </a-button>
                    </a-form>
            </a-modal>                                              

            <!--注册结果对话框-->
            <a-modal v-model:visible="visible2" title="注册" @cancel="handleCancel2" @before-ok="handleBeforeOk2" >
                    <a-form :model="form1">
                        <a-result status="success" title="注册结果：" >
                            <template #subtitle>
                              注册成功！
                            </template>
                        </a-result>
                    </a-form>
            </a-modal>                                            
            <!-- 因为界面中只能同时存在一个对话框，所以利用visible="visible--x"来选择呈现出哪一个对话框-->


            <hr>
            <a-popover position="left">
               <icon-more class="userCard"/>
               <template #content>
                <h4>开发者信息</h4>
                <a-space>
                  <a-link href="C:\Users\王\Desktop\网页\HTML\w.html" >Mr.W</a-link>
                </a-space>
              </template>
            </a-popover>
          
        </div>
        <div class="functionalModule">
          <a-tooltip content="添加留言" position="left">
                <icon-plus class="iconBox" title="添加留言"/>
            </a-tooltip>
        </div>
        <div class="functionalModule">
            <a-tooltip content="历史记录" position="left">
                <icon-clock-circle class="iconBox" title="历史记录"/>
            </a-tooltip>
        </div>

    </div>
</template>

<style scoped>
    hr{
        width: 2rem;
        margin: auto;
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
  import { Notification } from '@arco-design/web-vue'; //引入通知组件
  import axios from 'axios'                            //引入axios
  import { reactive, ref, } from 'vue';                //引入reactive和ref

  const loginVisible = ref(false);

  const handleClick = () => {
    loginVisible.value = true;
  };                                      //点击函数visible.value = true;来让绑定visible的对话框显示

  const handleBeforeOk = (done) => {
    console.log(loginForm)
    window.setTimeout(() => {
      done()
      // prevent close
      // done(false)
    }, 3000)
  };                                       //点击对话框的“确认”后可以执行一些判定，来决定对话框是否关闭，或者进行其他操作

  const handleCancel = () => {             //点击对话框“取消”后运行的操作
    loginVisible.value = false;
  };                                       //点击函数visible.value = false;来让绑定visible的对话框隐藏
  const loginForm = reactive({
    acount: '',
    password: ''
  });                                      

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
        }
      })
      .catch(function(error){
        console.log(error)
      })
    }
    
  };                                      //登录函数，通过axios.post()来向后端发送请求，根据后端返回的数据来判断登录是否成功


  const visible1= ref(false);
  const visible2= ref(false);


  const form1 = reactive({
    name: '',
    post: '',
    post1: ''
  });     

  const zhuce = () => {
    visible1.value = true;
    visible.value = false;
  };

  const handleBeforeOk1 = (done) => {
    console.log(form1)
    window.setTimeout(() => {
      done()
        //prevent close
        //done(false)
    }, 3000)
  };    

  const handleCancel1 = () => {
    visible1.value = false;
    visible.value = true;
  }

  const zhuce1 = () => {
    visible2.value = true;
    visible1.value = false;
  };

  const handleBeforeOk2 = (done) => {
    console.log(form1)
    window.setTimeout(() => {
      done()
        //prevent close
        //done(false)
    }, 3000)
  };    

  const handleCancel2 = () => {
      
    visible2.value = false;
    visible1.value = false;
    visible.value = true;
  }

  

  const lianjie1 = () => {
    window.open("C:\Users\王\Desktop\网页\HTML\w.html");
  }

</script>