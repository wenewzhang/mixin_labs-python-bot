# Mixin Messenger application development tutorial in Python 3
This tutorial will let you know how to write a Mixin Messenger bot in Python 3. The bot can receive and response to user's message. User can pay Bitcoin to bot and bot can transfer Bitcoin to user immediately.

## Index
1. [Create bot and receive message from user](https://github.com/wenewzhang/mixin_labs-python-bot#create-bot-and-receive-message-from-user)
2. [Receive and send Bitcoin](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2.md)

## Create bot and receive message from user
You will create a bot in Mixin Messenger to receive user message after read the chapter.


### Python 3 setup:
This tutorial is written in Python 3.7.2 So you need to install Python 3.7.2 or above.

on macOS
```bash
brew upgrade
brew install python@3
```

on Ubuntu, build python 3.7.2 from source.

###
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```

When prompted press Enter to continue:
```bash
Press [ENTER] to continue or Ctrl-c to cancel adding it.
```

```bash
sudo apt update
sudo apt install python3.7 python3.7-venv
```

Check the installation whether success.

on macOS
```bash
python3 -V
```

on Ubuntu
```bash
python3.7 -V
```


pip3 install flask requests Crypto pycryptodomex websocket-client pyjwt
```

apt install python3-pip

```bash
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_ws_api.py
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_api.py
wget https://github.com/includeleec/mixin-python3-sdk/raw/master/mixin_config.py
```

ubuntu python3.7:

apt install python3 python3-venv

https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/

before build 3.7.2 install libffi-dev
apt-get install libffi-dev

python3 env
```bash
cd mixin_labs-python-bot
python3 -m venv ./
source ./bin/activate
pip install --upgrade pip
pip install -r requirements2.txt
python3 ws_test.py

```
