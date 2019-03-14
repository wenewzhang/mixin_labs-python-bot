# Руководство Python Bitcoin для Mixin Network
![cover](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/Bitcoin_python.jpg)
В этом руководстве будет создан бот для мессенджера Mixin. Бот написан на языке python и позволяет пересылать сообщения и Bitcoin от пользователя.

Полный список сетевых ресурсов Mixin [список](https://github.com/awesome-mixin-network/index_of_Mixin_Network_resource)

## Что Вы изучите в этом руководстве
1. [Как создать бота для мессенджера Mixin и ответить на сообщение пользователя](https://github.com/wenewzhang/mixin_labs-python-bot#create-bot-and-receive-message-from-user)
2. [Как получить и отправить Bitcoin в мессенджере Mixin](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2.md)
3. [Как создать кошелек Bitcoin при помощи Mixin Network API](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README3.md)
## Как создать бота для мессенджера Mixin и ответить на сообщение пользователя
## Установка Python 3:
Это руководство написано для Python 3.7.2, поэтому Вы должны установить Python 3.7.2 или более новый.

macOS
```bash
brew upgrade
brew install python@3
```

Ubuntu, установка python 3.7.2 из сторонних репозитариев.
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```

Нажмите Enter для продолжения
```bash
Press [ENTER] to continue or Ctrl-c to cancel adding it.
```
Обновите список репозитариев, затем установите python3.7, python3.7-venv
```bash
sudo apt update
sudo apt install python3.7 python3.7-venv
sudo ln -s /usr/bin/python3.7 /usr/bin/python3
```

Проверьте, что оба компонента python3 and python3-venv установлены
```bash
$ python3 -V
Python 3.7.2
```

```bash
root@n2:~ python3 -m venv -h
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]
Создает виртуальное окружение Python в одной или нескольких целевых папках:
Creates virtual Python environments in one or more target directories.
необходимый аргумент:
  ENV_DIR               Папка, для которой создается окружение.

дополнительные аргументы:
  -h, --help            показывает этот хелп и закрывает окно
  --system-site-packages
                        Дает виртуальному окружению доступ к папке с системными пакетами
  --symlinks            Пытаться использовать символические ссылки, а не копии,
                        даже когда симлинки не используются платформой "по умолчанию".
  --copies              Пытаться использовать копии, на не символические ссылки,
                        даже если символические ссылки используют платформой "по умолчанию".
  --clear               Удалить содержимое папки окружения, если она существует,
                        перед созданием окружения.
  --upgrade             Обновить папку окружения для использования этой версии
                        Python, при условии что он был обновлен "на месте".
  --without-pip         Пропустить или обновить установку pip в виртуальном
                        окружении (pip загружается по умолчанию)
  --prompt PROMPT       Предоставляет альтернативный префикс приглашения для
                        этой виртуальной среды.

Как только окружение создано, Вы можете активировать его, например,
путем поиска сценария активации в его папке bin.
```

## Создаем проект mixin_labs-python-bot

Вы должны создать папку проекта, сделать ее как виртуальное окружение python и установить необходимые пакеты.
```bash
mkdir mixin_labs-python-bot
cd mixin_labs-python-bot
python3 -m venv ./
```

Запускаем **python3 -m venv** , следующие файл и папка будут созданы:
```bash
wenewzha:mixin_labs-python-bot wenewzhang$ ls
bin		include		lib		pyvenv.cfg
```

Как только виртуальное окружение создано, его можно "активировать", используя скрипт в папке bin виртуального окружения.
```bash
wenewzha:mixin_labs-python-bot wenewzhang$ source ./bin/activate
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$
```
Так как “python” или "pip" вызываются из виртуального окружения, Вы можете запускать установленные скрипты без указания их полного пути.

## Установка необходимых пакетов с помощью "виртуального окружения"

Создайте список требуемого
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
Используйте "pip" для обновления самомго себя и установите требующиеся пакеты из списка
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Загрузка mixin-network api
```bash
wget https://github.com/wenewzhang/mixin-python3-sdk/raw/master/mixin_ws_api.py
wget https://github.com/wenewzhang/mixin-python3-sdk/raw/master/mixin_api.py
wget https://github.com/wenewzhang/mixin-python3-sdk/raw/master/mixin_config.py
```

## Hello, world при помощи Python

### Создайте свое первое приложение в дашборде разработчика Mixin Network
Вам необходимо создать  приложение в дашборде. Это [руководство](https://mixin-network.gitbook.io/mixin-network/mixin-messenger-app/create-bot-account) может помочь Вам.

### Генерация параметров приложения в дашборде
После создания приложения в дашборде Вы должны [генерировать параметры](https://mixin-network.gitbook.io/mixin-network/mixin-messenger-app/create-bot-account#generate-secure-parameter-for-your-app) и написать необходимое содержимое, это содержимое будет записано в файл mixin_config.py.

![mixin_network-keys](https://github.com/wenewzhang/mixin_labs-php-bot/blob/master/mixin_network-keys.jpg)
В папке создайте файл: mixin_config.py. Скопируйте следующее содержимое в этот файл.
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
Замените значеня содержимым, сгенерированным в дашборде. Создайте файл app-mini.py и заполните его содержимое текстом ниже:
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

Запустите app-mini.py, НЕ ЗАБУДЬТЕ активировать перед этим  "виртуальное окружение" python"
```bash
cd mixin_labs-python-bot
wenewzha:mixin_labs-python-bot wenewzhang$ source ./bin/activate
```
```bash
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app-mini.py
...
```
Если в консоли выводится следующее сообщение, значит, все прошло успешно.
```bash
(mixin_labs-python-bot) wenewzha:mixin_labs-python-bot wenewzhang$ python app-mini.py
ws open
-------json object begin---------
{'id': '1c798948-30eb-11e9-a20e-20c9d08850cd', 'action': 'LIST_PENDING_MESSAGES'}
-------json object end---------
```

Добавьте бота(например, id этого бота 7000101639) как Вашего друга в [Mixin Messenger](https://mixin.one/messenger) и отправьте ему сообщение.

![mixin_messenger](https://github.com/wenewzhang/mixin_labs-php-bot/blob/master/helloworld.jpeg)

### Объяснение исходного кода
Следующий код создает websocket клиент.
```python
if __name__ == "__main__":

    mixin_api = MIXIN_API(mixin_config)
    mixin_ws = MIXIN_WS_API(on_message=on_message)
    mixin_ws.run()
```

Отправьте сообщение операции READ на сервер, чтобы он знал, что сообщение прочитано. Иначе бот получит повторное сообщение, когда он подключится к серверу, если не будет отметки о прочтении.

```python
        MIXIN_WS_API.replayMessage(ws, msgid)
```
Бот повторяет любой текст от пользователя
```python
if categoryindata == "PLAIN_TEXT":
    realData = realData.decode('utf-8')
    print("dataindata",realData)
    MIXIN_WS_API.sendUserText(ws, conversationId, userId, realData)    
```

Не только текст, но и картинки, и другие типы сообщений могут передаваться Вашему боту. Вы можете узнать подробнее [тут](https://developers.mixin.one/api/beta-mixin-message/websocket-messages/) о сообщениях Messenger.

### Окончание
Теперь Ваш бот работает. И Вы можете взломать это.

Полный код [здесь](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/app-mini.py)
