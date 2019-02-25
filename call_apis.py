from Crypto.PublicKey import RSA
from mixin_api import MIXIN_API
import mixin_config
import json
import csv
import time

PIN             = "945689";
PIN2            = "845689";
MASTER_ID       = "37222956";
MASTER_UUID     = "0b4f49dc-8fb4-4539-9a89-fb3afc613747";
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
BTC_WALLET_ADDR = "14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C";
AMOUNT          = "0.001";

# // Mixin Network support cryptocurrencies (2019-02-19)
# // |EOS|6cfe566e-4aad-470b-8c9a-2fd35b49c68d
# // |CNB|965e5c6e-434c-3fa9-b780-c50f43cd955c
# // |BTC|c6d0c728-2624-429b-8e0d-d9d19b6592fa
# // |ETC|2204c1ee-0ea2-4add-bb9a-b3719cfff93a
# // |XRP|23dfb5a5-5d7b-48b6-905f-3970e3176e27
# // |XEM|27921032-f73e-434e-955f-43d55672ee31
# // |ETH|43d61dcd-e413-450d-80b8-101d5e903357
# // |DASH|6472e7e3-75fd-48b6-b1dc-28d294ee1476
# // |DOGE|6770a1e5-6086-44d5-b60f-545f9d9e8ffd
# // |LTC|76c802a2-7c88-447f-a93e-c29c9e5dd9c8
# // |SC|990c4c29-57e9-48f6-9819-7d986ea44985
# // |ZEN|a2c5d22b-62a2-4c13-b3f0-013290dbac60
# // |ZEC|c996abc9-d94e-4494-b1cf-2a3fd3ac5714
# // |BCH|fd11b6e3-0b87-41f1-a41f-f0e9b49e5bf0

def pubkeyContent(inputContent):
    contentWithoutHeader= inputContent[len("-----BEGIN PUBLIC KEY-----") + 1:]
    contentWithoutTail = contentWithoutHeader[:-1 * (len("-----END PUBLIC KEY-----") + 1)]
    contentWithoutReturn = contentWithoutTail[:64] + contentWithoutTail[65:129] + contentWithoutTail[130:194] + contentWithoutTail[195:]
    return contentWithoutReturn

def generateMixinAPI(private_key,pin_token,session_id,user_id,pin,client_secret):
    mixin_config.private_key       = private_key
    mixin_config.pin_token         = pin_token
    mixin_config.pay_session_id    = session_id
    mixin_config.client_id         = user_id
    mixin_config.client_secret     = client_secret
    mixin_config.pay_pin           = pin
    return  MIXIN_API(mixin_config)

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

            # print(btcInfo.get("data").get("public_key"))

mixinApiBotInstance = MIXIN_API(mixin_config)

