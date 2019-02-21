from Crypto.PublicKey import RSA
from mixin_api import MIXIN_API
# from random_word import RandomWords
import mixin_config
import json
def pubkeyContent(inputContent):
    contentWithoutHeader= inputContent[len("-----BEGIN PUBLIC KEY-----") + 1:]
    contentWithoutTail = contentWithoutHeader[:-1 * (len("-----END PUBLIC KEY-----") + 1)]
    contentWithoutReturn = contentWithoutTail[:64] + contentWithoutTail[65:129] + contentWithoutTail[130:194] + contentWithoutTail[195:]
    return contentWithoutReturn

mixin_api = MIXIN_API(mixin_config)

key = RSA.generate(1024)
pubkey = key.publickey()
print(key.exportKey())
print(pubkey.exportKey())
private_key = key.exportKey()
session_key = pubkeyContent(pubkey.exportKey())
# print(session_key)
print(session_key.decode())
userInfo = mixin_api.createUser(session_key.decode(),"Tom Bot")
print(userInfo)
# r = RandomWords()
# r.get_random_word()
