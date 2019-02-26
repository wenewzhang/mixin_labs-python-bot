In [the previous chapter](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README.md), we created our first app, when user sends "Hello,world!", the bot reply the same message.

# Receive and send Bitcoin in Mixin Messenger

> app.py
```python
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
        created_at = data["created_at"]
        updated_at = data["updated_at"]

        realData = base64.b64decode(dataindata)

        MIXIN_WS_API.replayMessage(ws, msgid)

        print('userId', userId)
        print("created_at",created_at)

        if categoryindata == "PLAIN_TEXT":
            realData = realData.decode('utf-8')
            print("dataindata",realData)
            MIXIN_WS_API.sendUserText(ws, conversationId, userId, realData)
        elif categoryindata == "SYSTEM_ACCOUNT_SNAPSHOT":
            rdJs = json.loads(realData)
            if ( float(rdJs["amount"]) > 0 ):
                mixin_api.transferTo(userId, rdJs["asset_id"], rdJs["amount"], "")

if __name__ == "__main__":

    mixin_api = MIXIN_API(mixin_config)

    mixin_ws = MIXIN_WS_API(on_message=on_message)

    mixin_ws.run()

```
### Hello Bitcoin!
Execute **python app.py** in the project directory.
```bash
cd mixin_labs-python-bot
source ./bin/activate
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app.py
ws open
-------json object begin---------
{'id': 'fd6ce766-331a-11e9-92a9-20c9d08850cd', 'action': 'LIST_PENDING_MESSAGES'}
-------json object end---------
```
Developer can send Bitcoin to their bots in message panel. The bot receive the Bitcoin and then send back immediately.
![transfer and tokens](https://github.com/wenewzhang/mixin_network-nodejs-bot2/blob/master/transfer-any-tokens.jpg)

User can pay 0.001 Bitcoin to bot by click the button and the 0.001 Bitcoin will be refunded in 1 second,In fact, user can pay any coin either.
![pay-link](https://github.com/wenewzhang/mixin_network-nodejs-bot2/blob/master/Pay_and_refund_quickly.jpg)

## Source code summary
```python
elif categoryindata == "SYSTEM_ACCOUNT_SNAPSHOT":
    rdJs = json.loads(realData)
    if ( float(rdJs["amount"]) > 0 ):
        mixin_api.transferTo(userId, rdJs["asset_id"], rdJs["amount"], "")
```
* rdJs["amount"] is negative if bot sends Bitcoin to user successfully.
* rdJs["amount"] is positive if bot receive Bitcoin from user.
Call mixin_api.transferTo to refund the coins back to user.

## Advanced usage
#### APP_BUTTON_GROUP
In some payment scenario, for example:
The coin exchange provides coin-exchange service which transfer BTC to EOS ETH, BCH etc,
you want show the clients many pay links with different amount, APP_BUTTON_GROUP can help you here.
```python
print('send a link APP_BUTTON_GROUP')
btnBTC    = MIXIN_WS_API.packButton(mixin_config.client_id, BTC_ASSET_ID, "0.0001","BTC pay")
btnEOS    = MIXIN_WS_API.packButton(mixin_config.client_id, EOS_ASSET_ID, "0.01","EOS pay","#0080FF")
buttons   = [btnBTC,btnEOS]
MIXIN_WS_API.sendAppButtonGroup(ws, conversationId, userId, buttons)
```
Here show clients two buttons for EOS and BTC, you can add more buttons in this way.

#### APP_CARD
Maybe a group of buttons too simple for you, try a pay link which show a icon: APP_CARD.
```python
print('send a link APP_CARD')
MIXIN_WS_API.sendAppCard(ws, conversationId, mixin_config.client_id,
                        BTC_ASSET_ID, "0.0001",
                        "https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128",
                        "Pay BTC 0.0001","topay")
```
![APP_CARD](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app_card.jpg)

[Full source code](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app.py)
