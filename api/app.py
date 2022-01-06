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
def do_save(url: str):
    url = str(url)
    try:
        session = requests.Session()
        req = session.get(f"http://web.archive.org/save/{url}")
        return({"status": "success", "url": url, "answer": req.text})
    except:
        print(url)
        return({"status": "error"})

# api system end