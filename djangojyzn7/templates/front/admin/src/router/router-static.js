import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import news from '@/views/modules/news/list'
    import aboutus from '@/views/modules/aboutus/list'
    import gongcheren from '@/views/modules/gongcheren/list'
    import zulindingdan from '@/views/modules/zulindingdan/list'
    import discusscheliangxinxi from '@/views/modules/discusscheliangxinxi/list'
    import cheliangleixing from '@/views/modules/cheliangleixing/list'
    import yongcheren from '@/views/modules/yongcheren/list'
    import cheliangguihai from '@/views/modules/cheliangguihai/list'
    import chat from '@/views/modules/chat/list'
    import messages from '@/views/modules/messages/list'
    import cheliangcailiao from '@/views/modules/cheliangcailiao/list'
    import cheliangxinxi from '@/views/modules/cheliangxinxi/list'
    import config from '@/views/modules/config/list'


//2.配置路由   注意：名字
const routes = [{
    path: '/index',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '公告资讯',
        component: news
      }
      ,{
	path: '/aboutus',
        name: '关于我们',
        component: aboutus
      }
      ,{
	path: '/gongcheren',
        name: '供车人',
        component: gongcheren
      }
      ,{
	path: '/zulindingdan',
        name: '租赁订单',
        component: zulindingdan
      }
      ,{
	path: '/discusscheliangxinxi',
        name: '车辆信息评论',
        component: discusscheliangxinxi
      }
      ,{
	path: '/cheliangleixing',
        name: '车辆类型',
        component: cheliangleixing
      }
      ,{
	path: '/yongcheren',
        name: '用车人',
        component: yongcheren
      }
      ,{
	path: '/cheliangguihai',
        name: '车辆归还',
        component: cheliangguihai
      }
      ,{
	path: '/chat',
        name: '在线客服',
        component: chat
      }
      ,{
	path: '/messages',
        name: '问题反馈',
        component: messages
      }
      ,{
	path: '/cheliangcailiao',
        name: '车辆材料',
        component: cheliangcailiao
      }
      ,{
	path: '/cheliangxinxi',
        name: '车辆信息',
        component: cheliangxinxi
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: '系统首页',
    redirect: '/index'
  }, /*默认跳转路由*/
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
