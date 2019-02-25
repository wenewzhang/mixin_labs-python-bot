# import json
# body = {
#             "session_secret": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLHhlK0GZCjE6o6/seNz8x0X7r+1zYtACrgJT60GHr5ol9SUFHrTt8qTPfDphxcVA9S8LN4MIowXfIabhP/5FJX3G3wdR4U+U18cFqEiYB+i7uF9ME9Q8RIk/orzeimID97F/sn0XVk8lCCaKUuL1FOHN3J67ox2RWkvMCrIJlrQIDAQAB",
#             "full_name": "Tom Bot "
#         }
# print(body)
# body_in_json = json.dumps(body)
# print(body_in_json)
from Crypto.PublicKey import RSA
from mixin_api import MIXIN_API
# from random_word import RandomWords
import mixin_config
import json

PIN             = '832047';

mixinApiBotInstance = MIXIN_API(mixin_config)
print("will verify Pin",mixin_config.pay_pin)
pinInfo = mixinApiBotInstance.verifyPin(mixin_config.pay_pin)
print(pinInfo)
# pinInfo = mixinApiBotInstance.updatePin(PIN,mixin_config.pay_pin)
