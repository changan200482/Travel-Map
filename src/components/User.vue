<template>
    <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
      <div id="userBox">
          <icon-user @click="loginClick" class="userCard" title="个人信息"/>   
          <!--登陆界面对话框-->
            <a-modal v-model:visible="loginVisible" title="账号登入" @cancel="loginCancel" @before-ok="loginBeforeOk" width="520px" >
                <a-form :model="loginForm">
                    <a-form-item field="acount">
                      <a-input 
                      v-model="loginForm.acount"
                      placeholder="请输入邮箱" allow-clear />
                    </a-form-item>

                    <a-form-item field="password">
                      <a-input-password
                      v-model="loginForm.password"
                      placeholder="密码"
                      allow-clear
                      />
                    </a-form-item>

                    <a-button type="primary" @click="login">登录</a-button> 
                </a-form>
                <a-link @click="newAcount">注册新用户</a-link>               
            </a-modal>
            <!--注册界面对话框-->
            <a-modal v-model:visible="registerVisible" title="注册" @cancel="registerCancel" @before-ok="registerBeforeOk" width="550px">
                    <a-form :model="registerForm">
                        <a-form-item field="acount">
                            <a-input 
                            v-model="registerForm.name"
                            placeholder="请输入您的用户名"/>
                        </a-form-item>
                        <a-form-item field="acount">
                            <a-input 
                            v-model="registerForm.acount"
                            placeholder="请输入您的邮箱"/>
                        </a-form-item>
                        <a-form-item field="password">
                            <a-input-password
                            v-model="registerForm.password" 
                            placeholder="请输入您的密码"/>
                        </a-form-item>
                        <a-form-item field="confirmPassword">
                            <a-input-password
                            v-model="registerForm.confirmPassword"
                            placeholder="请确认您的密码"
                            />
                        </a-form-item>
                        <a-button type="primary" @click="register">注册</a-button>
                    </a-form>
            </a-modal>                                              


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
  import { Notification } from '@arco-design/web-vue';  //引入通知组件
  import axios from 'axios'                             //引入axios
  import { reactive, ref, } from 'vue';                 //引入reactive和ref

  const loginVisible = ref(false);

  const loginClick = () => {
    loginVisible.value = true;
  };                                                    //点击函数visible.value = true;来让绑定visible的对话框显示

  const loginBeforeOk = (done) => {
    console.log(loginForm)
    window.setTimeout(() => {
      done()
      // prevent close
      // done(false)
    }, 3000)
  };                                                    //点击对话框的“确认”后可以执行一些判定，来决定对话框是否关闭，或者进行其他操作

  const loginCancel = () => {                           //点击对话框“取消”后运行的操作
    loginVisible.value = false;
  };                                                    //点击函数visible.value = false;来让绑定visible的对话框隐藏
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
  };                                                           //登录函数，通过axios.post()来向后端发送请求，根据后端返回的数据来判断登录是否成功

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

  const registerBeforeOk = (done) => {
    console.log(registerForm)
    window.setTimeout(() => {
      done()
        //prevent close
        //done(false)
    }, 3000)
  };    

  const registerCancel = () => {
    registerVisible.value = false;
  }

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


  const lianjie1 = () => {
    window.open("C:\Users\王\Desktop\网页\HTML\w.html");
  }

</script>