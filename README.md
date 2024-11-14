# 基于 MCDR 的玩家管理插件

### ***让你在没有OP的情况下管理你的玩家！***

### 食用方法：

1. 使用 MCDR 命令 !!MCDR plugin install batter_manage 安装插件

2. 使用 MCDR 命令 !!bm help 或 !!bm 查看帮助

### config配置方式：

- passwd ： 获取op的密码，默认为「 admin 」***切记要更改密码，获取op的命令没有权限等级检查！（本意是为了方便被信任但没有权限的玩家获取op）***

- permission ： 执行命令的最低权限，默认为「 4 」

| **名称** | **整数值** | **描述** |
|:-------:|:-------:|:-------|
| owner | 4 | 最高权限，所有者，具有控制物理服务器的能力。例子：服务器拥有者 |
| admin | 3 | 管理员，拥有控制 MCDR 与 Minecraft 服务器的能力。例子：Minecraft 中的 OP |
| helper | 2 | 助手，可以协助管理员进行服务器管理。例子：值得信赖的成员 |
| user | 1 | 普通玩家 |
| guest | 0 | 最低权限，如访客或者熊孩子 |

***选自 https://docs.mcdreforged.com/zh-cn/latest/permission.html***

### 功能：

1. 玩家管理

2. 玩家封禁

4. 玩家踢出

5. 获取玩家列表

***by icelly_QAQ***