PromptMsg  = "1: Create user and update PIN\n2: Read Bitcoin balance \n3: Read Bitcoin Address\n4: Read EOS balance\n"
PromptMsg += "5: Read EOS address\n6: Transfer Bitcoin from bot to new account\n7: Transfer Bitcoin from new account to Master\n"
PromptMsg += "8: Withdraw bot's Bitcoin\na: Verify Pin\nd: Create Address and Delete it\nr: Create Address and read it\n"
PromptMsg += "9: Exit \nMake your choose:"
while ( 1 > 0 ):
    cmd = input(PromptMsg)
    if (cmd == '9' ):
        exit()
    print("Run...")
    if ( cmd == '1' ):
        key = RSA.generate(1024)
        pubkey = key.publickey()
        print(key.exportKey())
        print(pubkey.exportKey())
        private_key = key.exportKey()
        session_key = pubkeyContent(pubkey.exportKey())
        # print(session_key)
        print(session_key.decode())
        userInfo = mixinApiBotInstance.createUser(session_key.decode(),"Tom Bot")
        print(userInfo.get("data").get("user_id"))
        with open('new_users.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([private_key.decode(),
                                userInfo.get("data").get("pin_token"),
                                userInfo.get("data").get("session_id"),
                                userInfo.get("data").get("user_id"),
                                PIN])
        mixinApiNewUserInstance = generateMixinAPI(private_key.decode(),
                                                    userInfo.get("data").get("pin_token"),
                                                    userInfo.get("data").get("session_id"),
                                                    userInfo.get("data").get("user_id"),
                                                    PIN,"")
        pinInfo = mixinApiNewUserInstance.updatePin(PIN,"")
        print(pinInfo)
        time.sleep(3)
        # mixinApiNewUserInstance.pay_pin = PIN
        pinInfo2 = mixinApiNewUserInstance.verifyPin()
        print(pinInfo2)
    if ( cmd == '2' ):
        print("Read Bitcoin(uuid:%s) balance" %(BTC_ASSET_ID))
        readAssetBalance(BTC_ASSET_ID)
    if ( cmd == '3' ):
        print("Read Bitcoin(uuid:%s) address" %(BTC_ASSET_ID))
        readAssetAddress(BTC_ASSET_ID)
    if ( cmd == '4' ):
        print("Read EOS(uuid:%s) balance" %(EOS_ASSET_ID))
        readAssetBalance(EOS_ASSET_ID)
    if ( cmd == '5' ):
        print("Read Bitcoin(uuid:%s) address" %(EOS_ASSET_ID))
        readAssetAddress(EOS_ASSET_ID,False)
    if ( cmd == '6' ):
        with open('new_users.csv', newline='') as csvfile:
            reader  = csv.reader(csvfile)
            for row in reader:
                row.pop()
                userid  = row.pop()
                mixinApiBotInstance.transferTo(userid, BTC_ASSET_ID, AMOUNT, "")
    if ( cmd == '7' ):
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
                btcInfo = mixinApiBotInstance.transferTo(MASTER_UUID, BTC_ASSET_ID, AMOUNT, "")
                print(btcInfo)
    if ( cmd == '8' ):
        with open('new_users.csv', newline='') as csvfile:
            reader  = csv.reader(csvfile)
            for row in reader:
                pin         = row.pop()
                userid      = row.pop()
                session_id  = row.pop()
                pin_token   = row.pop()
                private_key = row.pop()
                print(pin)
                mixinApiNewUserInstance = generateMixinAPI(private_key,
                                                            pin_token,
                                                            session_id,
                                                            userid,
                                                            pin,"")
                btcInfo = mixinApiBotInstance.createAddress(BTC_ASSET_ID, BTC_WALLET_ADDR,"BTC","","")
                mixinApiBotInstance.withdrawals(btcInfo.get("data").get("address_id"),AMOUNT,"")
                print(btcInfo)
    if ( cmd == 'a' ):
        with open('new_users.csv', newline='') as csvfile:
            reader  = csv.reader(csvfile)
            for row in reader:
                pin         = row.pop()
                userid      = row.pop()
                session_id  = row.pop()
                pin_token   = row.pop()
                private_key = row.pop()
                print(pin)
                mixinApiNewUserInstance = generateMixinAPI(private_key,
                                                            pin_token,
                                                            session_id,
                                                            userid,
                                                            pin,"")
                btcInfo = mixinApiNewUserInstance.verifyPin()
                print(btcInfo)
    if ( cmd == 'd' ):
        with open('new_users.csv', newline='') as csvfile:
            reader  = csv.reader(csvfile)
            for row in reader:
                pin         = row.pop()
                userid      = row.pop()
                session_id  = row.pop()
                pin_token   = row.pop()
                private_key = row.pop()
                print(pin)
                mixinApiNewUserInstance = generateMixinAPI(private_key,
                                                            pin_token,
                                                            session_id,
                                                            userid,
                                                            pin,"")
                btcInfo = mixinApiBotInstance.createAddress(BTC_ASSET_ID, BTC_WALLET_ADDR,"BTC","","")
                addr_id = btcInfo.get("data").get("address_id")
                print(addr_id)
                delInfo = mixinApiBotInstance.delAddress(addr_id)
                print(delInfo)
    if ( cmd == 'r' ):
        with open('new_users.csv', newline='') as csvfile:
            reader  = csv.reader(csvfile)
            for row in reader:
                pin         = row.pop()
                userid      = row.pop()
                session_id  = row.pop()
                pin_token   = row.pop()
                private_key = row.pop()
                print(pin)
                mixinApiNewUserInstance = generateMixinAPI(private_key,
                                                            pin_token,
                                                            session_id,
                                                            userid,
                                                            pin,"")
                btcInfo = mixinApiBotInstance.createAddress(BTC_ASSET_ID, BTC_WALLET_ADDR,"BTC","","")
                addr_id = btcInfo.get("data").get("address_id")
                print(addr_id)
                addrInfo = mixinApiBotInstance.getAddress(addr_id)
                print(addrInfo)
