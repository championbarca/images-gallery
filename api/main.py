from flask import Flask, request
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")

print(os.environ)

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")
if not UNSPLASH_ACCESS_KEY:
    raise EnvironmentError("API Acees key is not set")
    
app = Flask(__name__)

@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {
        'Accept-Version' : "v1",
        'Authorization': "Client-Id " + UNSPLASH_ACCESS_KEY
    }
    params = {
        "query": word
    }

    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()
    return {"data": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)