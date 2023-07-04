# PF-QQchat
#### PFingan服务器MCDRQQ机器人插件  
源：[QQChat-用于连接Minecraft和QQ的插件](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/qq_chat)<br>
修改：XueK__ [前往主页](https://github.com/XueK66)
### 这是基于原插件的修改版本

## 依赖
### Python包
- [requests](https://www.python.org/)
### Python模块
- 已存储在插件对应的文件夹内的 [requirements.txt](requirements.txt) 中, 可以使用 `pip install -r requirements.txt` 安装
### 前置插件
- [CoolQAPI](https://github.com/AnzhiZhang/CoolQAPI)
- [OnlinePlayerAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/.archived/OnlinePlayerAPI)
- [ConfigAPI](https://github.com/MCDReforged/ConfigAPI)
- [JsonDataAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/.archived/JsonDataAPI)

## 功能列表
QQ部分帮助，向QQ机器人发送，可以私聊也可以群聊发送 `#帮助`
<br>基本功能：聊天互相转发
#### 部分功能在群聊和私聊都能使用
### 管理员部分，请私聊机器人
```
#绑定   -> 查看绑定相关帮助
#白名单 -> 查看白名单相关帮助
#启动指令 -> 查看启动指令相关帮助
#违禁词 -> 查看违禁词相关帮助
#关键词 -> 查看关键词相关帮助
#游戏内关键词 -> 查看游戏内关键词相关帮助
#uuid   -> 查看uuid 匹配相关帮助
#名字   -> 查看机器人名字相关帮助
#审核   -> 协助审核功能
```
* 游戏ID与QQ绑定 `#绑定`
```
#绑定 列表 -> 查看绑定列表
#绑定 查询 <QQ号> -> 查询绑定ID
#绑定 解绑 <QQ号> -> 解除绑定
#绑定 <QQ号> <游戏ID> -> 绑定新ID
```
* 白名单管理 `#白名单`
```
#白名单 添加 <target> -> 添加白名单成员
#白名单 列表 -> 列出白名单成员
#白名单 关   -> 关闭白名单
#白名单 开   -> 开启白名单
#白名单 重载 -> 重载白名单
#白名单 删除 <target> -> 删除白名单成员
<target> 可以是玩家名/目标选择器/UUID
```
* 服务器启动时执行指令 `#启动指令`
```
#启动指令 添加 <名称> <指令> -> 添加启动指令
#启动指令 列表 -> 查看现有启动指令
#启动指令 删除 <名称> -> 删除指定启动指令
#启动指令 开   -> 开启开服指令
#启动指令 关   -> 关闭开服指令
#启动指令 执行 -> 执行一遍开服指令
#启动指令 重载 -> 重载开服指令
```
* 触发(包含模式)违禁词自动撤回 `#违禁词`
```
#违禁词 添加 <违禁词> <违禁理由> -> 添加违禁词
#违禁词 列表 -> 显示违禁词列表及理由
#违禁词 删除 <违禁词> -> 删除指定违禁词
#违禁词 开   -> 开启违禁词
#违禁词 关   -> 关闭违禁词
#违禁词 重载 -> 重载违禁词
```
* 发送关键词（完全匹配模式）自动回复，支持图片 `#关键词`
```
#关键词 开   -> 开启关键词
#关键词 关   -> 关闭关键词
#关键词 重载 -> 重载关键词
#关键词 列表 -> 显示关键词列表
#添加 <关键词> <回复> -> 添加关键词
#删除 <关键词> -> 删除指定关键词
```
* 游戏内关键词 `#游戏内关键词`
```
#不再提供开关
```
* uuid 匹配 游戏ID，如果有时游戏内现实ID不匹配，可以尝试重新匹配一下uuid `#uuid`
```
#uuid 列表   -> 查看uuid绑定表
#uuid 重载 -> 重新匹配uuid
#uuid 更新 <老ID> <新ID> -> 改白名单的名字
/uuid name 查看白名单名字 #此功能已失去
```
* 让机器人昵称显示为在线人数 `#名字`
```
#名字 开 -> 机器人名字显示为在线人数,需要在配置文件内配置服务器公网或IP域名和端口(一直显示会占用少许服务器资源)
#名字 关 -> 机器人名字为特殊空白名字，如果不支持请关闭此功能，然后你就可以自己给机器人命名了
```
* 协助审核,会自动识别加群申请，通过申请填写的回答（请将问题设置为"你的邀请人？"或"你的邀请人?"）的 <别名> 并将请求通过私聊和群聊艾特的方式将申请人昵称和回答发送到审核员，若审核员游戏在线还会发送到游戏，此时审核员只需在游戏、群聊或私聊发送通过即可同意申请 `#审核`
```
#审核 开 -> 开启自动审核
#审核 关 -> 关闭自动审核
#审核 添加 <QQ号> <别名> -> 添加审核员的别名(匹配用)
#审核 删除 <QQ号> -> 删除审核员
#审核 列表 -> 审核员列表
```

### 群聊部分，请在群内使用
```
#玩家 -> 获取在线玩家列表
#假人 -> 获取在线假人列表
#绑定 <游戏ID> -> 绑定你的游戏ID
#mc <消息> -> 向游戏内发送消息（可以触发游戏内关键词）
#风格 -> 机器人风格帮助
#游戏关键词 列表 -> 显示现有游戏内关键词列表
#删除假人 <假人名字> -> 删除游戏内指定假人

关键词相关：
#添加 <关键词> <回复> -> 添加游戏内关键词回复
#添加图片 <关键词> -> 添加关键词图片
#删除 <关键词> -> 删除关键词
#列表 -> 获取关键词回复列表
```
* 机器人回复风格切换 `#风格`
```
#风格 列表   -> 风格列表
#风格 <风格> -> 切换至指定风格
```
- 内置模式：`普通` `傲娇`
- AI生成后内置的模式：`雌小鬼` `御姐` `萝莉` `波奇酱` `病娇` `中二病`

## 配置文件
[点击查看配置文件说明](https://github.com/LoosePrince/PF-GUGUBot/blob/main/Config-QQChat.yml)

# 使用条款
- 禁止声明为你原创
- 在关键词回复处添加以下关键词 `插件来源` -> `https://github.com/LoosePrince/PF-MCDRQQchat`
- 禁止商业服使用、盈利等
- 禁止售卖
- 允许二次创作，但请标明来源
