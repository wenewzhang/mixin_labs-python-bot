# Mixin Messenger application development tutorial in Python 3
This tutorial will let you know how to write a Mixin Messenger bot in Python 3. The bot can receive and response to user's message. User can pay Bitcoin to bot and bot can transfer Bitcoin to user immediately.

## Index
1. [Create bot and receive message from user](https://github.com/wenewzhang/mixin_labs-python-bot#create-bot-and-receive-message-from-user)
2. [Receive and send Bitcoin](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2.md)

## Create bot and receive message from user
You will create a bot in Mixin Messenger to receive user message after read the chapter.


## Python 3 installation:
This tutorial is written in Python 3.7.2 So you need to install Python 3.7.2 or above.

on macOS
```bash
brew upgrade
brew install python@3
```

on Ubuntu, install python 3.7.2 from the third apt source.
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```

When prompt like below, press Enter to continue:
```bash
Press [ENTER] to continue or Ctrl-c to cancel adding it.
```
Update the source and then install python3.7, python3.7-venv
```bash
sudo apt update
sudo apt install python3.7 python3.7-venv
sudo ln -s /usr/bin/python3.7 /usr/bin/python3
```

Check whether the installation is success, you need check both python3 and python3-venv.
```bash
$ python3 -V
Python 3.7.2
```

```bash
root@n2:~ python3 -m venv -h
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]
Creates virtual Python environments in one or more target directories.
positional arguments:
  ENV_DIR               A directory to create the environment in.

optional arguments:
  -h, --help            show this help message and exit
  --system-site-packages
                        Give the virtual environment access to the system
                        site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks
                        are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when
                        symlinks are the default for the platform.
  --clear               Delete the contents of the environment directory if it
                        already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version
                        of Python, assuming Python has been upgraded in-place.
  --without-pip         Skips installing or upgrading pip in the virtual
                        environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this
                        environment.

Once an environment has been created, you may wish to activate it, e.g. by
sourcing an activate script in its bin directory
```

## Create mixin_labs-python-bot project

You need create project directory, make it as a python's “virtual environment”, and then install the required packages.
```bash
mkdir mixin_labs-python-bot
cd mixin_labs-python-bot
python3 -m venv ./
```

After **python3 -m venv** command finished,  the project directory has data like below:
```bash
wenewzha:mixin_labs-python-bot wenewzhang$ ls
bin		include		lib		pyvenv.cfg
```

Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory.
```bash
wenewzha:mixin_labs-python-bot wenewzhang$ source ./bin/activate
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$
```
So that “python” or "pip" invoke from the virtual environment, and you can run installed scripts without having to use their full path.

## Install required packages by "virtual environment"

Create the requirement list.
> requirements.txt
```txt
cryptography==2.4.2
pycparser==2.19
pycryptodome==3.7.2
PyJWT==1.7.1
python-dateutil==2.7.5
PyYAML==3.13
requests==2.21.0
websocket-client==0.54.0
```
Use pip to upgrade pip itself, and install required packages.
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Download the mixin-network api.
```bash
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_ws_api.py
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_api.py
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_config.py
```

## Hello, world!

### Create you first app in developer dashboard
Create an app by following [tutorial](https://mixin-network.gitbook.io/mixin-network/mixin-messenger-app/create-bot-account).

### Generate parameter for your app
Remember to [generate parameter](https://mixin-network.gitbook.io/mixin-network/mixin-messenger-app/create-bot-account#generate-secure-parameter-for-your-app)
and write down required information, they are required in config.php file soon.

![mixin_network-keys](https://github.com/wenewzhang/mixin_labs-php-bot/blob/master/mixin_network-keys.jpg)
In the folder, create a file: mixin_config.py. Copy the following content into it.
> mixin_config.py
```python
client_id= 'ed882a39-0b0c-4413-bbd9-221cdeee56bf'
client_secret = '8d7ec7b9c8261b6c7bd6309210496ca4b72bce9efc7e49be14a428ce49ff7202'


