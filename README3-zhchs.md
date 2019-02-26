我们已经创建过一个[回复消息](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README.md)的机器人和一个能自动[支付比特币](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2.md)的机器人.

# 通过本教程的学习，你可以学到如下内容
1. 如何创建一个比特币钱包.
2. 如何读取比特币钱包的余额.
3. 如何支付比特币并即时确认.
4. 如何将Mixin Network的比特币提现到你的冷钱包或第三方交易所.

## 通过Mixin Network Python SDK创建一个比特币钱包
前期准备：你要有一个Mixin Network账户。如果没有账户，一行代码就能创建一个
```python
  userInfo = mixinApiBotInstance.createUser(session_key.decode(),"Tom Bot")
```
上面的语句会在本地创建一个RSA密钥对，然后调用Mixin Network来创建帐号，最后输出帐号信息.
```python
//Create User api include all account information
userInfo.get("data").get("pin_token"),
userInfo.get("data").get("session_id"),
userInfo.get("data").get("user_id"),
```

帐号创建成功后结果如下:

```python
{'data': {'type': 'user', 'user_id': '2f25b669-15e7-392c-a1d5-fe7ba43bdf37',
'identity_number': '0', 'full_name': 'Tom Bot', 'avatar_url': '',
'relationship': '', 'mute_until': '0001-01-01T00:00:00Z',
'created_at': '2019-02-22T06:23:41.754573722Z', 'is_verified': False,
'session_id': '284c7b39-3284-4cf6-9354-87df30ec7d57', 'phone': '',
'pin_token': 'g4upUgBXa8ATk7yxL6B94HgI4GV4sG4t8Wyn6uTu2Q2scH11UMQ5bYDb6Md+3LRQqRjEdRFcLlHijXGBihRweTaKTZjHQqolWbZcffesVIias6WppV/QMu4TzXCuKa5xpj3uhjL+yPyfWTLGUaVJTJN9n7PQmHSIUBXrovbfodk=',
'invitation_code': '', 'code_id': '', 'code_url': '', 'has_pin': False,
'receive_message_source': 'EVERYBODY', 'accept_conversation_source': 'EVERYBODY'}}
```

现在你需要小心保管好你的帐号信息，在读取该账户的比特币资产余额或者进行其他操作时，将需要用到这些信息.
### 给新建的帐号创建一个比特币钱包
新账号并不默认内置比特币钱包， 现在读一下比特币余额就可以创建一个比特币钱包。
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

创建的帐号的比特币资产详细信息如下，其中public key就是比特币的存币地址:
```python
{'data': {'type': 'asset', 'asset_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'chain_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'symbol': 'BTC', 'name': 'Bitcoin',
'icon_url': 'https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128',
'balance': '0',
'public_key': '12sJHR7HJPMt33KwSHyxQvYqGGUEbVGREf',
'account_name': '', 'account_tag': '', 'price_btc': '1',
'price_usd': '3879.88117389', 'change_btc': '0',
'change_usd': '0.017333475714793264',
'asset_key': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'confirmations': 12, 'capitalization': 0}}
Account a8cefb2e-cb93-338f-aba7-32a3a635ad02 's Bitcoin wallet address is 12sJHR7HJPMt33KwSHyxQvYqGGUEbVGREf
```

这个API能够提供若干与比特币有关的信息:
* 存币地址:[public_key]
* Logo: [icon_url]
* 资产名字:[name]
* 资产在Mixin Network的uuid: [asset_key]
* 对美元的价格(Coinmarketcap.com提供): [price_usd]
* 存币时确认的区块数量:[confirmations]


### 比特币私钥呢？
比特币的私钥呢？这个私钥被Mixin Network通过多重签名保护，所以对用户来说是不可见的,比特币资产的提现和转账都需要用户提供正确的的RSA签名,PIN代码与会话密钥才能完成.

