import json
body = {
            "session_secret": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLHhlK0GZCjE6o6/seNz8x0X7r+1zYtACrgJT60GHr5ol9SUFHrTt8qTPfDphxcVA9S8LN4MIowXfIabhP/5FJX3G3wdR4U+U18cFqEiYB+i7uF9ME9Q8RIk/orzeimID97F/sn0XVk8lCCaKUuL1FOHN3J67ox2RWkvMCrIJlrQIDAQAB",
            "full_name": "Tom Bot "
        }
print(body)
body_in_json = json.dumps(body)
print(body_in_json)
