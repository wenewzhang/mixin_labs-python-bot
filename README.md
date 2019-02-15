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

on Ubuntu, install python 3.7.2 from third apt source.

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
sudo ln -s /usr/bin/python3.7 /usr/bin/python3
```

Check the installation whether success, you need check python3 and python3-venv.
```bash
$python3 -V
Python 3.7.2
```
```bash
root@n2:~# python3 -m venv -h
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
