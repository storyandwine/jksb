# jksb_sysu

基于 [@tomatoF](https://github.com/tomatoF) 的 [jksb_sysu](https://github.com/tomatoF/jksb_sysu) 项目，适配了 GitHub Actions，可以实现每天定时运行，并使用微信发送运行结果。

**经过简单测试，已经可以正常运行**

## 技术方案

python+selenium+firefox。

## 项目配置

首先 Fork 此项目**顺便 Star 一下**，之后前往 Settings-Secrets 填写下列信息，注意需要大写。

|NETID|PASSWORD|SEND_KEY|RECURL|

|NETID|密码|sct.ftqq.com/sendkey|[第三方在线识别平台](http://fast.95man.com)api地址|

### 验证码

采用[第三方在线识别平台](http://fast.95man.com)，每日免费额度100，请自行前往注册账号，获取 Token。

将上述的 api地址 填入 `RECURL` 中。

### 账号密码

将 netid 填入 `NETID` 中，将密码填入 `PASSWORD` 中。



## 免责声明

此脚本仅供学习交流，禁止商业使用，使用软件过程中，发生意外造成的损失由使用者承担。如遇身体不适、或居住地址发生变化，请及时更新健康申报信息。
