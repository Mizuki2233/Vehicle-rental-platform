
# 摘  要
本文介绍了一个基于H5技术开发的共享用车平台。本平台采用前后端分离的开发模式，后端使用Django框架，前端使用Vue和Element-UI技术开发。数据库管理采用MySQL，并借助Navicat进行辅助操作。项目通过Django中的Models（数据存储层）与MySQL数据库进行交互，并对有些操作数据库的常用方法进行封装，后端数据接口通过调用这些方法进行数据库操作，最后利用JsonResponse向前端返回JSON格式的数据，为前端页面提供数据支持。本平台能够运行在各大主流浏览器上，具有高效的运行效率和良好的结构设计。

该平台的主要目标用户是拥有闲置车辆或有用车需求的消费者。用户可以注册用车人账号来满足他们的用车需求，有闲置车辆的用户可以注册供车人账号来出租车辆。平台会为供车人展示和宣传车辆，并匹配合适的用车人。同时，平台会根据用车人的位置和具体需求筛选出合适的车辆，并联系其供车人。双方协商后，通过平台确认订单，实现共享用车。用车结束后，用车人发起归还申请，供车人确认后订单完成。平台还提供了租赁双方互评功能，评价内容对所有用户可见。此外，平台对每位注册用户进行严格审核，以确保交易双方的人身和财产安全。

共享用车平台为用户提供了更加便捷和经济的出行方式，有效解决了传统交通方式带来的用户出行难和车辆利用率低的问题，提高了交通资源的利用效率，同时也促进了经济的发展。

**关键词**：共享用车平台；H5；Django；Vue；Element-UI；Python；MySQL

**Abstract**

This article introduces a shared car platform based on H5 technology development. The platform adopts a front-end and back-end separated development model, using Django framework for the back-end and Vue and Element-UI technology for the front-end. The database management uses MySQL with the help of Navicat for auxiliary operations. The project interacts with MySQL database through Models (data storage layer) in Django and encapsulates some common methods to operate the database, and the back-end data interface operates the database by calling these methods, and finally returns JSON format data to the front-end using JsonResponse to provide data support for the front-end page. The platform can run on major mainstream browsers, with efficient operation efficiency and good structural design.

The main target users of the platform are consumers who own idle vehicles or have a need for a car. Users can sign up for a car user account to meet their car needs, and those with idle vehicles can sign up for a supplier account to rent vehicles. The platform will display and promote the vehicles for the car suppliers and match them with suitable car users. At the same time, the platform will screen out suitable vehicles according to the location and specific needs of the users and contact their car suppliers. After negotiation, both parties will confirm the order through the platform and realize the shared use of the car. After the use of the car, the user initiates a return application and the order is completed after the supplier confirms. The platform also provides the function of mutual evaluation between the two leasing parties, and the evaluation content is visible to all users. In addition, the platform conducts a strict audit of each registered user to ensure the personal and property safety of both parties to the transaction.

The shared-use platform provides users with a more convenient and economical way to travel, effectively solving the problems of difficult travel and low utilization of vehicles by users brought about by traditional transportation methods, improving the efficiency of transportation resources utilization, and also promoting economic development.

**Keywords**: Car sharing platform, H5, Django, Vue, Element-UI, Python, MySQL

# 第1章 序言
## 1.1 研究背景及意义
在当今这个信息技术高速发展的时代，人们的生活节奏不断加快，提高效率成为当务之急。于是对越来越多的城市居民来说，日益增长的用车需求和车辆高昂的购置、维护费用之间产生了矛盾。与此同时，随着互联网渗透入人们生活的方方面面。各行各业都与互联网紧密相连，利用其优势使得数据信息的管理变得方便快捷。

在此背景下，为了满足人们日益增长的出行需求，为广大消费者提供更加便捷、经济的用车选择，本文基于H5技术，开发了一个共享用车平台。该平台可以为供需双方提供信息匹配，通过共享用车的方法，帮助用户出租闲置的车辆，并为有临时用车需求的用户筛选符合其需求的车辆。

平台通过充分利用车辆资源，提高车辆利用率，降低出行成本，为消费者提供更为便捷、经济的出行方式，提高用户的生活质量和幸福水平。
## 1\.2 研究现状
当谈及车辆租赁的研究成果时，国内外都有大量的相关研究。国外有全球范围的汽车租赁管理系统网络，以及赫兹、AVSI等众多知名企业。国内的车辆租赁行业也在1989年以来取得了长足的发展。尤其是近年来，随着汽车市场竞争的加剧，汽车租赁行业异军突起，成为国际市场上发展迅速的领域，被视为未来汽车服务行业的重要方向<sup>[1]</sup>。

越来越多的学者深入研究后发现，限制汽车租赁行业发展的问题日益显现，而网络化汽车租赁被认为是解决当前汽车租赁困境的一个重要方向<sup>[2]</sup>。此外，国内的学者对汽车租赁企业的成本控制进行了分析，并针对目前汽车租赁企业成本管理中常见的问题提出了解决方案，给出了许多有助于汽车租赁企业加强成本管理的方法和建议<sup>[3]</sup>。在国外，也有学者采用报童模型并基于博弈论建立起最优的车辆订购方案，以解决汽车租赁需求难以准确预测、租赁能力过剩或不足等问题<sup>[4]</sup>。