pay_pin = '599509'
pay_session_id = 'bd53b6a4-e79a-49e5-ad04-36da518354f6'
pin_token = "nVREh0/Ys9vzNFCQT2+PKcDN2OYAUSH8CidwHqDQLOCvokE7o6wtvLypjW9iks/RsnBM6N4SPF/P3bBW254YHGuDZXhitDEWOGkXs7v8BxMQxf+9454qTkMSpR9xbjAzgMXnSyHrNVoBtsc/Y+NvemB3VxPfsCOFHasiMqAa5DU="


private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCnaoO1SdPxggEpAIUdM/8Ll4FOqlXK7vwURHr4FFi6hnQ1I79g
pZSlJdzjr24WcIuNi6kVdXVIpyzZJGXS2I72dpGs5h1jKxL8AWIUVL2axZXqTJNi
c4wj6GJ4gDRP2U9I9gae+S/frM6KP8TioV0OcbmrlfrwI0OElLH3363y1wIDAQAB
AoGAduaGLi4F8cMkMculvqzcGY57jrQZBGyg6YANWb2Rmr+9LrR5yhkvLe9rJuXE
KPm7k0a6SnxGVNguWPWpv4qAVVGAJ0eb8ETXTRO20HlKmcbxfFdDtHBDV3QufNa1
h3mNEsqWDNCDdAm7p/EZwfG2F9+nmeXLfip7R1I72qbK0wkCQQDiJR6NEGVwbj8H
K8kRpzY1D9lPqp1ZMrma5AFYGZIb5voTxLjRpYdxQJHi7CCdE1zgqJOXvA3jj/io
f7bMIJY7AkEAvYSSC5H+fUKAjyjeCTGJBBKoPDsq+aALAYLWf77sGXE9BBmhhY0l
iwmbj8X6/qZtQ0yEzdT/OSdiYL86CcrgFQJBALz/sMzMSzrvqJVhrqWmTdOC72d5
fA+0KRKeQ9FRbZ8MJyymWKA96zhncoVoOsmMCS9pNBC4BhONm4+XTTrEcUkCQQCo
DWB8Bg/G/yuExtZtDJHVHL41+rmW9UYNJvoR+TjfLrzOX/QMuyapbfGVwhdZrDaD
UN0KsG9JPRVNeQR8HnwpAkACrr9cNp1H1bytHG9a6L+5cVHkRhqqEYWVO41MhgZF
5bIKx5OXCJB2VwY7fjFet2KxTHGfEZt/khjFNZzVX7lN
-----END RSA PRIVATE KEY-----"""
```
Replace the value with YOUR APP  client_id, client_secret, and the pay_pin, pin token, pay_session_id, private key you have already generated them in dashboard.

Create an app-mini.py file, fill it by the content below:
> app-mini.py
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
```

Run the app-mini.py, DO NOT forget active the python "virtual environment" before!"
```bash
python app.php
```
If everything is ok, the following content will be display.
```bash
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app-mini.py
ws open
-------json object begin---------
{'id': '1c798948-30eb-11e9-a20e-20c9d08850cd', 'action': 'LIST_PENDING_MESSAGES'}
-------json object end---------
```

In [Mixin Messenger](https://mixin.one/),add the bot as your friend,(for example, this bot id is 7000101639) and then send any text!

![mixin_messenger](https://github.com/wenewzhang/mixin_labs-php-bot/blob/master/helloworld.jpeg)

### Source code explanation
The WebSocket providing full-duplex communication channels over a single TCP connection, It is a persistence connection, so create loop for it.
```python
if __name__ == "__main__":

    mixin_api = MIXIN_API(mixin_config)
    mixin_ws = MIXIN_WS_API(on_message=on_message)
    mixin_ws.run()
```

Send the READ message to the server let it knows this message has already been read. If you don't send it,  the bot will receive the duplicated message again after the bot connect to server again!

```python
        MIXIN_WS_API.replayMessage(ws, msgid)
```
The bot reply any TEXT message unchanged.
```python
if categoryindata == "PLAIN_TEXT":
    realData = realData.decode('utf-8')
    print("dataindata",realData)
    MIXIN_WS_API.sendUserText(ws, conversationId, userId, realData)    
```

Not only text messages, images and other type message can be received. You can find message details in [Here](https://developers.mixin.one/api/beta-mixin-message/websocket-messages/).

### End
Now your bot is running. You can try your idea now, enjoy!

A full code is [here](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app-mini.py)
