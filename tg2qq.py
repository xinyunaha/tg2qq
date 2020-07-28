from telegram.ext import Updater, MessageHandler, Filters
import websocket
import json
import config
import threading

ws = None
updater = None


def qq():
    def on_message(ws, message):
        # print(ws)
        print(message)
        msgType = json.loads(message)['message_type']
        if msgType == 'group':
            group = json.loads(message)['group_id']
            if group == config.qq1:
                text = json.loads(message)['message']
                user = json.loads(message)['sender'].get('card')
                SendMsg = f'QQ [{user}]:\n{text}'
                updater.bot.send_message(config.tg_group, SendMsg)
            else:
                print('非指定群消息')
        else:
            print('非群消息')

    def on_error(ws, error):
        # print(ws)
        print(error)

    def on_close(ws):
        print('ws closed')

    # websocket.enableTrace(True)
    global ws
    ws = websocket.WebSocketApp(config.ws_url,
                                on_message=on_message,
                                on_close=on_close,
                                on_error=on_error)

    ws.run_forever(ping_interval=30, ping_timeout=10)


def tg():
    global updater
    if config.proxy:
        updater = Updater(token=config.PoiGuGuGu_token, request_kwargs={'proxy_url': config.proxy_url}, use_context=True)
    else:
        updater = Updater(token=config.PoiGuGuGu_token, use_context=True)
    dispatcher = updater.dispatcher
    print(updater.bot.get_me())

    def msgHandler(msg, context):
        msgJsonStr = json.loads(
            str(msg.message).replace("'", '"').replace('False', 'false').replace('True', 'true'))
        text = msg.message.text
        if len(text) > config.tg_message_max:
            pass
        else:
            # group = msgJsonStr['chat'].get('id')
            user = msgJsonStr['from'].get('username')
            SendMsg = f'来自TG [{user}]:\n{text}'
            JsonStr = {"action": "send_group_msg", "params": {"group_id": config.qq_group, "message": SendMsg}}
            ws.send(json.dumps(JsonStr))

    dispatcher.add_handler(MessageHandler(Filters.text, msgHandler))
    updater.start_polling()


qq = threading.Thread(target=qq)
tg = threading.Thread(target=tg)

qq.start()
tg.start()