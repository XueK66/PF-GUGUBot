# -*- coding: utf-8 -*-
from .base_system import base_system
from ..data.text import key_word_help
from aiocqhttp import CQHttp
from mcdreforged.api.types import PluginServerInterface, Info

class key_word_system(base_system):
    def __init__(self, path: str, help_msg = key_word_help):
        super().__init__(path, help_msg)

    def handle_command(self, raw_command:str, bot:CQHttp, info: Info, reply_style:str='正常', *arg, **kargs):
        parameter = raw_command.strip().split() 
        if parameter[0] in ['添加', 'add', '删除','移除', 'del', '列表','list']:
            raw_command = "关键词 " + raw_command

        super().handle_command(raw_command, bot, info, reply_style, *arg, *kargs)

    def check_response(self, key_word):                                                
        if key_word in self.data:
            return self.data[key_word]
