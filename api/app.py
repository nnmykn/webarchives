from fastapi import FastAPI
import time
import datetime
import requests

# Setup
app = FastAPI()
webarchive = "https://web.archive.org/"
# Setup end

# api system
@app.get("/save")
def do_save(p: str):
    url = p
    try:
        response = requests.get(p)
        print(response)
        return({"status": "success", "url": response.url})
    except:
        print(url)
        return({"status": "error"})

# api system end