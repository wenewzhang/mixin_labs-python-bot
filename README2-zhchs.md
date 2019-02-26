
在 [上一篇教程中](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README-zhchs.md), 我们创建了自动回复消息的机器人,当用户发送消息"Hello,World!"时，机器人会自动回复同一条消息!

# 第二课: 机器人接受比特币并立即退还用户
按本篇教程后学习后完成后，你的机器人将会接受用户发送过来的加密货币，然后立即转回用户。
完整代码如下：
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
在项目目录下，执行 **python app.py**
```bash
cd mixin_labs-python-bot
source ./bin/activate
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app.py
ws open
-------json object begin---------
{'id': 'fd6ce766-331a-11e9-92a9-20c9d08850cd', 'action': 'LIST_PENDING_MESSAGES'}
-------json object end---------
```
开发者可以通过消息面板，给机器人转比特币，当机器人收到比特币后，马上返还给用户！
![transfer and tokens](https://github.com/wenewzhang/mixin_network-nodejs-bot2/blob/master/transfer-any-tokens.jpg)

事实上，用户可以发送任意的币种给机器人，它都能马上返还！
![pay-link](https://github.com/wenewzhang/mixin_network-nodejs-bot2/blob/master/Pay_and_refund_quickly.jpg)

## 源代码解释
```python
elif categoryindata == "SYSTEM_ACCOUNT_SNAPSHOT":
    rdJs = json.loads(realData)
    if ( float(rdJs["amount"]) > 0 ):
        mixin_api.transferTo(userId, rdJs["asset_id"], rdJs["amount"], "")
```
如果机器人收到币，rdJs["amount"] 大于零；如果机器人支付币给用户，接收到的消息是一样的，唯一不同的是,rdJs["amount"]是一个负数.
最后一步，调用SDK的 mixin_api.transferTo 将币返还用户！

## 高级用法
#### APP_BUTTON_GROUP
在一些应用场景，比如：有一个交易所想提供换币服务，将比特币换成以太坊，EOS,比特币现金等,
你想显示给用户一组按钮，它们分别代表不同的币与不同的数量,APP_BUTTON_GROUP可以帮你做到这一点.
```python
print('send a link APP_BUTTON_GROUP')
btnBTC    = MIXIN_WS_API.packButton(mixin_config.client_id, BTC_ASSET_ID, "0.0001","BTC pay")
btnEOS    = MIXIN_WS_API.packButton(mixin_config.client_id, EOS_ASSET_ID, "0.01","EOS pay","#0080FF")
buttons   = [btnBTC,btnEOS]
MIXIN_WS_API.sendAppButtonGroup(ws, conversationId, userId, buttons)
```
这里演示给用户BTC与EOS两种，你还可以增加更多的按钮.

#### APP_CARD
如果你觉得一组按钮太单调了，可以试一下APP_CARD,它提供一个图标的链接
```python
print('send a link APP_CARD')
MIXIN_WS_API.sendAppCard(ws, conversationId, mixin_config.client_id,
                        BTC_ASSET_ID, "0.0001",
                        "https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128",
                        "Pay BTC 0.0001","topay")
```
![APP_CARD](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app_card.jpg)

[Full source code](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app.py)