综上所述，无论是国内还是国外，对于车辆租赁的研究成果都非常丰富。学者们也致力于解决汽车租赁行业面临的问题，如网络化汽车租赁、成本管理以及需求预测等，为该行业的发展提供了有益的指导和解决方案。
## 1.3 主要研究内容
本平台采用前后端分离的开发模式，后端使用Django框架，前端使用Vue和Element-UI技术开发。数据库管理采用MySQL，并借助Navicat进行辅助操作。项目通过Django中的Models（数据存储层）与MySQL数据库进行交互，并对有些操作数据库的常用方法进行封装，后端数据接口通过调用这些方法进行数据库操作，最后利用JsonResponse向前端返回JSON格式的数据，为前端页面提供数据支持。本平台能够运行在各大主流浏览器上，具有高效的运行效率和良好的结构设计。

平台主要面向拥有闲置车辆或有临时用车需求的消费人群。平台用户分成三种身份，用车人，供车人、运营管理人员，三种身份将分别注册和登录对应的类型的账号。

如果用户希望将闲置的车辆出租，可注册供车人账号，填写并提交希望出租的车辆基本信息。平台会为其展示、宣传并匹配合适的用车人。有用车需求的用户可以注册用车人账号，希望利用闲置车辆的用户可注册用车人账号。

对于供车用户，平台会为其展示、宣传闲置车辆，并匹配合适的用车人。对于用车用户，平台会根据其所在地和具体需求为其筛选和展示合适的车辆。待用车人选定心仪车辆后，系统联系供车人，双方进行沟通。协商完成后，即可通过平台确认订单，达到共享用车的目的。在用车完成后，用车人发起归还申请，供车人确认归还后订单完成。平台还提供了租赁双方互评功能，评价内容可供所有用户查看。此外，平台会对每位注册用户进行严格审核，确保交易双方的人身及财产安全。

# 第2章 相关技术介绍
## 2.1 所用技术
### 2\.1.1 Vue.js技术
Vue.js是一种现代化的JavaScript前端框架，以其简单易学易用的特性吸引了大量开发者，在众多前端技术中脱颖而出，被广泛用于构建交互式的Web应用程序<sup>[5]</sup>。

Vue的主要特点之一是其响应式数据绑定系统。随着用户对产品体验和可用性要求的提升，使用前端框架成为开发的趋势。在这一背景下，Vue作为一种流行的JavaScript框架，帮助开发者处理常见的前端问题，如操作DOM和渲染数据<sup>[6]</sup>。通过Vue，开发人员可以将数据和DOM元素之间建立起动态的绑定关系。这意味着当数据发生变化时，相关的DOM元素会自动更新，使得开发人员无需手动处理DOM操作，从而提高开发效率。

另一个重要的特性是Vue的组件化开发模式。Vue允许开发人员将应用程序拆分为多个可重用的组件，每个组件都有自己的模板、样式和逻辑。这种组件化的开发方式使得代码结构清晰、易于维护，并且可以提高代码的可复用性。Vue的组件系统还支持单文件组件（SFC），允许开发人员在一个文件中编写组件的模板、样式和逻辑，提供了更好的开发体验和可读性。

总之，Vue.js是一个功能强大、灵活且易于上手的前端框架，适用于构建各种规模的Web应用程序。值得初学者和专业开发人员学习和使用。
### 2.1.2 Element-UI技术
Element-UI是一套基于Vue.js的开源UI组件库，专注于构建企业级Web应用程序的用户页面。它提供了一系列易于使用、美观且功能强大的组件，帮助开发人员快速搭建专业水平的页面。

Element-UI的特点之一是其丰富多样的组件库。它包含了诸如按钮、表单、表格、对话框、导航菜单、弹出框等常用的UI组件，覆盖了大部分企业级应用程序开发中所需的功能。这些组件具有一致的设计风格，易于使用和定制，可以满足不同项目的需求。它还提供了高级组件和特性，如数据可视化、表单验证和国际化。Element-UI具有详细的文档和示例代码，帮助开发人员快速上手。

由于其易用性和丰富的功能，Element-UI在Vue.js社区中非常受欢迎。它拥有庞大的用户群体和活跃的开发社区，可以获取到许多开发人员共享的插件、主题和解决方案。这使得开发人员能够更快速地构建出优秀的企业级Web应用程序，并与其他开发者分享他们的经验和资源。

总之，Element-UI是一个功能强大、易于使用的Vue.js的UI组件库，适用于构建企业级Web应用程序。
### 2\.1.3 Django框架
Django是用Python开发的开放源码的Web框架,遵循MVC设计理念, 并提供了许多工具和功能，使开发人员能够专注于业务逻辑而不必担心底层的复杂性。使用Django框架,可以在短时间内创建出高品质,易维护和数据库驱动的Web应用程序<sup>[7]</sup>。

Django的主要特点之一是其强大的ORM（对象关系映射）功能。ORM使开发人员能够通过Python对象与数据库进行交互，而无需直接编写SQL查询语句。这简化了数据库操作的过程，并提供了对多种数据库后端的支持。另一个重要特性是Django的自动化管理页面，开发人员可以通过简单的配置就能实现对数据的增删改查操作。Django提供了一套灵活的URL路由系统。开发人员可以通过定义URL模式将请求映射到相应的处理函数，这使得URL的管理和路由变得简单而直观。Django还拥有活跃的社区和完善的文档资源。

总之，Django是一个功能强大、易于使用的Python Web框架，适用于构建各种规模的Web应用程序，使用Django可以降低Web应用开发的复杂性,提高开发效率<sup>[8]</sup>。
### 2\.1.4 MySQL数据库
MySQL是一种流行的开源关系型数据库管理系统，具有功能齐全、操作简单、管理效率高、运行速度快等特点，因此被广泛应用于Web应用程序和企业级系统中<sup>[9]</sup>。

