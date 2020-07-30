import os
import sys


def ClearScreen():
    import platform
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


ClearScreen()
try:
    from telegram.ext import Updater, MessageHandler, Filters
except ImportError:
    print('尝试补全依赖: python-telegram-bot')
    os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple python_telegram_bot')
    ClearScreen()

try:
    import websocket
except ImportError:
    print('尝试补全依赖: websocket_client')
    os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple websocket_client')
    ClearScreen()

try:
    from termcolor import colored
except ImportError:
    print('尝试补全依赖: termacolor')
    os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple termcolor')
    ClearScreen()

try:
    import requests
except ImportError:
    print('尝试补全依赖: requests')
    os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests')
    ClearScreen()

try:
    print(colored('依赖检查...pass', 'green'))
except:
    print('依赖安装完成，再运行一次吧')
    sys.exit(1)

with open('config_test.py', 'w+', encoding='utf-8') as f:
    while True:
        ws_url = input(colored('请输入ws地址(例如ws://127.0.0.1:1234):', 'yellow'))
        try:
            websocket.create_connection(ws_url, timeout=3)
            break
        except:
            print(colored('ws连接检测....failed', 'red'))
    print(colored('ws连接检测....pass', 'green'))
    f.write('# cqhttp插件设置的websocket地址\n')
    f.write(f'ws_url = \'{ws_url}\'\n')

    while True:
        proxy = input(colored('tg是否使用代理(y/n):', 'yellow'))
        if proxy == 'y':
            f.write('# tg是否使用代理\n')
            f.write(f'proxy = True\n')
            break
        elif proxy == 'n':
            f.write('# tg是否使用代理\n')
            f.write(f'proxy = False')
        else:
            print(colored('输入错误', 'red'))

    if proxy == 'y':
        while True:
            proxy_url = input(colored('输入您的http代理地址(例如127.0.0.1:1234)：', 'yellow'))
            try:
                code = requests.get('http://www.google.com', proxies={"http": proxy_url}, timeout=5)
                if code.status_code == 200:
                    print(colored('代理连接测试....pass', 'green'))
                    f.write('# 代理链接\n')
                    f.write(f'proxy_url = \'{proxy_url}\'\n')
                    break
                else:
                    print(colored('代理连接测试....failed', 'red'))
            except requests.exceptions.ProxyError:
                print(colored('代理连接测试....failed', 'red'))
    if proxy == 'n':
        f.write('# 代理链接\n')
        f.write(f'proxy_url = ''\n')

    tg_bot_token = input(colored('请输入tg机器人的token:', 'yellow'))
    f.write('# tg—bot的token\n')
    f.write(f'tg_bot_token = \'{tg_bot_token}\'\n')

    tg_message_max = input(colored('tg消息转发长度限制:', 'yellow'))
    f.write('# tg消息转发长度限制\n')
    f.write(f'tg_message_max = \'{tg_message_max}\'\n')

    qq_message_max = input(colored('qq消息转发长度限制:', 'yellow'))
    f.write('# qq消息转发长度限制\n')
    f.write(f'qq_message_max = \'{qq_message_max}\'\n')

    while True:
        tg_bot_message = input(colored('tg其他bot消息是否转发(y/n):', 'yellow'))
        if tg_bot_message == 'y':
            f.write('# 转发tg其他bot的消息\n')
            f.write(f'tg_bot_message = True\n')
            break
        elif tg_bot_message == 'n':
            f.write('# 转发tg其他bot的消息\n')
            f.write(f'tg_bot_message = False\n')
            break
        else:
            print(colored('输入错误', 'red'))

    while True:
        MultipleGroup = input(colored('是否同时转发多个群消息(y/n):', 'yellow'))
        if tg_bot_message == 'y':
            f.write('# 同时转发多个群消息(一对一)\n')
            f.write(f'multiple_group = True\n')
            break
        elif tg_bot_message == 'n':
            f.write('# 同时转发多个群消息(一对一)\n')
            f.write(f'multiple_group = False\n')
            break
        else:
            print(colored('输入错误', 'red'))

    qq_group_dict = {}
    while True:
        if MultipleGroup == 'y':
            qq_group = input(colored('输入一个QQ群号:', 'yellow'))
            tg_group = input(colored(f'输入{qq_group}需要转发的TG群号:', 'yellow'))
            qq_group_dict[str(qq_group)] = str(tg_group)
            is_continue = input(colored('还要添加吗?(y/n):'))
            if is_continue == 'y':
                pass
            elif is_continue == 'n':
                break
            else:
                print(colored('输入错误', 'red'))
    f.write('# QQ群号\n')
    f.write(f'qq_group_dict = {qq_group_dict}\n')
    f.write('# TG群号\n')
    f.write(f'tg_group_dict = %s\n' % {key: value for value, key in qq_group_dict.items()})
    print(colored('感谢使用tg2qq,现在您可以运行main.py开始使用了', 'green'))