# 基于Mixin Network的Python比特币开发教程
![cover](https://github.com/wenewzhang/mixin_labs-python-bot/raw/master/Bitcoin_python.jpg)
[Mixin Network](https://mixin.one) 是一个免费的 极速的端对端加密数字货币交易系统.
在本章中，你可以按教程在Mixin Messenger中创建一个bot来接收用户消息, 学到如何给机器人转**比特币** 或者 让机器人给你转**比特币**.

[Mixin Network的开发资源汇编](https://github.com/awesome-mixin-network/index_of_Mixin_Network_resource)

## 课程简介
1. [创建一个接受消息的机器人](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README-zhchs.md)
2. [机器人接受比特币并立即退还用户](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2-zhchs.md)
3. [创建比特币钱包](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2-zhchs.md)

## 创建一个接受消息的机器人

通过本教程，你将学会如何用PHP创建一个机器人APP,让它能接受消息.

## Python 3 安装:
本教程基于Python 3.7.2, 所以你需要安装Python 3.7.2 或 以上的版本.

on macOS
```bash
brew upgrade
brew install python@3
```

on Ubuntu, 从第三方的APT源中安装.
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```

当出现下面的提示时，按"回车"继续.
```bash
Press [ENTER] to continue or Ctrl-c to cancel adding it.
```
重新更新一次apt源, 再安装python3.7, python3.7-venv
```bash
sudo apt update
sudo apt install python3.7 python3.7-venv
sudo ln -s /usr/bin/python3.7 /usr/bin/python3
```
检查安装是否成功了，需要检查python3与python3-venv, 正确的提示如下:
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

## 创建 mixin_labs-python-bot 项目

你首先需要创建项目目录，初始化"虚拟环境",然后安装需要的软件包.
```bash
mkdir mixin_labs-python-bot
cd mixin_labs-python-bot
python3 -m venv ./
```

在 **python3 -m venv** 指令完成之后， 项目目录如下：
```bash
wenewzha:mixin_labs-python-bot wenewzhang$ ls
bin		include		lib		pyvenv.cfg
```

当"虚拟环境"创建成功后，需要激活它, 通过执行bin目录下相应的activate文件完成.
```bash
wenewzha:mixin_labs-python-bot wenewzhang$ source ./bin/activate
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$
```
成功激活后，可以直接执行python或pip了，这时，不再需要输入他们的完整路径了.

## 在"虚拟环境"里安装必需的包

创建一个必需包的list
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
通过pip升级pip包本身, 并安装必需包.
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 下载 Mixin Network的python 3的API
```bash
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_ws_api.py
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_api.py
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_config.py
```

## 你好，世界!

### 创建第一个机器人APP
按下面的提示，到mixin.one创建一个APP[tutorial](https://mixin-network.gitbook.io/mixin-network/mixin-messenger-app/create-bot-account).

### 生成相应的参数
记下这些[生成的参数](https://mixin-network.gitbook.io/mixin-network/mixin-messenger-app/create-bot-account#generate-secure-parameter-for-your-app)
它们将用于mixin_config.py中.

![mixin_network-keys](https://github.com/wenewzhang/mixin_labs-php-bot/raw/master/mixin_network-keys.jpg)
在项目目录下，创建mixin_config.py,将生成的参数，替换成你的！

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
需要替换的参数包括： client_id, client_secret,  pay_pin, pin_token, pay_session_id, private key.

创建 app-mini.py 文件, 内容如下:
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

运行 app-mini.py, 记得要先激活“虚拟环境”哦!
```bash
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app-mini.py
...
```
如果一切正常，将会有如下提示：
```bash
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app-mini.py
ws open
-------json object begin---------
{'id': '1c798948-30eb-11e9-a20e-20c9d08850cd', 'action': 'LIST_PENDING_MESSAGES'}
-------json object end---------
```

在手机安装 [Mixin Messenger](https://mixin.one/),增加机器人为好友,(比如这个机器人是7000101639) 然后发送消息给它,效果如下!

![mixin_messenger](https://github.com/wenewzhang/mixin_labs-php-bot/raw/master/helloworld.jpeg)


## 源代码解释
WebSocket是建立在TCP基础之上的全双工通讯方式，我们需要建立一个loop循环来维持通迅。

```python
if __name__ == "__main__":

    mixin_api = MIXIN_API(mixin_config)
    mixin_ws = MIXIN_WS_API(on_message=on_message)
    mixin_ws.run()
```

每接收到一个消息，需要按消息编号(message_id)给服务器回复一个"已读"的消息,避免服务器在机器人重新登入后，再次发送处理过的消息！

```python
        MIXIN_WS_API.replayMessage(ws, msgid)
```
机器人程序完整回复用户的信息
```python
if categoryindata == "PLAIN_TEXT":
    realData = realData.decode('utf-8')
    print("dataindata",realData)
    MIXIN_WS_API.sendUserText(ws, conversationId, userId, realData)    
```
Mixin Messenger支持的消息类型很多，具体可到下面链接查看:  [WebSocket消息类型](https://developers.mixin.one/api/beta-mixin-message/websocket-messages/).

### 完成
现在你的机器人APP运行起来了，你打算如何改造你的机器人呢？

完整的代码[在这儿](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app-mini.py)
