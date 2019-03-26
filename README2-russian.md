# Python Bitcoin Руководство для Mixin Network: получение и отправка Bitcoin в Mixin Messenger
![cover](https://github.com/wenewzhang/mixin_labs-python-bot/raw/master/Bitcoin_python.jpg)
В [предыдущем руководстве](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README_russian.md), мы создали наше первое приложение, где пользователь отправляет "Hello,world!", а бот отвечает таким же сообщением.



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
Запустите **python app.py** в папке проекта.
```bash
cd mixin_labs-python-bot
source ./bin/activate
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app.py
ws open
-------json object begin---------
{'id': 'fd6ce766-331a-11e9-92a9-20c9d08850cd', 'action': 'LIST_PENDING_MESSAGES'}
-------json object end---------
```
Разработчик может отправить Bitcoin своим ботам в панели сообщения. Бот получает Bitcoin и отправляет назад немедленно.
![передача и токены](https://github.com/wenewzhang/mixin_network-nodejs-bot2/raw/master/transfer-any-tokens.jpg)

Пользователь может оплатить 0.001 Bitcoin боту одним нажатием кнопки и 0.001 BTC будет возвращено в 1 секунду. Фактически, таким образом пользователь может оплачивать любым токеном.
![ссылка на оплату](https://github.com/wenewzhang/mixin_network-nodejs-bot2/raw/master/Pay_and_refund_quickly.jpg)

## Итоговый исходный код
```python
elif categoryindata == "SYSTEM_ACCOUNT_SNAPSHOT":
    rdJs = json.loads(realData)
    if ( float(rdJs["amount"]) > 0 ):
        mixin_api.transferTo(userId, rdJs["asset_id"], rdJs["amount"], "")
```
* rdJs["amount"] отрицательно, если бот отправил Bitcoin пользователю успешно.
* rdJs["amount"] положительно, если бот получил Bitcoin от пользователя.
Вызывайте mixin_api.transferTo для возврата монет обратно пользователю.

## Продвинутое использование
#### APP_BUTTON_GROUP
В некоторых сценариях использования, например:
Обмен монет предлагает услугу конвертации, которая меняет BTC на EOS, ETH, BCH  и т.п.
Вы хотите показать клиентам несколько ссылок на оплату с различным количеством, конструкция APP_BUTTON_GROUP может помочь в этом.
```python
print('send a link APP_BUTTON_GROUP')
btnBTC    = MIXIN_WS_API.packButton(mixin_config.client_id, BTC_ASSET_ID, "0.0001","BTC pay")
btnEOS    = MIXIN_WS_API.packButton(mixin_config.client_id, EOS_ASSET_ID, "0.01","EOS pay","#0080FF")
buttons   = [btnBTC,btnEOS]
MIXIN_WS_API.sendAppButtonGroup(ws, conversationId, userId, buttons)
```
Здесь клиентам показаны 2 кнопки для EOS и BTC, Вы можете добавить больше таким же способом.

#### APP_CARD
Может быть, группа кнопок слишком просто для Вас, в этом случае можно использовать ссылку оплаты, которая покажет иконку: APP_CARD.
```python
print('send a link APP_CARD')
MIXIN_WS_API.sendAppCard(ws, conversationId, mixin_config.client_id,
                        BTC_ASSET_ID, "0.0001",
                        "https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128",
                        "Pay BTC 0.0001","topay")
```
![APP_CARD](https://github.com/wenewzhang/mixin_labs-python-bot/raw/master/app_card.jpg)

[Полный исходный код](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app.py)
