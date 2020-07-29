import sys
import json

sys.path.append('..')
import config


def SendText_Custom(context, group, message):
    JsonStr = {"action": "send_group_msg", "params": {"group_id": config.qq_group, "message": ''}}
    context.send(json.dumps(JsonStr))


def SendPicture_Custom(context, group, picture):
    JsonStr = {"action": "send_group_msg", "params": {"group_id": config.qq_group, "message": ''}}
    context.send(json.dumps(JsonStr))


# tg消息处理
def IsText(_json):
    pass


def IsPicture(_json):
    pass


def ToJson(text):
    try:
        _json = json.loads(str(text).replace("'", '"').replace('False', 'false').replace('True', 'true'))
        _dict = {'group': _json['chat'].get('id'), 'text': _json['text'],
                 'user': _json['from'].get('username'),
                 'bot': _json['from'].get('is_bot')}
        if len(_dict['text']) > config.tg_message_max:
            return 'length max'
        else:
            return _dict
    except:
        return 'json error'


def SendTextToQQ(context, text):
    _dict = ToJson(text)
    if type(_dict) != dict:
        if _dict == 'json error':
            return 'json解析错误'
        elif _dict == 'length max':
            return '消息长度上限'
    else:
        return _dict

