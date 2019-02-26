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

MASTER_UUID     = "0b4f49dc-8fb4-4539-9a89-fb3afc613747";
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";

def on_message(ws, message):
    inbuffer = BytesIO(message)

    f = gzip.GzipFile(mode="rb", fileobj=inbuffer)
    rdata_injson = f.read()
    rdata_obj = json.loads(rdata_injson)
    print("-------json object begin---------")
    print(rdata_obj)
    print("-------json object end---------")
    action = rdata_obj["action"]
    if action == "ERROR":
        return;

    # if rdata_obj["data"] is not None:
    #     print("data in message:",rdata_obj["data"])
    #
    # if rdata_obj["data"] is not None and rdata_obj["data"]["category"] is not None:
    #     print(rdata_obj["data"]["category"])

    if action == "CREATE_MESSAGE":

        data = rdata_obj["data"]
        msgid = data["message_id"]
        typeindata = data["type"]
        categoryindata = data["category"]
        userId = data["user_id"]
        conversationId = data["conversation_id"]
        dataindata = data["data"]
        created_at = data["created_at"]
        updated_at = data["updated_at"]

        realData = base64.b64decode(dataindata)

        MIXIN_WS_API.replayMessage(ws, msgid)

        print('userId', userId)
        print("created_at",created_at)

        if categoryindata == "PLAIN_TEXT":
            realData = realData.decode('utf-8')
            print("dataindata",realData)
            if 'a' == realData:
                print('send a link APP_CARD')
                MIXIN_WS_API.sendAppCard(ws, conversationId, mixin_config.client_id,
                                        BTC_ASSET_ID, "0.0001",
                                        "https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128",
                                        "Pay BTC 0.0001","topay")
                return
            if 'g' == realData:
                print('send a link APP_BUTTON_GROUP')
                btnBTC    = MIXIN_WS_API.packButton(mixin_config.client_id, BTC_ASSET_ID, "0.0001","BTC pay")
                btnEOS    = MIXIN_WS_API.packButton(mixin_config.client_id, EOS_ASSET_ID, "0.01","EOS pay","#0080FF")
                buttons   = [btnBTC,btnEOS]
                MIXIN_WS_API.sendAppButtonGroup(ws, conversationId, userId, buttons)
                return
            MIXIN_WS_API.sendUserText(ws, conversationId, userId, realData)
        elif categoryindata == "SYSTEM_ACCOUNT_SNAPSHOT":
            rdJs = json.loads(realData)
            if ( float(rdJs["amount"]) > 0 ):
                mixin_api.transferTo(userId, rdJs["asset_id"], rdJs["amount"], "")

if __name__ == "__main__":

    mixin_api = MIXIN_API(mixin_config)

    mixin_ws = MIXIN_WS_API(on_message=on_message)

    mixin_ws.run()