MySQL具有良好的性能和可伸缩性。它可以处理大量的数据和高并发访问，并且能够根据需求进行水平和垂直扩展。MySQL采用了先进的查询优化和索引技术，能够快速执行复杂的查询操作，并通过适当的配置和调优提供卓越的性能。MySQL提供了丰富的功能和灵活的存储引擎选择。MySQL具有广泛的平台兼容性。它可以在多个操作系统上运行，包括Windows、Linux、Mac等。无论是在开发、测试还是生产环境中，MySQL都能提供可靠和稳定的数据库解决方案。

此外，MySQL还具有强大的事务支持和数据完整性。它遵循ACID（原子性、一致性、隔离性和持久性）原则，可以确保数据的安全性和一致性<sup>[10]</sup>。如果数据在不小心的情况下被删除，MySQL提供了回滚日志（undo log）和回收站（recycle bin）的功能。当数据库发生崩溃或意外关闭时，MySQL具备自动恢复机制。通过重放日志文件（redo log），可以将未持久化到磁盘的更改重新应用，恢复数据库到崩溃前的状态。

总而言之，MySQL是一种功能强大、高性能、可伸缩和可靠的关系型数据库管理系统。它提供了丰富的功能和灵活的存储引擎选择，具有强大的事务支持和数据完整性。
## 2.2 核心功能技术路线
### 2\.2.1 首页轮播图
1、功能：

在首页导航栏下方放置一个车辆轮播图。

2、技术路线：

前端前台：在系统前端的首页代码中，添加一个轮播图容器，用于展示轮播图片。使用Element-UI提供的轮播图组件，选择合适轮播图样式和功能。在轮播图组件中设置相应的样式和动画效果。

前端后台：在管理员页面创建一个轮播图管理页面，在管理员页面中提供上传图片的功能，允许管理员选择图片并上传到后端服务器，同时保存图片路径到数据库。提供编辑和删除轮播图的功能，允许管理员对已上传的轮播图进行修改和删除操作。

后端：使用Django框架，创建一个轮播图管理的模型（config），用于存储轮播图相关的信息，包括名称、值（图片文件）。创建一个后端API端点，用于管理员对轮播图进行管理，包括查看和修改轮播图等操作。在后端实现对轮播图的增删改查功能，如：上传图片、保存图片路径到数据库、获取轮播图信息。
### 2\.2.2 用车人查询车辆
1、功能：

用车人在车辆信息页面输入出发地以及所需车辆的信息并点击查询按钮。系统会将车辆位置在用车人出发地，符合用车人需求的车辆筛选出来。

2、技术路线：

数据库：在MySQL数据库中创建一个名为“车辆信息”的表，包含车辆的相关字段，如车辆名称、车型、品牌、载人数、载货量和车辆位置等。确保表中的车辆位置字段与用车人提供的出发地相互匹配。

前端：在前端车辆信息页面中创建一个查询表单，包括出发地和所需车辆的相关信息输入字段。添加一个查询按钮，用于触发查询操作。

后端：在后端使用Django框架，创建一个API端点，接收前端传递的查询参数。使用pymysql模块连接MySQL数据库，并执行相应的查询操作。构建查询语句，根据用车人提供的查询条件，在“车辆信息”数据库表中进行筛选和匹配。查询结果可以使用Django的ORM来获取，并将结果返回给前端。
### 2\.2.3 管理员审核、添加车辆
1、功能：

管理员点击“添加车辆”按钮，将通过审核的车辆信息加入系统的“车辆信息”列表，使该车辆能够被租赁。

2、技术路线：

数据库：创建“车辆材料数据表”，存放待审核的车辆信息，并链接前端“车辆材料”页面；创建“车辆信息数据表”，存放通过审核的车辆信息，并链接前端“车辆信息”页面。这样，只要把前表的数据移入后表即可实现审核功能。

前端：在管理员页面中创建一个车辆材料管理页面，显示待审核的车辆，并在列表每行末尾创建一个“添加车辆”按钮。再创建一个车辆信息管理页面，显示通过审核的车辆。管理员点击“添加车辆”按钮，即可添加对应车辆。

后端：使用Django框架的django.db.connection模块与封装好的数据库操作方法链接、操作数据库。在后端实现管理员点击“添加车辆”按钮后“更新跨表属性”的逻辑函数，读取车辆信息从“车辆材料数据表”中读取并写入“车辆信息数据表”
# 第3章 可行性和需求分析
## 3\.1 平台可行性分析
### 3\.1.1 技术可行性
从技术可行性的角度来看，该平台具备一些优势，具体分析如下：

1、技术栈选择合理：平台采用了Django作为Web框架，Vue和Element-UI作为前端开发工具，这些都是成熟且广泛使用的技术框架和工具，具备良好的稳定性和可扩展性。

2、前后端分离：采用Vue和Element-UI进行前端开发，与后端通过API进行数据交互，实现了前后端分离的架构模式，提高了开发效率、代码可维护性和可扩展性。

3、数据库管理：使用MySQL作为数据库管理系统，这是一种常用的关系型数据库系统，具备稳定性和性能优势。

4、浏览器兼容性：平台能够运行在大多数浏览器上，这意味着用户可以在各种设备和浏览器上访问和使用平台，提供了良好的用户体验和可用性。

总体来说，该共享用车平台在技术可行性方面表现良好。平台采用成熟的技术框架和工具，合理的架构设计以及与主流浏览器的兼容性，能够提供稳定、高效和用户友好的使用体验。
### 3\.1.2 经济可行性
从经济角度来看，该平台具备一定可行性，具体分析如下：

1、市场前景良好：随着生活节奏的不断加快，于是对越来越多的城市居民来说，用车需求日益增长。另一方面，随着汽车市场竞争的加剧，汽车租赁行业异军突起，成为市场上发展迅速的领域，被视为未来汽车服务行业的重要方向。因此，汽车租赁行业是一片蓝海。

