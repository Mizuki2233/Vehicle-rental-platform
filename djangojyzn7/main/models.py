#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yongcheren(BaseModel):
    __doc__ = u'''yongcheren'''
    __tablename__ = 'yongcheren'

    __loginUser__='yonghuming'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuming'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuming=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    shenfenzheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='身份证' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    shenfenzhengzhao=models.TextField   ( null=False, unique=False, verbose_name='身份证照' )
    jiazhao=models.TextField   ( null=False, unique=False, verbose_name='驾照' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    yonghuming=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    touxiang=Text
    nianling=Integer
    shenfenzheng=VARCHAR
    shouji=VARCHAR
    youxiang=VARCHAR
    shenfenzhengzhao=Text
    jiazhao=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'yongcheren'
        verbose_name = verbose_name_plural = '用车人'
class gongcheren(BaseModel):
    __doc__ = u'''gongcheren'''
    __tablename__ = 'gongcheren'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    shenfenzheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='身份证' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    dianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    shenfenzhengzhao=models.TextField   ( null=False, unique=False, verbose_name='身份证照' )
    jiazhao=models.TextField   ( null=False, unique=False, verbose_name='驾照' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    zhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    touxiang=Text
    nianling=Integer
    shenfenzheng=VARCHAR
    youxiang=VARCHAR
    dianhua=VARCHAR
    shenfenzhengzhao=Text
    jiazhao=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'gongcheren'
        verbose_name = verbose_name_plural = '供车人'
class cheliangleixing(BaseModel):
    __doc__ = u'''cheliangleixing'''
    __tablename__ = 'cheliangleixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheliangleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='车辆类型' )
    '''
    cheliangleixing=VARCHAR
    '''
    class Meta:
        db_table = 'cheliangleixing'
        verbose_name = verbose_name_plural = '车辆类型'
class cheliangcailiao(BaseModel):
    __doc__ = u'''cheliangcailiao'''
    __tablename__ = 'cheliangcailiao'



    __authTables__={'zhanghao':'gongcheren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheliangmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='车辆名称' )
    cheliangleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='车辆类型' )
    cheliangpinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆品牌' )
    cheliangxinghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆型号' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    chepaihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车牌号' )
    lichengshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='里程数' )
    zuidazairenliang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='最大载人量' )
    yunhuoliang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='运货量' )
    meirizujin=models.FloatField   ( null=False, unique=False, verbose_name='每日租金' )
    cailiaowenjian=models.TextField   ( null=False, unique=False, verbose_name='材料文件' )
    xiangxijieshao=models.TextField   (  null=True, unique=False, verbose_name='详细介绍' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    dianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    cheliangmingcheng=VARCHAR
    cheliangleixing=VARCHAR
    cheliangpinpai=VARCHAR
    cheliangxinghao=VARCHAR
    tupian=Text
    chepaihao=VARCHAR
    lichengshu=VARCHAR
    zuidazairenliang=VARCHAR
    yunhuoliang=VARCHAR
    meirizujin=Float
    cailiaowenjian=Text
    xiangxijieshao=Text
    zhanghao=VARCHAR
    xingming=VARCHAR
    dianhua=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'cheliangcailiao'
        verbose_name = verbose_name_plural = '车辆材料'
class cheliangxinxi(BaseModel):
    __doc__ = u'''cheliangxinxi'''
    __tablename__ = 'cheliangxinxi'



    __authTables__={'zhanghao':'gongcheren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheliangmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆名称' )
    cheliangleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆类型' )
    cheliangpinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆品牌' )
    cheliangxinghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆型号' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    chepaihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车牌号' )
    lichengshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='里程数(万公里)' )
    zuidazairenliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='最大载人量（人）' )
    yunhuoliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='运货量（吨）' )
    chufadi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='出发地(精确到市)' )
    meirizujin=models.FloatField   (  null=True, unique=False, verbose_name='每日租金（元）' )
    xiangxijieshao=models.TextField   (  null=True, unique=False, verbose_name='详细介绍' )
    zhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    dianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    '''
    cheliangmingcheng=VARCHAR
    cheliangleixing=VARCHAR
    cheliangpinpai=VARCHAR
    cheliangxinghao=VARCHAR
    tupian=Text
    chepaihao=VARCHAR
    lichengshu=VARCHAR
    zuidazairenliang=VARCHAR
    yunhuoliang=VARCHAR
    chufadi=VARCHAR
    meirizujin=Float
    xiangxijieshao=Text
    zhuangtai=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    dianhua=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    '''
    class Meta:
        db_table = 'cheliangxinxi'
        verbose_name = verbose_name_plural = '车辆信息'
