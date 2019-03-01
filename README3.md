# How to create a Bitcoin wallet based on Mixin Network API
We have created a bot to [echo message](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README.md) and [echo Bitcoin](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/README2.md).

# What you will learn from this chapter
1. How to create Bitcoin wallet
2. How to read Bitcoin balance
3. How to send Bitcoin with zero transaction fee and confirmed in 1 second
4. How to send Bitcoin to other wallet

## Create a Bitcoin wallet by Mixin Network Python SDK
Pre-request: You should have a Mixin Network account. Create an account can be done by one line code:

```python
  userInfo = mixinApiBotInstance.createUser(session_key.decode(),"Tom Bot")
```
The function in Python SDK create a RSA key pair automatically, then call Mixin Network to create an account. last the function return all account information.

```python
//Create User api include all account information
userInfo.get("data").get("pin_token"),
userInfo.get("data").get("session_id"),
userInfo.get("data").get("user_id"),
```

Result of createUser is:
```python
{'data': {'type': 'user', 'user_id': '2f25b669-15e7-392c-a1d5-fe7ba43bdf37', 'identity_number': '0',
'full_name': 'Tom Bot', 'avatar_url': '', 'relationship': '', 'mute_until': '0001-01-01T00:00:00Z',
'created_at': '2019-02-22T06:23:41.754573722Z', 'is_verified': False,
'session_id': '284c7b39-3284-4cf6-9354-87df30ec7d57', 'phone': '',
'pin_token':'g4upUgBXa8ATk7yxL6B94HgI4GV4sG4t8Wyn6uTu2Q2scH11UMQ5bYDb6Md+3LRQqRjEdRFcLlHijXGBihRweTaKTZjHQqolWbZcffesVIias6WppV/QMu4TzXCuKa5xpj3uhjL+yPyfWTLGUaVJTJN9n7PQmHSIUBXrovbfodk=',
'invitation_code': '', 'code_id': '', 'code_url': '', 'has_pin': False,
'receive_message_source': 'EVERYBODY', 'accept_conversation_source': 'EVERYBODY'}}
```

Now you need to carefully keep the account information. You need these information to read asset balance and other content.
### Create Bitcoin wallet for the Mixin Network account
The Bitcoin  wallet is not generated automatically at same time when we create Mixin Network account. Read Bitcoin asset once to generate a Bitcoin wallet.
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
You can found information about Bitcoin asset in the account. Public key is the Bitcoin deposit address. Full response of read  Bitcoin asset is
```python
{'data': {'type': 'asset', 'asset_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'chain_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa', 'symbol': 'BTC', 'name': 'Bitcoin',
'icon_url': 'https://images.mixin.one/HvYGJsV5TGeZ-X9Ek3FEQohQZ3fE9LBEBGcOcn4c4BNHovP4fW4YB97Dg5LcXoQ1hUjMEgjbl1DPlKg1TW7kK6XP=s128', 'balance': '0',
'public_key': '1AYAMaRi3j5rXoFLmhJBFxvUEgGt8zeF4k', 'account_name': '', 'account_tag': '',
'price_btc': '1', 'price_usd': '3979.12975801', 'change_btc': '0',
'change_usd': '-0.0018925165548280905', 'asset_key': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'confirmations': 12, 'capitalization': 0}}
```
The API provide many information about Bitcoin asset.
* Deposit address:[public_key]
* Logo: [icon_url]
* Asset name:[name]
* Asset uuid in Mixin network: [asset_key]
* Price in USD from Coinmarketcap.com: [price_usd]
* Least confirmed blocks before deposit is accepted by Mixin network:[confirmations]


### Private key?
Where is Bitcoin private key? The private key is protected by multi signature inside Mixin Network so it is invisible for user. Bitcoin asset can only be withdraw to other address when user provide correct RSA private key signature, PIN code and Session key.

