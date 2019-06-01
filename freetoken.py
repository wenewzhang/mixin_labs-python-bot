from flask import Flask
from flask import request
import uuid
from mixin_api import MIXIN_API
import mixin_config
import json
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/token", methods = ["POST"])
def freetoken():
    if (request.is_json):
        content = request.get_json()
        print(content)
        if (('session_secret' in content) and ('full_name' in content)):
            print (content['session_secret'])
            mixinApiBotInstance = MIXIN_API(mixin_config)
            body_in_json = json.dumps(content)

            token = mixinApiBotInstance.genPOSTJwtToken("/users", body_in_json, str(uuid.uuid4()), 20).decode('utf8')
            return jsonify({"token":token})
    return "OK"
