from mcdreforged.api.all import *
import minecraft_data_api as api
import datetime

builder = SimpleCommandBuilder()

help_msg = """§aBatter Manage 帮助列表§r
§b!!bm list §f- §e获取所有在线玩家列表
§b!!bm kick <player> <massge> §f- §e踢出玩家, <massge>为踢出信息
§b!!bm ban <player> §f- §eban玩家
§b!!bm op <passwd> <player> §f- §e获取op，<passwd>为配置文件中设置的密码，<player>为被设定op的玩家
"""

dim_convert = {
    0: '主世界',
    -1: '地狱',
    1: '末地'
}

class Config(Serializable):
    passwd: str = "admin"
    permission: int = 4

config: Config

# 命令执行
def help_message(src: PluginServerInterface):   # 帮助信息
    src.reply(help_msg)

def add_log(name, passwd, status):
    with open("op_log.log", "a+") as data:
        data.write(f"「{datetime.datetime.today()}」玩家名：{name}   使用密码：{passwd}   状态：{status}\n")


@new_thread
def run_list(src: PluginServerInterface):  # 获取玩家列表
    amount, limit, players = api.get_server_player_list()
    if amount == 0:
        src.reply("§c当前没有玩家在线！")
    else:
        src.reply(f"玩家列表 §b{amount}/{limit}：")
        for player in players:
            coord = api.get_player_coordinate(player)
            dimension = api.get_player_dimension(player)
            src.reply((f"§b{player} §f：\n §e所在纬度：{dim_convert[dimension]}\n §e所在坐标({dim_convert[dimension]})：{round(coord.x, 0)}, {round(coord.y, 0)}, {round(coord.z, 0)}\n"))

def get_op(source: CommandSource, context: CommandContext):   # 获取op
    if context['passwd'] == config.passwd:
        source.get_server().execute(f"op {context['player']}")
        source.reply(f"已将「§6{context["player"]}§f」设为OP！")
        add_log(context['player'], context['passwd'], "成功")
    else:
        add_log(context['player'], context['passwd'], "失败")
        source.reply("§c密码错误！")

def kick_player(source: CommandSource, context: CommandContext):    # 踢出玩家
    if source.has_permission(config.permission):
        source.get_server().execute(f"kick {context["player"]}")
        source.reply(f"已将「§c{context["player"]}§f」§f踢出游戏！")
    else:
        source.reply("§c权限不足！！！")

def ban_player(source: CommandSource, context: CommandContext):
    if source.has_permission(config.permission):
        source.get_server().execute(f"ban {context["player"]}")
        source.reply(f"已封禁「§c{context["player"]}§f」")
    else:
        source.reply("§c权限不足！！！")


# 命令构建
def all_command(src: PluginServerInterface):  # 所有命令
    builder.command("!!bm", help_message)
    builder.command("!!bm help", help_message)
    builder.command("!!bm list", run_list)  # 获取玩家列表
    builder.command("!!bm op <passwd> <player>", get_op)    # 获取op
    builder.command("!!bm kick <player>", kick_player)   # 踢出玩家
    builder.command("!!bm ban <player>", ban_player)    # ban玩家

    builder.arg('passwd', Text)
    builder.arg('player', Text)

    builder.register(src)   # 将所有注册的命令和参数注册到插件服务器接口

def on_load(server: PluginServerInterface, old):
    global config

    config = server.load_config_simple(target_class=Config)
    server.logger.info('this plugin by icelly_QAQ!')
    server.register_help_message('!!bm help', "获取帮助")
    all_command(server)
