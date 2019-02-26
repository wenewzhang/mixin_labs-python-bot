from mixin_ws_api import MIXIN_WS_API
import base64

MASTER_UUID     = "0b4f49dc-8fb4-4539-9a89-fb3afc613747";
BTC_ASSET_ID    = "c6d0c728-2624-429b-8e0d-d9d19b6592fa";
EOS_ASSET_ID    = "6cfe566e-4aad-470b-8c9a-2fd35b49c68d";

btnBTC = MIXIN_WS_API.packButton(MASTER_UUID, BTC_ASSET_ID, "0.0001","BTC pay")
btnEOS = MIXIN_WS_API.packButton(MASTER_UUID, EOS_ASSET_ID, "0.01","EOS pay","#0080FF")
print(btnBTC)
print(btnEOS)
buttons   = [btnBTC,btnEOS]
print(type(buttons))
buttons_utf = '[' + ','.join(str(btn) for btn in buttons) + ']'
print(buttons_utf)
enButtons = base64.b64encode(buttons_utf.encode('utf-8')).decode(encoding='utf-8')
print(enButtons)