class zulindingdan(BaseModel):
    __doc__ = u'''zulindingdan'''
    __tablename__ = 'zulindingdan'



    __authTables__={'zhanghao':'gongcheren','yonghuming':'yongcheren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    cheliangmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆名称' )
    cheliangleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆类型' )
    chufadi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='出发地' )
    chepaihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车牌号' )
    zairenshu=models.CharField ( max_length=255,null=False, unique=False, verbose_name='载人数' )
    mudedi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='目的地' )
    yunhuoliang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='运货量' )
    meirizujin=models.FloatField   (  null=True, unique=False, verbose_name='每日租金' )
    shiyongtianshu=models.IntegerField  ( null=False, unique=False, verbose_name='使用天数' )
    zongjiage=models.FloatField   (  null=True, unique=False, verbose_name='总价格' )
    shiyongshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='使用时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    yonghuming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shenfenzheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身份证' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    dingdanbianhao=VARCHAR
    cheliangmingcheng=VARCHAR
    cheliangleixing=VARCHAR
    chufadi=VARCHAR
    chepaihao=VARCHAR
    zairenshu=VARCHAR
    mudedi=VARCHAR
    yunhuoliang=VARCHAR
    meirizujin=Float
    shiyongtianshu=Integer
    zongjiage=Float
    shiyongshijian=DateTime
    zhanghao=VARCHAR
    yonghuming=VARCHAR
    xingming=VARCHAR
    shenfenzheng=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'zulindingdan'
        verbose_name = verbose_name_plural = '租赁订单'
class cheliangguihai(BaseModel):
    __doc__ = u'''cheliangguihai'''
    __tablename__ = 'cheliangguihai'



    __authTables__={'zhanghao':'gongcheren','yonghuming':'yongcheren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='订单编号' )
    cheliangmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆名称' )
    cheliangleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车辆类型' )
    chepaihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车牌号' )
    guihaishuoming=models.TextField   ( null=False, unique=False, verbose_name='归还说明' )
    guihaishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='归还时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    yonghuming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shenfenzheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身份证' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    dingdanbianhao=VARCHAR
    cheliangmingcheng=VARCHAR
    cheliangleixing=VARCHAR
    chepaihao=VARCHAR
    guihaishuoming=Text
    guihaishijian=DateTime
    zhanghao=VARCHAR
    yonghuming=VARCHAR
    xingming=VARCHAR
    shenfenzheng=VARCHAR
    shouji=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'cheliangguihai'
        verbose_name = verbose_name_plural = '车辆归还'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '在线客服'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告资讯'
class aboutus(BaseModel):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'aboutus'
        verbose_name = verbose_name_plural = '关于我们'
class messages(BaseModel):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='留言人id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
    cpicture=models.TextField   (  null=True, unique=False, verbose_name='留言图片' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    rpicture=models.TextField   (  null=True, unique=False, verbose_name='回复图片' )
    '''
    userid=BigInteger
    username=VARCHAR
    avatarurl=Text
    content=Text
    cpicture=Text
    reply=Text
    rpicture=Text
    '''
    class Meta:
        db_table = 'messages'
        verbose_name = verbose_name_plural = '问题反馈'
class discusscheliangxinxi(BaseModel):
    __doc__ = u'''discusscheliangxinxi'''
    __tablename__ = 'discusscheliangxinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusscheliangxinxi'
        verbose_name = verbose_name_plural = '车辆信息评论表'
