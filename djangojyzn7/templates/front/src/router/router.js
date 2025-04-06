import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Messages from '../pages/messages/list'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import yongcherenList from '../pages/yongcheren/list'
import yongcherenDetail from '../pages/yongcheren/detail'
import yongcherenAdd from '../pages/yongcheren/add'
import gongcherenList from '../pages/gongcheren/list'
import gongcherenDetail from '../pages/gongcheren/detail'
import gongcherenAdd from '../pages/gongcheren/add'
import cheliangleixingList from '../pages/cheliangleixing/list'
import cheliangleixingDetail from '../pages/cheliangleixing/detail'
import cheliangleixingAdd from '../pages/cheliangleixing/add'
import cheliangcailiaoList from '../pages/cheliangcailiao/list'
import cheliangcailiaoDetail from '../pages/cheliangcailiao/detail'
import cheliangcailiaoAdd from '../pages/cheliangcailiao/add'
import cheliangxinxiList from '../pages/cheliangxinxi/list'
import cheliangxinxiDetail from '../pages/cheliangxinxi/detail'
import cheliangxinxiAdd from '../pages/cheliangxinxi/add'
import zulindingdanList from '../pages/zulindingdan/list'
import zulindingdanDetail from '../pages/zulindingdan/detail'
import zulindingdanAdd from '../pages/zulindingdan/add'
import cheliangguihaiList from '../pages/cheliangguihai/list'
import cheliangguihaiDetail from '../pages/cheliangguihai/detail'
import cheliangguihaiAdd from '../pages/cheliangguihai/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'messages',
					component: Messages
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yongcheren',
					component: yongcherenList
				},
				{
					path: 'yongcherenDetail',
					component: yongcherenDetail
				},
				{
					path: 'yongcherenAdd',
					component: yongcherenAdd
				},
				{
					path: 'gongcheren',
					component: gongcherenList
				},
				{
					path: 'gongcherenDetail',
					component: gongcherenDetail
				},
				{
					path: 'gongcherenAdd',
					component: gongcherenAdd
				},
				{
					path: 'cheliangleixing',
					component: cheliangleixingList
				},
				{
					path: 'cheliangleixingDetail',
					component: cheliangleixingDetail
				},
				{
					path: 'cheliangleixingAdd',
					component: cheliangleixingAdd
				},
				{
					path: 'cheliangcailiao',
					component: cheliangcailiaoList
				},
				{
					path: 'cheliangcailiaoDetail',
					component: cheliangcailiaoDetail
				},
				{
					path: 'cheliangcailiaoAdd',
					component: cheliangcailiaoAdd
				},
				{
					path: 'cheliangxinxi',
					component: cheliangxinxiList
				},
				{
					path: 'cheliangxinxiDetail',
					component: cheliangxinxiDetail
				},
				{
					path: 'cheliangxinxiAdd',
					component: cheliangxinxiAdd
				},
				{
					path: 'zulindingdan',
					component: zulindingdanList
				},
				{
					path: 'zulindingdanDetail',
					component: zulindingdanDetail
				},
				{
					path: 'zulindingdanAdd',
					component: zulindingdanAdd
				},
				{
					path: 'cheliangguihai',
					component: cheliangguihaiList
				},
				{
					path: 'cheliangguihaiDetail',
					component: cheliangguihaiDetail
				},
				{
					path: 'cheliangguihaiAdd',
					component: cheliangguihaiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