2、成本控制：平台的开发和运行均可由笔者独立完成，因此不需要考虑项目的开发、运营成本。在市场推广方面，主要通过在平台主要用户群体常用网站发布软文的方式，易于成本控制。

综合以上因素，可以确定共享用车平台具备一定的可持续盈利的潜力。
### 3\.1.3 社会可行性
该共享用车平台在社会影响方面具备一定优势和可行性，具体如下：

1、资源利用效率：共享用车平台能够提高车辆的利用效率，使得闲置车辆得到更好的利用，提高了整体交通资源的利用效率，减少资源浪费。

2、便捷出行选择：共享用车平台为用户提供了一种便捷的出行选择。用户可以通过平台方便地找到合适的车辆，并进行预订和租赁。这为用户提供了更多出行方式，特别是对于没有私人车辆或需要临时用车的人群来说，提供了便捷的出行解决方案。

3、提供就业岗位：共享用车平台可以促进经济发展。它为供车人提供了额外的收入来源，特别是对于那些拥有闲置车辆的人来说，可以将其车辆进行共享出租。同时，平台的运营也为相关行业提供了就业机会，促进了经济的增长和就业的增加。

综上所述，通过提供便捷、经济的出行选择，该共享用车平台可以为社会带来积极的影响和益处。
### 3\.1.4 结论
综合前面对共享用车平台的技术可行性、经济可行性和社会可行性的分析，可以得出结论：共享用车平台的开发，具有一定可行性。
## 3\.2 平台需求分析
### 3\.2.1 功能需求
共享用车平台应该拥有以下功能：

1、用户注册和登录：实现用车人、供车人的注册和登录以及管理员登录功能。

2、车辆信息的上传和审核：供车人需要向平台上传车辆信息，这些信息的类型包括字符、图片和文件，平台接收存储、这些信息并向管理员展示。平台管理员需对上传的信息进行审核。

3、车辆信息展示和筛选：平台应该能够展示供车人上传的车辆信息，供用车人筛选和选择。用车人可以根据自身情况，在搜索栏中输入出发地以及所需车辆的名称、车型、品牌、载人数、载货量等信息。平台根据这些信息筛选出符合用车人需求的车辆。

4、下单和接单：用车人可以提交订单后，平台会向用车人选择的车辆的供车人发送订单信息。供车人可以接受或拒绝订单，如果接受订单，供车人需要在规定时间内确认订单。

5、订单评价：双方在订单完成后需要进行评价，评价内容将写入用户信息，供平台所有用户查看。
### 3\.2.2 UML用例图
用车人主要实现的功能有：账号注册登录，个人中心管理，查看车辆信息，车辆在线租赁，车辆归还管理，发表评论留言，查看公告信息，问题反馈留言，在线客服留言，我的收藏管理。用车人用例图如图3-1所示。

图3-1 用车人用例图

供车人用户主要实现的功能有：账号注册登录，个人中心管理，车辆材料管理，车辆信息管理，租赁订单管理，车辆归还管理。供车人用户用例图如图3-2所示。

图3-2 供车人用户用例图

管理员主要实现的功能有：个人中心管理，用车人管理，供车人管理，车辆材料管理，车辆类型管理，车辆信息管理，租赁订单管理，车辆归还管理，问题反馈管理，系统信息管理。管理员用例图如图3-3所示。

图3-3 管理员用例图
# 第4章 共享用车平台的设计
## 4.1 整体架构
为完成该系统的功能，系统设计了注册用户和管理员两个主要的操作权限模块。其中，管理员作为系统的管理者在系统中起到了至关重要的作用，需要对整个系统的运行环境进行动态的维护，以保证系统的功能实现和运行的安全性，达到最终满足用户的要求。

系统功能模块设计根据不同类别的用户对应用系统的具体要求来选择相应的模块，每个模块又由若干个子系统构成。共享用车平台的用户身份主要有三类，分别是用车人用户，供车人用户及管理员，他们在系统内可以进行不同功能权限的操作。具体平台功能模块结构如图4-1所示。

图4-1 平台功能模块结构
## 4.2 数据库设计
数据库设计决定了数据库及其应用的整体性能。为了确定数据表内的字段关系以及长度，将E-R与数据表结合形成数据流通体系。以下是共享用车平台数据库的E-R图。

1、用车人信息E-R图，如图4-2所示。

图4-2 用车人信息

2、供车人信息E-R图，如图4-3所示。

图4-3 供车人信息

3、车辆材料E-R图，如图4-4所示。

图4-4 车辆材料

4、车辆信息E-R图，如图4-5所示。

图4-5 车辆信息

5、收藏表E-R图，如图4-6所示。

图4-6 收藏表

6、租赁订单E-R图，图4-7所示。

图4-7 租赁订单
# 第5章 共享用车平台的实现
## 5\.1 数据库实现
共享用车平台数据库创建的数据表如表5-1至表5-15所示。

1、车辆信息评论表：

表5-1 discussqichexinxi

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|refid|bigint||关联表id|||
|userid|bigint||用户id|||
|avatarurl|longtext|4294967295|头像|||
|nickname|varchar|200|用户名|||
|content|longtext|4294967295|评论内容|||
|reply|longtext|4294967295|回复内容|||

2、用车人表：

表5-2 yongcheren

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|yonghuming|varchar|200|用户名|||
|mima|varchar|200|密码|||
|xingming|varchar|200|姓名|||
|xingbie|varchar|200|性别|||
|touxiang|longtext|4294967295|头像|||
|nianling|int||年龄|||
|shenfenzheng|varchar|200|身份证|||
|shouji|varchar|200|手机|||
|youxiang|varchar|200|邮箱|||
|shenfenzhengzhao|longtext|4294967295|身份证照|||
|jiazhao|longtext|4294967295|驾照|||
|sfsh|varchar|200|是否审核||待审核|
|shhf|longtext|4294967295|审核回复|||
3、车辆材料表：

