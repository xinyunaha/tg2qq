import json
import config


def SendText_Custom(context, group, message):
    JsonStr = {"action": "send_group_msg", "params": {"group_id": group, "message": message}}
    context.send(json.dumps(JsonStr))


def SendPicture_Custom(context, group, picture):
    JsonStr = {"action": "send_group_msg", "params": {"group_id": group, "message": ''}}
    context.send(json.dumps(JsonStr))


# tg消息处理
def IsText(_json):
    pass


def IsPicture(_json):
    pass


# json解析收到的消息
def ToJson_Text(text):
    try:
        _json = json.loads(str(text).replace("'", '"').replace('False', 'false').replace('True', 'true'))
    except:
        return 'json error'
    _dict = {'group': _json['chat'].get('id'), 'text': _json['text'],
             'user': _json['from'].get('username'),
             'bot': _json['from'].get('is_bot')}
    if len(_dict['text']) > config.tg_message_max:
        return 'length max'
    elif config.tg_bot_message and _dict['bot'] == 'true':
        return 'is bot message'
    elif str(_dict['group']) not in config.tg_group_dict:
        return 'group error'
    else:
        return _dict


def SendTextToQQ(context, text):
    _dict = ToJson_Text(text)
    if type(_dict) != dict:
        if _dict == 'json error':
            return 'json解析错误'
        elif _dict == 'length max':
            return '消息长度上限'
        elif _dict == 'is bot message':
            return 'bot消息,不转发'
        elif _dict == 'group error':
            return '非指定消息群'
    else:
        SendText_Custom(context=context, message='来自TG [{0}]:\n{1}'.format(_dict['user'], _dict['text']), group=config.tg_group_dict[str(_dict['group'])])
        return _dict
