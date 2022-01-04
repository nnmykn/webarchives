from fastapi import FastAPI
import time
import datetime
import requests

# Setup
app = FastAPI()
webarchive_top = "https://web.archive.org/"
# Setup end

# api system
@app.get("/save")
def do_save(p: str):
    url = p
    try:
        return({"status": "success", "url": url})
    except:
        print(url)
        return({"status": "error"})

# api system end