表5-3 cheliangcailiao

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|cheliangmingcheng|varchar|200|车辆名称|||
|cheliangleixing|varchar|200|车辆类型|||
|cheliangpinpai|varchar|200|车辆品牌|||
|cheliangxinghao|varchar|200|车辆型号|||
|tupian|longtext|4294967295|图片|||
|chepaihao|varchar|200|车牌号|||
|lichengshu|varchar|200|里程数|||
|zuidazairenliang|varchar|200|最大载人量|||
|yunhuoliang|varchar|200|运货量|||
|meirizujin|double||每日租金|||
|cailiaowenjian|longtext|4294967295|材料文件|||
|xiangxijieshao|longtext|4294967295|详细介绍|||
|zhanghao|varchar|200|账号|||
|xingming|varchar|200|姓名|||
|dianhua|varchar|200|电话|||
|sfsh|varchar|200|是否审核||待审核|
|shhf|longtext|4294967295|审核回复|||

4、管理员表：

表5-4 users 

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|username|varchar|100|用户名|||
|password|varchar|100|密码|||
|role|varchar|100|角色||管理员|
|addtime|timestamp||新增时间||CURRENT\_TIMESTAMP|

5、在线客服信息表：

表5-5 chat 

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|userid|bigint||用户id|||
|adminid|bigint||管理员id|||
|ask|longtext|4294967295|提问|||
|reply|longtext|4294967295|回复|||
|isreply|int||是否回复|||

6、收藏信息表：

表5-6 storeup 

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|userid|bigint||用户id|||
|refid|bigint||商品id|||
|tablename|varchar|200|表名|||
|name|varchar|200|名称|||
|picture|longtext|4294967295|图片|||
|type|varchar|200|类型||1|
|inteltype|varchar|200|推荐类型|||
|remark|varchar|200|备注|||

7、平台介绍表：

表5-7 aboutus

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|title|varchar|200|标题|||
|subtitle|varchar|200|副标题|||
|content|longtext|4294967295|内容|||
|picture1|longtext|4294967295|图片1|||
|picture2|longtext|4294967295|图片2|||
8、车辆信息表：

表5-8 qichexinxi

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|cheliangmingcheng|varchar|200|车辆名称|||
|cheliangleixing|varchar|200|车辆类型|||
|cheliangpinpai|varchar|200|车辆品牌|||
|cheliangxinghao|varchar|200|车辆型号|||
|tupian|longtext|4294967295|图片|||
|chepaihao|varchar|200|车牌号|||
|lichengshu|varchar|200|里程数(万公里)|||
|zuidazairenliang|varchar|200|最大载人量（人）|||
|yunhuoliang|varchar|200|运货量（吨）|||
|chufadi|varchar|200|出发地(精确到市)|||
|meirizujin|double||每日租金（元）|||
|xiangxijieshao|longtext|4294967295|详细介绍|||
|zhuangtai|varchar|200|状态|||
|zhanghao|varchar|200|供车人账号|||
|xingming|varchar|200|供车人姓名|||
|dianhua|varchar|200|供车人电话|||
|crossuserid|bigint||操作管理员id|||
|crossrefid|bigint||车辆材料表数据id|||

9、车辆类型表：

表5-9 qicheleixing 

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|qicheleixing|varchar|200|车辆类型|||

10、租赁订单表：

表5-10 zulindingdan 

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|dingdanbianhao|varchar|200|订单编号|||
|qichemingcheng|varchar|200|车辆名称|||
|qicheleixing|varchar|200|车辆类型|||
|chufadi|varchar|200|出发地|||
|chepaihao|varchar|200|车牌号|||
|zairenshu|varchar|200|载人数|||
|mudedi|varchar|200|目的地|||
|yunhuoliang|varchar|200|运货量|||
|meirizujin|double||每日租金|||
|shiyongtianshu|int||使用天数|||
|zongjiage|double||总价格|||
|shiyongshijian|datetime||使用时间|||
|zhanghao|varchar|200|账号|||
|yonghuming|varchar|200|用户名|||
|xingming|varchar|200|姓名|||
|shenfenzheng|varchar|200|身份证|||
|shouji|varchar|200|手机|||
|sfsh|varchar|200|是否审核||待审核|
|shhf|longtext|4294967295|审核回复|||

11、车辆归还信息表：

表5-11 qicheguihai 

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|dingdanbianhao|varchar|200|订单编号|||
|qichemingcheng|varchar|200|车辆名称|||
|qicheleixing|varchar|200|车辆类型|||
|chepaihao|varchar|200|车牌号|||
|guihaishuoming|longtext|4294967295|归还说明|||
|guihaishijian|datetime||归还时间|||
|zhanghao|varchar|200|账号|||
|yonghuming|varchar|200|用户名|||
|xingming|varchar|200|姓名|||
|shenfenzheng|varchar|200|身份证|||
|shouji|varchar|200|手机|||
|crossuserid|bigint||归还用户id|||
|crossrefid|bigint||租赁订单表id|||
|sfsh|varchar|200|是否审核||待审核|
|shhf|longtext|4294967295|审核回复|||

12、公告资讯表：

表5-12 news

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|title|varchar|200|标题|||
|introduction|longtext|4294967295|简介|||
|picture|longtext|4294967295|图片|||
|content|longtext|4294967295|内容|||

13、问题反馈表：

