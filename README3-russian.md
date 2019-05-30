# Руководство Python Bitcoin для Mixin Network: Создание кошелька Bitcoin
![cover](https://github.com/wenewzhang/mixin_labs-python-bot/raw/master/Bitcoin_python.jpg)
Мы уже создали бота в [echo message](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README.md) и [echo Bitcoin](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2.md).

# Что мы изучим в данном руководстве
1. Как создать кошелек Bitcoin
2. Как прочитать баланс Bitcoin
3. Как отправить Bitcoin с нулевой комиссией и получить подтверждение за 1 секунду
4. Как отправить Bitcoin на другой кошелек


Требования: Вы должны иметь аккаунт в Mixin Network. Создание аккаунта может быть выполнено одной командой:

```python
  userInfo = mixinApiBotInstance.createUser(session_key.decode(),"Tom Bot")
```
Функция в Python SDK создает пару RSA ключей автоматически, затем вызывает Mixin Network для создания аккаунта. По завершении функция возвращает всю информацию об аккаунте.

```python
// Интерфейс Create User включает всю информацию об аккаунте
userInfo.get("data").get("pin_token"),
userInfo.get("data").get("session_id"),
userInfo.get("data").get("user_id"),
```

Результат команды createUser:
```python
{'data': {'type': 'user', 'user_id': '2f25b669-15e7-392c-a1d5-fe7ba43bdf37', 'identity_number': '0',
'full_name': 'Tom Bot', 'avatar_url': '', 'relationship': '', 'mute_until': '0001-01-01T00:00:00Z',
'created_at': '2019-02-22T06:23:41.754573722Z', 'is_verified': False,
'session_id': '284c7b39-3284-4cf6-9354-87df30ec7d57', 'phone': '',
'pin_token':'g4upUgBXa8ATk7yxL6B94HgI4GV4sG4t8Wyn6uTu2Q2scH11UMQ5bYDb6Md+3LRQqRjEdRFcLlHijXGBihRweTaKTZjHQqolWbZcffesVIias6WppV/QMu4TzXCuKa5xpj3uhjL+yPyfWTLGUaVJTJN9n7PQmHSIUBXrovbfodk=',
'invitation_code': '', 'code_id': '', 'code_url': '', 'has_pin': False,
'receive_message_source': 'EVERYBODY', 'accept_conversation_source': 'EVERYBODY'}}
```

Теперь Вам нужно внимательно хранить информацию аккаунта. Вам нужна эта информация, чтобы прочитать баланс и другое содержимое.
### Создание кошелька Bitcoin для аккаунта Mixin Network
Кошелек Bitcoin не создается автоматически при создании аккаунта в сети Mixin Network. Прочитайте данные актива Bitcoin один раз для генерации кошелька Bitcoin.
```python
def readAssetAddress(asset_id,isBTC = True):
    with open('new_users.csv', newline='') as csvfile:
        reader  = csv.reader(csvfile)
        for row in reader:
            pin         = row.pop()
            userid      = row.pop()
            session_id  = row.pop()
            pin_token   = row.pop()
            private_key = row.pop()
            mixinApiNewUserInstance = generateMixinAPI(private_key,
                                                        pin_token,
                                                        session_id,
                                                        userid,
                                                        pin,"")
            btcInfo = mixinApiNewUserInstance.getAsset(asset_id)
            print(btcInfo)
            if isBTC:
                print("Account %s \'s Bitcoin wallet address is %s  " %(userid,btcInfo.get("data").get("public_key")))
            else:
                print("Account %s \'s EOS account name is %s, wallet address is %s  " %(userid,
                                                                        btcInfo.get("data").get("account_name"),
                                                                        btcInfo.get("data").get("account_tag")))
```
Вы можете найти информацию об активе Bitcoin в аккаунте. Публичный ключ - это Bitcoin-адрес. Полный ответ при чтении данных об активах Bitcoin у аккаунта:
```python
{'data': {'type': 'asset', 'asset_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'chain_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa', 'symbol': 'BTC', 'name': 'Bitcoin',
'icon_url': 'https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128', 'balance': '0',
'public_key': '1AYAMaRi3j5rXoFLmhJBFxvUEgGt8zeF4k', 'account_name': '', 'account_tag': '',
'price_btc': '1', 'price_usd': '3979.12975801', 'change_btc': '0',
'change_usd': '-0.0018925165548280905', 'asset_key': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'confirmations': 12, 'capitalization': 0}}
```
API обеспечивает получение много другой информации об активе Bitcoin.
* Адрес кошелька:[public_key]
* Логотип: [icon_url]
* Имя актива:[name]
* uuid актива в Mixin network: [asset_key]
* Цена в USD из Coinmarketcap.com: [price_usd]
* Последний подтвержденный блок перед размещением депозита в Mixin network:[confirmations]


### Приватный ключ?
Где приватный ключ кошелька Bitcoin? Приватный ключ защищен муультиподписью внутри Mixin Network, так что он невидим для пользователя. Актив Bitcoin может быть выведен на другой адрес, только если пользователь обеспечит корректную подпись приватного RSA ключа, PIN код and ключ Session.

### Не только Bitcoin, но также и Ethereum, EOS
Аккаунт содержит не только кошелек Bitcoin, но и кошелек Ethereum, EOS, etc. Полный  [список](https://mixin.one/network/chains) поддерживаемых блокчейнов. Все ERC20 токены and EOS токены также поддерживаются аккаунтом.

Создать кошелек другого актива также просто, как и создание Bitcoin кошелька: просто прочитать его данные.
#### Mixin Network поддерживает криптовалюты (2019-02-19):

|crypto |uuid in Mixin Network
|---|---
|EOS|6cfe566e-4aad-470b-8c9a-2fd35b49c68d
|CNB|965e5c6e-434c-3fa9-b780-c50f43cd955c
|BTC|c6d0c728-2624-429b-8e0d-d9d19b6592fa
|ETC|2204c1ee-0ea2-4add-bb9a-b3719cfff93a
|XRP|23dfb5a5-5d7b-48b6-905f-3970e3176e27
|XEM|27921032-f73e-434e-955f-43d55672ee31
|ETH|43d61dcd-e413-450d-80b8-101d5e903357
|DASH|6472e7e3-75fd-48b6-b1dc-28d294ee1476
|DOGE|6770a1e5-6086-44d5-b60f-545f9d9e8ffd
|LTC|76c802a2-7c88-447f-a93e-c29c9e5dd9c8
|SC|990c4c29-57e9-48f6-9819-7d986ea44985
|ZEN|a2c5d22b-62a2-4c13-b3f0-013290dbac60
|ZEC|c996abc9-d94e-4494-b1cf-2a3fd3ac5714
|BCH|fd11b6e3-0b87-41f1-a41f-f0e9b49e5bf0

Если Вы читаете адрес EOS, он будет состоять из двух частей: account_name и метка (account_tag). Когда Вы переводите EOS токены на Ваш аккаунт в Mixin network, Вы должны заполнить два параметра: account_name и memo. Содержимым memo и будет значение 'account_tag'.
Результат чтения актива EOS:
```python
{'data': {'type': 'asset', 'asset_id': '6cfe566e-4aad-470b-8c9a-2fd35b49c68d',
'chain_id': '6cfe566e-4aad-470b-8c9a-2fd35b49c68d',
'symbol': 'EOS', 'name': 'EOS',
'icon_url': 'https://images.mixin.one/a5dtG-IAg2IO0Zm4HxqJoQjfz-5nf1HWZ0teCyOnReMd3pmB8oEdSAXWvFHt2AJkJj5YgfyceTACjGmXnI-VyRo=s128',
'balance': '0', 'public_key': '',
'account_name': 'eoswithmixin', 'account_tag': '185b27f83d76dad3033ee437195aac11',
'price_btc': '0.00096903', 'price_usd': '3.8563221', 'change_btc': '0.00842757579765049',
'change_usd': '0.0066057628802373095', 'asset_key': 'eosio.token:EOS',
'confirmations': 64, 'capitalization': 0}}
```

### Размещение Bitcoin и чтение баланса
Теперь Вы можете внести Bitcoin на Ваш адрес.

Это может быть слишком дорого в рамках данного руководства. Есть бесплатное и очень быстрое решение для внесения Bitcoin: добавьте этот адрес в Ваш аккаунт Mixin messenger как адрес для вывода and выведите небольшое количество Bitcoin из Вашего аккаунта на указанный адрес. Это бесплатно и будет быстро подтверждено, потому что оба адреса будут в Mixin Network.

Теперь Вы можете прочитать баланс Bitcoin аккаунта.
```python
btcInfo = mixinApiNewUserInstance.getAsset("c6d0c728-2624-429b-8e0d-d9d19b6592fa");
print(btcInfo);
```
### Отправка Bitcoin внутри Mixin Network, чтобы убедиться в быстрых подтверждениях и нулевой комиссии
Любая транзакция между аккаунтами Mixin Network бесплатна и подтверждается 1 секунду.

#### Отправка Bitcoin другому аккаунту Mixin Network
Мы можем отправлять Bitcoin нашему боту через Mixin Messenger и затем передавать Bitcoin от бота новому пользователю.

```python
mixinApiBotInstance = MIXIN_API(mixin_config)
//$user_info["user_id"] создается при помощи команды create user;
mixinApiBotInstance.transferTo(userid, BTC_ASSET_ID, AMOUNT, "")
```

Прочитаем баланс Bitcoin у бота для подтверждения транзакции.
Предупреждение: **mixinApiNewUserInstance** используется для НОВЫХ пользователей!
```python
def readAssetBalance(asset_id):
    with open('new_users.csv', newline='') as csvfile:
        reader  = csv.reader(csvfile)
        for row in reader:
            pin         = row.pop()
            userid      = row.pop()
            session_id  = row.pop()
            pin_token   = row.pop()
            private_key = row.pop()
            mixinApiNewUserInstance = generateMixinAPI(private_key,
                                                        pin_token,
                                                        session_id,
                                                        userid,
                                                        pin,"")
            btcInfo = mixinApiNewUserInstance.getAsset(asset_id)
            print("Account %s \'s balance is %s  " %(userid,btcInfo.get("data").get("balance")))
```

### Отправка Bitcoin на другие Bitcoin биржу или кошелек
Если Вы хотите отправить Bitcoin на другие биржу или кошелек, Вы должны узнать адрес назначения, затем добавить этот адрес в список адресов для вывода в аккаунте Mixin Network.

Подготовительные задачи: добавить адрес для вывода и узнать комиссию за вывод Bitcoin

#### Добавление адреса назначения в список адресов для вывода
Вызываем createAddress, ID адреса будет возвращено как результат API и вскоре потребуется.
```python
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
BTC_WALLET_ADDR = "14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C";
btcInfo = mixinApiBotInstance.createAddress(BTC_ASSET_ID, BTC_WALLET_ADDR,"BTC","","")
print(btcInfo)
```
Значение **14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C** это адрес кошелька Bitcoin, результат выполнения указан ниже, он содержит ID адреса вывода и значение комиссии 0.0034802 BTC.
```python
{'data': {'type': 'address', 'address_id': '47998e2f-2761-45ce-9a6c-6f167b20c78b',
'asset_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'public_key': '14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C', 'label': 'BTC',
'account_name': '', 'account_tag': '',
'fee': '0.0034802', 'reserve': '0', 'dust': '0.0001',
'updated_at': '2019-02-26T00:03:05.028140704Z'}}
```
Если Вы хотите создать адрес EOS, вызов будет выглядеть так:
```python
EOS_ASSET_ID     = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
EOS_WALLET_ADDR  = "3e2f70914c8e8abbf60040207c8aae62";
EOS_ACCOUNT_NAME = "eoswithmixin";
eosInfo = mixinApiBotInstance.createAddress(EOS_ASSET_ID, "","",EOS_ACCOUNT_NAME,EOS_WALLET_ADDR)
print(eosInfo)
```
#### Узнать комиссию на вывод можно в любое время
```python
addr_id = btcInfo.get("data").get("address_id")
addrInfo = mixinApiBotInstance.getAddress(addr_id)
print(addrInfo)
```

#### Отправка Bitcoin на адрес назначения
Подтверждаем запрос вывода к Mixin Network, the btcInfo.get("data").get("address_id") - это id адреса, который возвращается функцией createAddress
```python
  mixinApiBotInstance.withdrawals(btcInfo.get("data").get("address_id"),AMOUNT,"")
```
#### Проверяем транзакцию в блокчейн эксплорере

[Полный исходный код](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/call_apis.py)
