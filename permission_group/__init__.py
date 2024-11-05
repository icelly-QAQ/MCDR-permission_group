from mcdreforged.api.all import *


help_msg = """§aPermission Group 帮助列表§r
§b!!pg <player> <add|remove> <group> §f- §e把玩家添加或移除组"""


def help_message(src: PluginServerInterface):
    src.reply(help_msg)
    
def run_command(src: PluginServerInterface, context: CommandContext):
    player = context["player"]
    action = context["action"]
    group = context["group"]
    src.reply(f"player:{player},action:{action},group:{group}")

def all_command(src: PluginServerInterface):
    builder = SimpleCommandBuilder()

    builder.command("!!pg", help_message)
    builder.command("!!pg help", help_message)
    builder.command("!!pg <player> <action> <group>", run_command)
    builder.arg("player", Text)
    builder.arg("action", Text)
    builder.arg("group", Text)
    builder.register(src)

    
def on_load(server: PluginServerInterface, old):
    server.logger.info('this plugin by icelly_QAQ!')
    server.register_help_message('!!pg help', "获取帮助")
    all_command(server)