表5-13 messages

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|userid|bigint||留言人id|||
|username|varchar|200|用户名|||
|avatarurl|longtext|4294967295|头像|||
|content|longtext|4294967295|留言内容|||
|cpicture|longtext|4294967295|留言图片|||
|reply|longtext|4294967295|回复内容|||
|rpicture|longtext|4294967295|回复图片|||

14、供车人表：

表5-14 gongcheren

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
| :-: | :-: | :-: | :-: | :-: | :-: |
|addtime|timestamp||创建时间||CURRENT\_TIMESTAMP|
|zhanghao|varchar|200|账号|||
|mima|varchar|200|密码|||
|xingming|varchar|200|姓名|||
|xingbie|varchar|200|性别|||
|touxiang|longtext|4294967295|头像|||
|nianling|int||年龄|||
|shenfenzheng|varchar|200|身份证|||
|youxiang|varchar|200|邮箱|||
|dianhua|varchar|200|电话|||
|shenfenzhengzhao|longtext|4294967295|身份证照|||
|jiazhao|longtext|4294967295|驾照|||
|sfsh|varchar|200|是否审核||待审核|
|shhf|longtext|4294967295|审核回复|||

15、配置文件表：

表5-15 config

|字段名称|类型|长度|字段说明|主键|默认值|
| :-: | :-: | :-: | :-: | :-: | :-: |
|id|bigint||主键|主键||
|name|varchar|100|配置参数名称|||
|value|varchar|100|配置参数值|||

## 5\.2 页面功能实现
### 5\.2.1 首页功能
游客用户输入共享用车平台的URL后，进入平台首页。在首页上，用户可以查看导航栏、轮播图、平台简介和公告资讯，如图5-1所示。

图5-1 平台首页

通过导航栏，游客用户可以进入“公告资讯”和“车辆信息”详情页面，以查看发布的具体内容，如图5-2和图5-3所示。

图5-2 公告资讯详细页面

图5-3 汽车信息详细页面

然而，游客用户的权限仅限于信息浏览，如果他们想进行进一步的操作，需要进行账号注册。
### 5\.2.2 用车人页面功能
1、注册、登录功能。

点击首页右上角的“登录/注册”按钮，进入登录页面，如图5-4所示。点击“注册用车人”链接，输入基本资料信息并设置账号密码，然后上传用户头像、身份证和驾驶证的图片，并保存提交以完成账号注册，如图5-5所示。注册后的账号经管理员审核通过后才能生效。注册成功后，用车人回到登录页面登录系统，登录成功，如图5-6所示。

图5-4 用车人登录页面

图5-5 用车人注册页面

图5-6 登录成功

2、账号信息修改功能

用车人成功登录系统后，自动跳转至“个人中心”页面。通过该页面，用车人可以修改个人账号的资料信息和登录密码，并保存提交以更新数据，如图5-7所示。

图5-7 个人中心页面

3、车辆租赁功能

通过导航栏进入车辆信息页面，用车人可再此查看平台车辆信息。他们可以根据自身情况，在搜索栏中输入出发地以及所需车辆的名称、车型、品牌、载人数、载货量等信息，并点击查询按钮。根据这些信息，系统会筛选出车辆位置在用车人出发地且符合用车人需求的车辆，并显示车辆的品牌、名称、租金、租赁状态和车辆照片，如图5-8所示。

图5-8 车辆信息查询页面

用车人从中找到心仪的车辆后，可以点击车辆链接，进入详情页面查看该车辆及其车主的更多信息。此外，用车人还可以在此页面中进行点赞和收藏操作，或通过其中的供车人联系方式同车主进一步沟通，如图5-9所示。

图5-9 车辆详情页面

协商完成后，用车人点击租赁按钮，进入租赁订单页面。在该页面中，用户需要填写租车的出发地、目的地、载人数/运货量（客车填写载人数，货车填写运货量）、使用天数等相关信息，并保存提交以生成租赁订单，如图5-10所示。

图5-10 租赁订单页面

订单提交后，平台将通知该车辆的供车人，供车人同意租赁后订单成立，车辆租赁成功，该车辆的“车辆状态”更新为“已租赁”。租赁成功后，用户可以发表评论和留言，如图5-11所示。

图5-11 评论和留言

用车人在租赁车辆后，可以登录系统后台查看所有的租赁记录，并查看租赁审核状态。若审核状态为“已通过”，说明车主同意租赁，用车人可根据车辆地点去线下提车。具体操作如图5-12所示。

图5-12 租赁管理页面

4、车辆归还功能

车辆使用结束后，用车人可以在系统中申请归还。进入系统后台，可在“租赁管理页面”找到所租车辆对应的订单，如图5-13所示。点击归还，填写“归还说明”后提交，系统将自动生成归还记录，如图5-14所示。如果用车人希望查看车辆的归还情况，可以进入后台的“车辆归还”页面查看归还的审核状态，若显示“通过”则说明归还成功。

图5-13 车辆归还管理页面图

图5-14 归还申请页面

5、车辆收藏功能

如果用车人需要查看自己收藏的车辆信息，可以在“个人中心”点击“我的收藏”进行信息管理，如图5-15所示。进入“我的收藏”页面后，系统将显示用户点赞和收藏过的所有信息列表。用车人可以通过车辆名称搜索要寻找的车辆。之后点击图片链接，进入详情页面查看信息。同时，用户还可以点击“取消收藏”，将信息从收藏模块中移除，如图5-16所示。

图5-15 我的收藏页面

图5-16 详情页面
###  供车人页面功能
1、注册、登录、个人中心功能

希望利用闲置车辆的用户可注册供车人账号，用车人的注册、登录页面以及个人中心页面功能和用车人页面类似，如图5-17、图5-18所示。

