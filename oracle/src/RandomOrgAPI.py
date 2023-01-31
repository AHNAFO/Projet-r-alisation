import requests
import json

#pip install requests

def getListRandomOrg(lengthTab):
    
    url = "https://api.random.org/json-rpc/2/invoke"

    payload = json.dumps({
    "jsonrpc": "2.0",
    "method": "generateIntegerSequences",
    "params": {
        "apiKey": "e7fa41aa-f9a0-4c91-9783-2708ad97c54e",
        "n": 1,
        "length": lengthTab,
        "min": 1,
        "max": 100,
        "replacement": True,
        "base": 10
    },
    "id": 3076
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': '__cflb=02DiuEMAZFhhWAbaKrDP2YYpUK2thcATmcXpqdkmqVArf'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    val = json.loads(response.text)
    try:
        val = val.get('result').get('random').get('data')[0]
    except AttributeError:
        val = False
        print("Erreur : mettre une valeur superieur a 0")
    return val

