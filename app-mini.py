from mixin_ws_api import MIXIN_WS_API
from mixin_api import MIXIN_API
import mixin_config

import json
import time
from io import BytesIO
import base64
import gzip

try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    inbuffer = BytesIO(message)

    f = gzip.GzipFile(mode="rb", fileobj=inbuffer)
    rdata_injson = f.read()
    rdata_obj = json.loads(rdata_injson)
    print("-------json object begin---------")
    print(rdata_obj)
    print("-------json object end---------")
    action = rdata_obj["action"]

    if rdata_obj["data"] is not None:
        print("data in message:",rdata_obj["data"])

    if rdata_obj["data"] is not None and rdata_obj["data"]["category"] is not None:
        print(rdata_obj["data"]["category"])

    if action == "CREATE_MESSAGE":

        data = rdata_obj["data"]
        msgid = data["message_id"]
        typeindata = data["type"]
        categoryindata = data["category"]
        userId = data["user_id"]
        conversationId = data["conversation_id"]
        dataindata = data["data"]

        realData = base64.b64decode(dataindata)

        MIXIN_WS_API.replayMessage(ws, msgid)

        if 'error' in rdata_obj:
            return

        if categoryindata == "PLAIN_TEXT":
            realData = realData.decode('utf-8')
            print("dataindata",realData)
            MIXIN_WS_API.sendUserText(ws, conversationId, userId, realData)


if __name__ == "__main__":

    mixin_api = MIXIN_API(mixin_config)
    mixin_ws = MIXIN_WS_API(on_message=on_message)
    mixin_ws.run()
