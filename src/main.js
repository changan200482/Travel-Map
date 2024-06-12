import './assets/main.css'                    // 引入全局样式

import { createApp } from 'vue'               // 引入 Vue
import { createPinia } from 'pinia'           // 引入 Pinia
import ArcoVue from '@arco-design/web-vue';   // 引入 ArcoVue

import App from './App.vue'                   // 引入 App 组件
import router from './router'                 // 引入路由
import '@arco-design/web-vue/dist/arco.css';  // 引入arco样式

const app = createApp(App)                    // 创建 Vue 实例

app.use(createPinia())                        // 注册 Pinia 
app.use(router)                               // 注册路由
app.use(ArcoVue);                             // 注册 ArcoVue


app.mount('#app')                             // 挂载到 #app 节点
