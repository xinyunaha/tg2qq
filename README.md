## tg2qq
这是一个使用coolq以及python-telegram-bot库的一个tg、qq互相转发的简易bot
## 实现的功能
- [x] 互相转发文本消息
- [x] 使用http代理连接tg 
- [ ] 多群消息转发(一对一)
- [ ] 多群消息转发(一对多)
- [ ] QQ消息分流发送
- [ ] qq->tg发送图片
- [ ] tg->qq发送图片(需要coolq pro)
- [ ] 语音转文字发送(qq->tg)
- [ ] 带敏感词不转发
## 如何使用
* 确保已经安装了python环境,pip可以使用
* 使用如下命令运行:python main.py
* [可选] 复制config-example.py为config.py并编辑config.py,修改为您的配置
## coolq配置
* [安装coolq](https://cqp.cc/)
* [安装cqhttp插件](https://github.com/richardchien/coolq-http-api/releases)
* [打开websocket功能](https://cqhttp.cc/docs/4.15/#/WebSocketAPI)
## 使用的库
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
