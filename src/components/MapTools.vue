<template>
    <div :style="{ display: 'flex',flexDirection: 'column',gap: '1rem' }">
        <a-tooltip content="旅行足迹" position="right">
            <a-switch id="switch"></a-switch>
        </a-tooltip>

        <div class="toolbox">
            <a-popover position="right" trigger="click" default-popup-visible="true">               
                <icon-apps id="toolsIcon"/>
                    <template #content>
                        <a-button @click="handleClick">Open Modal</a-button>
                            <a-modal v-model:visible="visible" @ok="handleOk" @cancel="handleCancel" draggable="true">
                                <template #title>
                                    Title
                                </template>
                                <div id="r-result"></div>
                            </a-modal>
                        <a-button>步行路线规划</a-button>
                        <a-button>公交、地铁路线规划</a-button>
                    </template>
            </a-popover>
        </div>

        

  </div>
 

</template>

<style scoped>
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
    #r-result,#r-result table{
        width:100%;
        height:100%;
    }
</style>

<script>
import { onMounted } from 'vue';
import bus from '@/utils/eventBus'
import EVENTS from '@/utils/EVENTS'
import { ref } from 'vue'
let travelmap =ref('');     //定义一个travelmap来接收传过来的值
export default {
  setup() {
    bus.on(EVENTS.SENDTOBROTHER, (data) => {          //传值
        travelmap = data;});
    
    const visible = ref(false);

    const handleClick = () => {
      visible.value = true;

    };
    const handleOk = () => {
      visible.value = true;

    };
    const handleCancel = () => {
      visible.value = true;
    }

    return {
      visible,
      handleClick,
      handleOk,
      handleCancel
    }
  },
}


</script>

 