图5-17 用车人注册页面


图5-18 个人中心页面

2、车辆租赁功能

完善个人信息后，供车人可以提交希望出租的闲置车辆信息，系统将为其上传车辆进行展示和宣传。供车人点击进入“车辆材料管理”页面，如图5-19所示。点击新增，填写车辆信息，在维护好车辆证明材料后保存并提交，即可生成新的车辆材料记录，如图5-20所示。这些记录需要管理员进行审核，审核通过后，供车人可在“车辆信息管理”页面，找到该车辆，车辆上传成功。

供车用户还可以对材料信息进行内容修改和删除。如果需要批量删除材料信息，用户可以勾选相应的记录，然后点击删除键进行删除操作。此外，用户还可以输入相关信息，进行车辆材料的快速筛选查询，如图5-20所示。

图5-19 车辆材料管理页面

图5-20 新增车辆页面

在“车辆信息管理”页面中，会显示供车人通过审核、可以出租的车辆信息，如图5-21所示。供车人可对这些信息进行查询和删除。供车人可对车辆信息进行修改，但他只能修改其中的“图片”、“每日租金”、“状态”和“详细介绍”的内容，其余信息无法更改。此外，供车用户还可以查看用车人对共享车的评价信息。

图5-21 车辆信息管理页面图

当供车人的车辆被用车人选择租赁后，系统会将此租赁订单发送给供车人，并显示在“租赁订单”列表，如图5-22所示。供车人进入“租赁订单管理”页面，可以查看订单详情，并选择是否同意租赁。若供车人同意，则可对租赁订单进行审核，审核通过后，租赁订单成立。而如果供车人拒绝租赁，一段时间后，该订单将被管理员删除。另外，用户还可以通过输入订单编号或车辆信息，进行租赁订单记录的快速筛选查询。

图5-22 租赁订单管理页面

3、车辆接收功能

当用车人通过系统归还车辆后，系统会将用车人填写的 “归还信息表”发送给供车人，并显示在“车辆归还”列表。供车人进入“车辆归还管理”页面，可以查看归还信息，如图5-23所示。在线上、线下确认后，若供车人允许归还，则对归还申请进行审核。审核通过后，系统确认车辆归还，订单完成。若供车人发现问题，拒绝确认车辆归还，用户可以勾选相应的记录，然后点击删除键进行删除操作。此外，用户还可以通过输入订单编号或车辆信息，进行租赁归还记录的快速筛选查询。

图5-23 车辆归还管理页面图
### 5\.2.4 管理员页面功能
1、账号信息管理功能

管理员账号负责整个平台信息数据的管理，其账号和密码由后台设置（初始默认为-u:admin;-p:admin）。登录后，同普通账号一样，可在个人中心修改管理员的账号信息，并可更新登录密码，如图5-24所示。



图5-24 个人中心管理页面图

2、用户管理功能

在“用车人管理页面”和“供车人管理页面”，管理员可以对用车人和供车人用户的信息进行管理和维护，确保用户信息的准确性和系统的正常运行，如图5-25、图5-26所示。例如，管理员需审核用户上传的身份证和驾驶证的真实性，如图5-27所示。通过这种方法，平台能尽可能维护用户的财产和人身安全。

管理员具有以下权限和功能：

1）用户信息编辑：包括对用户记录的新增、修改、删除和查询。管理员可以借此维护用车用户的基本资料信息，包括姓名、联系方式、地址等。

2）用户审核：管理员可以查看待审核的用户信息。这些刚完成注册的用车人账户，只有审核通过后才会生效，用户才能顺利登录系统进行操作。

图5-25 用车人信息管理页面

图5-26 供车用户管理页面

图5-27 信息审核页面

3、车辆类型管理功能

“车辆类型管理”页面，显示车辆类型信息的列表，包含小轿车、货车、房车、跑车、SUV等车型，如图5-28所示。供车人在填写车辆信息时，会从中选择自己的车辆对应的类型。管理员可以进入“车辆类型管理”页面，对车辆类型信息进行查询、添加和删除，确保系统能够按照不同的类型对车辆进行分类管理。

图5-28 车辆类型管理页面

“车辆材料管理”页面，显示车辆材料信息的列表，如图5-29所示。在这里，管理员可以对车辆材料信息进行管理和审核，确保车辆材料的有效性和合规性。在该页面，管理员具有以下权限和功能：

1）车辆材料信息编辑：包括对车辆材料的新增、修改、删除和查询。管理员可以点击材料记录，进入详情页面，查看车辆材料的详细信息，借此维护用车人上传到车辆信息，包括车辆名称、车辆类型、里程数、车牌号等。

2）下载并审核材料文件：为了维护平台用户的财产及人身安全，平台要求供车人上传车辆所有权证明材料和车辆安全证明材料。对于提交的材料申请，管理员可以进行下载操作，获取材料的电子版本，并对车辆材料进行审核。管理员可以选择多个材料记录进行批量审核操作。

3）添加合格车辆进入系统：车辆通过审核后，管理员点击“添加车辆”按钮，该车辆被加入系统的“车辆信息”列表，能够被租赁。其车主可登录用车人账户，在“车辆信息管理”页面中找到该车辆信息。

通过以上功能和权限，管理员可以对车辆材料信息进行管理和审核，确保车辆材料的准确性和合规性。

图5-29 车辆材料管理页面图

“车辆信息管理”页面，显示了所有通过审核的车辆的详细信息，如图5-30所示。管理员可以在此页面中对系统中的车辆信息进行管理，包括：快速筛选查询、修改车辆信息和批量删除。此外，管理员还能点击“查看评论”浏览曾租赁这些车辆的用车人们的评价。

