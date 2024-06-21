<template>
    <div :style="{ display: 'flex', flexDirection: 'column', gap: '1rem' }">
      <div id="userBox">
        <icon-message  class="userCard" title="个人信息" @click="handleClick" />
            <a-drawer :width="440" :visible="visible" @ok="handleOk" @cancel="handleCancel" unmountOnClose >
                <template #title>
                    论坛
                </template>
                <template #footer>
                    <a-form formItemLayout="{ wrapperCol: { span: 24 }, labelCol: { span: 0 } }">
                        <a-form-item label="帖子标题">
                            <a-input v-model="postTitle" placeholder="请输入帖子标题" />
                        </a-form-item>
                        <a-form-item label="帖子内容">
                            <a-textarea v-model="postContent" placeholder="请输入帖子内容" rows="4" />
                        </a-form-item>
                        <a-form-item>
                            <a-button type="primary" @click="createPost">发布帖子</a-button>
                        </a-form-item>
                    </a-form>
                </template>
                <a-comment author="postTitle" content="">
                    <template #actions>
                        <span class="action" key="heart" @click="onLikeChange">
                            <span v-if="like">
                                <IconHeartFill :style="{ color: '#f53f3f' }" />
                            </span>
                            <span v-else>
                                <IconHeart />
                            </span>
                            {{ 83 + (like ? 1 : 0) }}
                        </span>
                        <span class="action" key="star" @click="onStarChange">
                            <span v-if="star">
                                <IconStarFill style=" color: '#ffb400' " />
                            </span>
                            <span v-else>
                                <IconStar />
                            </span>
                            {{ 3 + (star ? 1 : 0) }}
                        </span>
                        <span class="action" key="reply">
                            <IconMessage /> Reply
                        </span>
                    </template>
                    <template #avatar>
                        <a-avatar>
                            <img alt="avatar" src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp"/>
                        </a-avatar>
                    </template>
                </a-comment>
            </a-drawer>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { Form as AForm, Input as AInput, Textarea as ATextarea, Button as AButton } from '@arco-design/web-vue';
  import {IconHeart,IconMessage,IconStar,IconStarFill,IconHeartFill,} from '@arco-design/web-vue/es/icon';
    export default {
        setup() {
            const visible = ref(false);
            const postTitle = ref('');
            const postContent = ref('');
            const like = ref(false);
            const star = ref(false);

            const handleClick = () => {
                visible.value = true;
            };
            const handleOk = () => {
                visible.value = false;
            };
            const handleCancel = () => {
                visible.value = false;
            };
            const createPost = () => {
                console.log('新建帖子:', postTitle.value, postContent.value);
                postTitle.value = '';
                postContent.value = '';



                
            };

            const onLikeChange = () => {
            like.value = !like.value;
            };
            const onStarChange = () => {
            star.value = !star.value;
            };
            return {
                visible,
                handleClick,
                handleOk,
                handleCancel,
                postTitle,
                postContent,
                createPost,
                like,
                star,
                onLikeChange,
                onStarChange
            };
        }
    }
  </script>
  
  <style scoped>
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
    .action {
        display: inline-block;
        padding: 0 4px;
        color: var(--color-text-1);
        line-height: 24px;
        background: transparent;
        border-radius: 2px;
        cursor: pointer;
        transition: all 0.1s ease;
    }
    .action:hover {
        background: var(--color-fill-3);
    }
  </style>