### 不只是比特币，还有以太坊，EOS等
这个帐号不只支持比特币，还支持以太坊，EOS等, 完整的区块链支持[列表](https://mixin.one/network/chains). 这个账户同时也支持所有的 ERC20 代币与 EOS 代币.

创建其它的币的钱包与创建比特币钱包过程一样，读对应的资产余额就可以.

#### Mixin Network 当前支持的加密货币 (2019-02-19)

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

EOS的存币地址与其它的币有些不同，它由两部分组成： account_name and account tag, 如果你向Mixin Network存入EOS，你需要填两项数据： account name 是**eoswithmixin**,备注里输入你的account_tag,比如**0aa2b00fad2c69059ca1b50de2b45569**.

EOS的资产余额返回结果如下:
```python
{'data': {'type': 'asset', 'asset_id': '6cfe566e-4aad-470b-8c9a-2fd35b49c68d',
'chain_id': '6cfe566e-4aad-470b-8c9a-2fd35b49c68d',
'symbol': 'EOS', 'name': 'EOS',
'icon_url': 'https://images.mixin.one/a5dtG-IAg2IO0Zm4HxqJoQjfz-5nf1HWZ0teCyOnReMd3pmB8oEdSAXWvFHt2AJkJj5YgfyceTACjGmXnI-VyRo=s128',
'balance': '0', 'public_key': '',
'account_name': 'eoswithmixin', 'account_tag': '70dae97b661ca9f80cb0e6549feeba6c',
'price_btc': '0.00092392', 'price_usd': '3.58276497',
'change_btc': '-0.019294922814297986', 'change_usd': '-0.0033825963089133683',
'asset_key': 'eosio.token:EOS', 'confirmations': 64, 'capitalization': 0}}
Account a8cefb2e-cb93-338f-aba7-32a3a635ad02 's EOS account name is eoswithmixin, wallet address is 70dae97b661ca9f80cb0e6549feeba6c
```

### 存入比特币与读取比特币余额
现在，你可以向比特币的钱包存币了。

当然，在比特币网络里转币，手续费是相当贵的，费用的中位数在0.001BTC,按当前4000美元的价格，在4美元左右，有一个方便的办法，如果你有[Mixin Messenger](https://mixin.one/messenger)帐号，里面并且有比特币的话，可以直接提现比特币到新创建的帐号的比特币充值地址，它们在同一个Mixin Network网络内，手续费为0，而且1秒到账。

下面的代码，可以读取比特币钱包余额.
```python
btcInfo = mixinApiNewUserInstance.getAsset(asset_id)
print("Account %s \'s balance is %s  " %(userid,btcInfo.get("data").get("balance")))
```
### Mixin Network网内免手续费的，并且即时确认
任何币在Mixin Network内部的交易，都是无手续费的，并且立刻到账。
前期准备： 账户设置了PIN

对于新创建的帐号，我们通过updatePin来设置新PIN码, 代码如下：
```python
pinInfo = mixinApiNewUserInstance.updatePin(PIN,"")
print(pinInfo)
```
#### Mixin Network帐号之间的比特币支付
通过Mixin Messenger，我们可以先转比特币给机器人，然后让机器人转币给新用户。
```python
mixinApiNewUserInstance = generateMixinAPI(private_key,
                                            pin_token,
                                            session_id,
                                            userid,
                                            pin,"")
btcInfo = mixinApiBotInstance.transferTo(MASTER_UUID, BTC_ASSET_ID, AMOUNT, "")
print(btcInfo)
```

读取Bitcoin的余额，来确认比特币是不是转成功了！ 注意**$mixinSdkNew**是新用户的。
```python
btcInfo = mixinApiNewUserInstance.getAsset(asset_id)
print("Account %s \'s balance is %s  " %(userid,btcInfo.get("data").get("balance")))
```
### 如何将比特币存入你的冷钱包或者第三方交易所
如果你希望将币存入你的冷钱包或者第三方交易所, 先要得到冷钱包或者你在第三方交易所的钱包地址，然后将钱包地址提交到Mixin Network.

- **要点提示**: 提现是需要支付收续费的,准备好比特币包地址!

#### 增加目的钱包地址到Mixin Network
调用createAddress API, 将会返回一个address_id,下一步的提现操作会用到这个id。
```python
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
BTC_WALLET_ADDR = "14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C";
btcInfo = mixinApiBotInstance.createAddress(BTC_ASSET_ID, BTC_WALLET_ADDR,"BTC","","")
print(btcInfo)
```
 这里的 **14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C** 就是一个比特币钱包地址, 如下所示，提现费用是0.0034802 BTC, address_id  是"345855b5-56a5-4f3b-ba9e-d99601ef86c1".                                                   
 ```python
 {'data': {'type': 'address',
 'address_id': '47998e2f-2761-45ce-9a6c-6f167b20c78b',
 'asset_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
 'public_key': '14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C', 'label': 'BTC',
 'account_name': '', 'account_tag': '',
 'fee': '0.0034802', 'reserve': '0', 'dust': '0.0001',
 'updated_at': '2019-02-26T00:03:05.028140704Z'}}
 ```

如果你操作的是EOS, 示例代码如下：
 ```python
 EOS_ASSET_ID     = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
 EOS_WALLET_ADDR  = "3e2f70914c8e8abbf60040207c8aae62";
 EOS_ACCOUNT_NAME = "eoswithmixin";
 eosInfo = mixinApiBotInstance.createAddress(EOS_ASSET_ID, "","",EOS_ACCOUNT_NAME,EOS_WALLET_ADDR)
 print(eosInfo)
 ```

#### 创建提现地址成功后，你可以用readAddress读取最新的提现费。
```python
addr_id = btcInfo.get("data").get("address_id")
addrInfo = mixinApiBotInstance.getAddress(addr_id)
print(addrInfo)
```
#### 提交提现请求，Mixin Network会即时处理提现请求.
提交提现请求到Mixin Network, $btcInfo["address_id"]就是createAddress创建的。
```python
  mixinApiBotInstance.withdrawals(btcInfo.get("data").get("address_id"),AMOUNT,"")
```
#### 可以通过blockchain explore来查看进度.

[完整的代码在这儿](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/call_apis.py)
