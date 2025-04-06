export function isAuth(tableName, key) {
  let role = localStorage.getItem("UserTableName");
  let menus = [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-time","buttons":["新增","查看","修改","删除","审核"],"menu":"用车人","menuJump":"列表","tableName":"yongcheren"}],"menu":"用车人管理"},{"child":[{"appFrontIcon":"cuIcon-circle","buttons":["新增","查看","修改","删除","审核"],"menu":"供车人","menuJump":"列表","tableName":"gongcheren"}],"menu":"供车人管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["新增","查看","修改","删除"],"menu":"车辆类型","menuJump":"列表","tableName":"cheliangleixing"}],"menu":"车辆类型管理"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["查看","删除","审核","添加汽车","修改","添加车辆"],"menu":"车辆材料","menuJump":"列表","tableName":"cheliangcailiao"}],"menu":"车辆材料管理"},{"child":[{"appFrontIcon":"cuIcon-paint","buttons":["查看","修改","查看评论","删除","审核"],"menu":"车辆信息","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息管理"},{"child":[{"appFrontIcon":"cuIcon-goodsnew","buttons":["查看","修改","删除"],"menu":"租赁订单","menuJump":"列表","tableName":"zulindingdan"}],"menu":"租赁订单管理"},{"child":[{"appFrontIcon":"cuIcon-full","buttons":["查看","修改","删除"],"menu":"车辆归还","menuJump":"列表","tableName":"cheliangguihai"}],"menu":"车辆归还管理"},{"child":[{"appFrontIcon":"cuIcon-message","buttons":["查看","回复","删除"],"menu":"问题反馈","tableName":"messages"}],"menu":"问题反馈"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"公告资讯","tableName":"news"},{"appFrontIcon":"cuIcon-service","buttons":["新增","查看","修改","删除"],"menu":"在线客服","tableName":"chat"},{"appFrontIcon":"cuIcon-camera","buttons":["查看","修改"],"menu":"关于我们","tableName":"aboutus"},{"appFrontIcon":"cuIcon-explore","buttons":["查看","修改"],"menu":"轮播图管理","tableName":"config"}],"menu":"系统管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","租赁"],"menu":"车辆信息列表","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-goodsnew","buttons":["查看","支付","归还"],"menu":"租赁订单","menuJump":"列表","tableName":"zulindingdan"}],"menu":"租赁订单管理"},{"child":[{"appFrontIcon":"cuIcon-full","buttons":["查看"],"menu":"车辆归还","menuJump":"列表","tableName":"cheliangguihai"}],"menu":"车辆归还管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","租赁"],"menu":"车辆信息列表","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息模块"}],"hasBackLogin":"否","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"用车人","tableName":"yongcheren"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"车辆材料","menuJump":"列表","tableName":"cheliangcailiao"}],"menu":"车辆材料管理"},{"child":[{"appFrontIcon":"cuIcon-paint","buttons":["查看","修改","查看评论"],"menu":"车辆信息","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息管理"},{"child":[{"appFrontIcon":"cuIcon-goodsnew","buttons":["查看","审核"],"menu":"租赁订单","menuJump":"列表","tableName":"zulindingdan"}],"menu":"租赁订单管理"},{"child":[{"appFrontIcon":"cuIcon-full","buttons":["查看","审核"],"menu":"车辆归还","menuJump":"列表","tableName":"cheliangguihai"}],"menu":"车辆归还管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","租赁"],"menu":"车辆信息列表","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息模块"}],"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"供车人","tableName":"gongcheren"}];
  for(let i=0;i<menus.length;i++){
    if(menus[i].tableName==role){
      for(let j=0;j<menus[i].frontMenu.length;j++){
          for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
            if(tableName==menus[i].frontMenu[j].child[k].tableName){
              let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
              return buttons.indexOf(key) !== -1 || false
            }
          }
      }
    }
  }
  return false;
}

/**
 *  * 获取当前时间（yyyy-MM-dd hh:mm:ss）
 *   */
export function getCurDateTime() {
    let currentTime = new Date(),
    year = currentTime.getFullYear(),
    month = currentTime.getMonth() + 1 < 10 ? '0' + (currentTime.getMonth() + 1) : currentTime.getMonth() + 1,
    day = currentTime.getDate() < 10 ? '0' + currentTime.getDate() : currentTime.getDate(),
    hour = currentTime.getHours(),
    minute = currentTime.getMinutes(),
    second = currentTime.getSeconds();
    return year + "-" + month + "-" + day + " " +hour +":" +minute+":"+second;
}

/**
 *  * 获取当前日期（yyyy-MM-dd）
 *   */
export function getCurDate() {
    let currentTime = new Date(),
    year = currentTime.getFullYear(),
    month = currentTime.getMonth() + 1 < 10 ? '0' + (currentTime.getMonth() + 1) : currentTime.getMonth() + 1,
    day = currentTime.getDate() < 10 ? '0' + currentTime.getDate() : currentTime.getDate();
    return year + "-" + month + "-" + day;
}
