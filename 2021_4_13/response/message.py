"""
定义响应消息.
"""


class ResponseMessage:
    """
    响应消息类.
    """
    def __init__(self, code, msg, data):
        """
        初始化状态码 / 消息体 / 返回数据
        """
        self._code = code
        self._msg = msg
        self._data = data

    def json_message(self):
        return {'code': self._code, 'msg': self._msg, 'data': self._data}

    @classmethod
    def success(cls, data):
        code = 0
        msg = 'success'
        res_obj = cls(code, msg, data)
        return res_obj.json_message()


print(ResponseMessage.success({'name': 'niu'}))