图5-30 车辆信息管理页面图

“租赁订单管理”页面，显示了用车人在系统前端提交的租赁订单，如图5-31所示。管理员可以对这些订单进行管理，包括查看、修改和删除等操作。

管理员进入“租赁订单管理”页面后，点击租赁记录，进入订单详情页面，以查看该订单的详细信息，包括租赁的车辆信息、租赁时间、出发地、目的地、载人数、运货量、使用天数等相关信息。如果填写的信息有问题，管理员可以对租赁订单的内容进行修改和更新。

此外，管理员可以了解租赁订单的审核状态，以确定对应的供车人是否同意了用车人的租赁请求。若某条订单长期未能通过审核，管理员可将其勾选并批量删除。

图5-31 租赁订单管理页面图

“车辆归还管理”页面，显示了用车人申请归还车辆后的系统生成的归还信息记录，如图5-32所示。管理员可以对这些记录进行管理，包括查看、修改和删除操作。

此外，管理员可以了解归还的审核状态，以确定对应的供车人是否确认车辆归还。管理员可将已归还的历史记录勾选并批量删除。

图5-32 车辆归还管理页面

4、问题反馈管理

管理员可以查看前端用户发布的问题反馈信息并进行管理。

平台用户通过点击首页导航栏的“问题反馈”按钮，进入留言反馈页面，在该页面上，用户可以撰写需要反馈的留言和图片，并保存提交以生成新的反馈记录，该记录可以供所有用户浏览和查看。

提交的信息还会录入系统后台，显示在管理员的“问题反馈管理”页面中，如图5-33所示。管理员可以点击反馈记录，进入反馈详情页面，以查看该反馈的详细内容和反馈者的信息。管理员点击回复链接后，在弹出的编辑框中回复内容，然后提交完成。回复的信息会更新至前端用户的留言管理页面，供用户查看。


图5-33 问题反馈管理页面图

5、系统信息管理

管理员能通过“系统管理”页面，可以对系统首页的轮播图、平台简介、以及咨询公告进行管理。以下是管理员管理这些信息的具体操作：

1）轮播图片管理：管理员可以点击轮播图片管理链接，进入轮播图片管理页面。在该页面中，管理员可以替换轮播图片，选择新的图片并上传到系统中，以更新前端显示的轮播图片，如图5-34所示。

2）平台简介管理：管理员可以点击“关于我们”管理链接，进入平台简介管理页面。在该页面中，管理员可以编辑修改平台简介的文字信息和并上传相关的图片展示，以丰富平台简介的内容，如图5-35所示。

3）咨询公告管理：管理员可以点击“咨询公告”管理链接，进入平台公告管理页面。在该页面中，管理员可以发布系统的公告信息，包括公告标题、内容、发布时间等。发布的公告信息会显示在前端系统首页供用户查看，如图5-36所示。

图5-34 轮播图管理页面

图5-35 平台简介管理页面

图5-36 公告资讯管理页面

管理员能通过“在线客服”页面，与前端用户沟通，解答问题，如图5-37所示。

用户可以通过点击首页导航栏的“在线客服”按钮进入该功能页面，在对话框编辑输入想要提问的内容信息，与客服进行留言沟通。点击发送后，信息会上传至管理员系统，并显示在“在线客服”页面。

管理员可以点击咨询信息管理链接，进入“在线客服”页面。该页面会显示前端用户提交的咨询信息列表。点击相应的咨询记录，查看咨询详情，了解用户的问题和需求，并使用对话框，编辑输入回复的内容，点击发送进行回复，回复信息将会上传至系统并显示在前端用户的咨询记录中。此外，如果某条咨询记录无效或需要删除，管理员可以勾选相应的记录，将其从系统中删除。


图5-37 在线客服管理页面图

# 第6章 共享用车平台的测试
## 6.1 测试目的
系统测试的主要目的是确保软件系统的质量。通过测试，可以发现和修复系统中的缺陷、错误和故障，以提高系统的可靠性、稳定性和可用性。测试的一个重要目标是验证系统是否按照开发者设计思路或用户需求运行。基于以上理论，执行各种测试用例，以确保系统的功能符合预期、确保系统在用户使用时提供良好的体验和功能、发现并纠正与用户体验相关的问题，帮助用户准确高效地解决用车需求，避免因系统故障引起损失提高用户满意度和系统的用户友好性。
## 6\.2 测试用例
### 6.2.1 注册模块
1、输入的任何一项为空，结果如图6-1所示。

图6-1 输入为空

2、没有按规定格式输入，结果如图6-2所示。

图6-2 格式错误

3、输入已经注册过的用户名，结果如图6-3所示。

图6-3 用户名重复

4、两次输入密码不一致，结果如图6-4所示。

图6-4 密码不一致

5、同一输入项输入两张图片，结果如图6-5所示。

图6-5 输入两张图片
### 6.2.2 登录模块
1、输入任何一项为空，结果如图6-6所示。

图6-6 输入项为空

2、用户名和密码有任何一项错误，结果如图6-7所示。

图6-7 密码错误
### 6\.2.3 用车人模块
用车人归还未通过/待审核的车辆，如图6-8所示。

图6-8 归还错误

结果如图6-9所示。

图6-9 无法归还
### 6\.2.3 供车人模块
供车人在个人中心修改密码时，需要输入原密码进行验证。如果原密码输入错误，如图6-10所示。

图6-10 输入错误

结果如图6-11所示。

图6-11 原密码错误
## 6.3 测试结果
根据大量的测试，可以说共享用车平台管理系统在功能上与开发项目是一致的，没有影响用户使用的bug，在安全性和稳定性上也非常符合条件。该系统功能基本达到了预期效果。
