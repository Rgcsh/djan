学习Django框架

知识如下：

.项目目录结构设计=配置文件根据不同环境进行分配，路由在每个app中进行注册，生成requirements.txt文件

.数据库导出和导入及跨数据库平台导入导入数据

.数据库迁移

.django-celery进行异步任务及查询任务执行结果

.定制中间件

.django-redis进行缓存及原生redis进行复杂数据格式的操作

.在日志模块中启动出现Error，发送邮件给管理员

.后台管理进行定制

.后台管理系统的使用

.使用debug_toolbar及其定制 监测系统各种数据

.信号的使用

.django数据库的CURD

.django的单元测试

.配置文件的使用

学习体验总结：

.之前工作学习的是flask和tornado框架，在学习django框架之后，发现django框架真的是大而全，强大的后台管理系统，仅仅进行简单的定制及权限管理，便能满足现公司财务及客服人员进行的相关操作，根本无需前端人员进行相关开发，当然了，官网也说了 后台管理系统不可能代替复杂的前端项目。

.django相对于flask,在内置的Model层便有一系列表字段输入的限制，并且可以自己根据需求进行定制。不像flask字段校验所需编码时间成本较高。

.django的中间件机制和flask的before_request的方式基本没有区别，都是在请求进入到路由函数前进行相关验证及限制

.django的信号机制能够很好的解决功能性代码和业务逻辑性代码的耦合问题及大量复用代码。

.相对于flask,因为django功能齐全，在使用时不用像flask那样需要安装许多额外的包，许多功能内置的都有，比如数据库的迁移。

.但是无论flask或者django,其优点往往在另一个层面代表了它的缺点。

.django走的是功能齐全，能够快速建站的套路，但是因此其相对于的限制也过多，灵活性没有flask强。

.flask走的是短小精悍，轻便灵活，易于扩展，但是也因此导致在开发初期或者新功能实现初期，相比django要慢一些。因为所有的功能都要自己实现，不想django内置了诸多功能。













