from Crypto.PublicKey import RSA
from mixin_api import MIXIN_API
import mixin_config
import json
import csv

PIN             = "945689";
MASTER_ID       = "37222956";
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";
BTC_WALLET_ADDR = "14T129GTbXXPGXXvZzVaNLRFPeHXD1C25C";
AMOUNT          = "0.001";

def pubkeyContent(inputContent):
    contentWithoutHeader= inputContent[len("-----BEGIN PUBLIC KEY-----") + 1:]
    contentWithoutTail = contentWithoutHeader[:-1 * (len("-----END PUBLIC KEY-----") + 1)]
    contentWithoutReturn = contentWithoutTail[:64] + contentWithoutTail[65:129] + contentWithoutTail[130:194] + contentWithoutTail[195:]
    return contentWithoutReturn

mixinApiBotInstance = MIXIN_API(mixin_config)

PromptMsg  = "1: Create user and update PIN\n2: Read Bitcoin balance \n3: Read Bitcoin Address\n4: Read EOS balance\n"
PromptMsg += "5: Read EOS address\n6: Transfer Bitcoin from bot to new user\n7: Transfer Bitcoin from new user to Master\n"
PromptMsg += "8: Withdraw bot's Bitcoin\n"
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
            mixin_config.private_key       = private_key.decode()
            mixin_config.pin_token         = userInfo.get("data").get("pin_token")
            mixin_config.pay_session_id    = userInfo.get("data").get("session_id")
            mixin_config.client_id         = userInfo.get("data").get("user_id")
            mixin_config.client_secret     = ""
            mixin_config.pay_pin           = PIN
            mixinApiNewUserInstance        = MIXIN_API(mixin_config)
            btcInfo                        = mixinApiNewUserInstance.getAsset(BTC_ASSET_ID)
            print(btcInfo)
    if ( cmd == '2' ):
        print("read bitcoin balance")
        btcInfo = mixinApiBotInstance.getAsset(BTC_ASSET_ID)
        print(btcInfo)