### Not only Bitcoin, but also Ethereum, EOS
The account not only contain a Bitcoin wallet, but also contains wallet for Ethereum, EOS, etc. Full blockchain support [list](https://mixin.one/network/chains). All ERC20 Token and EOS token are supported by the account.

Create other asset wallet is same as create Bitcoin wallet, just read the asset.
#### Mixin Network support cryptocurrencies (2019-02-19)

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

If you read EOS deposit address, the deposit address is composed of two parts: account_name and account tag. When you transfer EOS token to your account in Mixin network, you should fill both account name and memo. The memo content is value of 'account_tag'.
Result of read EOS asset is:
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

### Deposit Bitcoin and read balance
Now you can deposit Bitcoin into the deposit address.

This is maybe too expensive for this tutorial. There is a free and lightening fast solution to deposit Bitcoin: add the address in your Mixin messenger account withdrawal address and withdraw small amount Bitcoin from your account to the address. It is free and confirmed instantly because they are both on Mixin Network.

Now you can read Bitcoin balance of the account.
```python
btcInfo = mixinApiNewUserInstance.getAsset("c6d0c728-2624-429b-8e0d-d9d19b6592fa");
print(btcInfo);
```
### Send Bitcoin inside Mixin Network to enjoy instant confirmation and ZERO transaction fee
Any transaction happen between Mixin network account is free and is confirmed in 1 second.

#### Send Bitcoin to another Mixin Network account
We can send Bitcoin to our bot through Mixin Messenger, and then transfer Bitcoin from bot to new user.

```python
mixinApiBotInstance = MIXIN_API(mixin_config)
//$user_info["user_id"] generated by create user;
mixinApiBotInstance.transferTo(userid, BTC_ASSET_ID, AMOUNT, "")
```

Read bot's Bitcoin balance to confirm the transaction.
Caution: **mixinApiNewUserInstance** is for the New User!
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

### Send Bitcoin to another Bitcoin exchange or wallet
If you want to send Bitcoin to another exchange or wallet, you need to know the destination deposit address, then add the address in withdraw address list of the Mixin network account.

Pre-request: Withdrawal address is added and know the Bitcoin withdrawal fee

#### Add destination address to withdrawal address list
Call createAddress, the ID of address will be returned in result of API and is required soon.
```python
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
BTC_WALLET_ADDR = "14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C";
btcInfo = mixinApiBotInstance.createAddress(BTC_ASSET_ID, BTC_WALLET_ADDR,"BTC","","")
print(btcInfo)
```
The **14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C** is a Bitcoin wallet address, Output like below, The API result contains the withdrawal address ID, fee is 0.0034802 BTC.                                                   
```python
{'data': {'type': 'address', 'address_id': '47998e2f-2761-45ce-9a6c-6f167b20c78b',
'asset_id': 'c6d0c728-2624-429b-8e0d-d9d19b6592fa',
'public_key': '14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C', 'label': 'BTC',
'account_name': '', 'account_tag': '',
'fee': '0.0034802', 'reserve': '0', 'dust': '0.0001',
'updated_at': '2019-02-26T00:03:05.028140704Z'}}
```
If you want create a EOS address, call it like below:
```python
EOS_ASSET_ID     = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
EOS_WALLET_ADDR  = "3e2f70914c8e8abbf60040207c8aae62";
EOS_ACCOUNT_NAME = "eoswithmixin";
eosInfo = mixinApiBotInstance.createAddress(EOS_ASSET_ID, "","",EOS_ACCOUNT_NAME,EOS_WALLET_ADDR)
print(eosInfo)
```
#### Read withdraw fee anytime
```python
addr_id = btcInfo.get("data").get("address_id")
addrInfo = mixinApiBotInstance.getAddress(addr_id)
print(addrInfo)
```

#### Send Bitcoin to destination address
Submit the withdrawal request to Mixin Network, the btcInfo.get("data").get("address_id") is the address id it's return by createAddress
```python
  mixinApiBotInstance.withdrawals(btcInfo.get("data").get("address_id"),AMOUNT,"")
```
#### Confirm the transaction in blockchain explore

[Full source code](https://github.com/wenewzhang/mixin_labs-python-bot/blob/master/call_apis.py)
