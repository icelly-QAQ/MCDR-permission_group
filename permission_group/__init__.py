from typing import Literal
from mcdreforged.api.command import *
from mcdreforged.api.types import PluginServerInterface, Info

def all_command(server: PluginServerInterface):
        server.register_command(
        Literal("!!pg")
        .then(Text("player"))
        .then(Text("group"))
    )

def on_load(server: PluginServerInterface, old):
    server.logger.info('this plugin by icelly_QAQ!')
    server.register_help_message('!!pg', "获取帮助")
    all_command(server)