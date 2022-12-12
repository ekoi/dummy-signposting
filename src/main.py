import json
import logging
import os

import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends, status
from dynaconf import Dynaconf

import importlib.metadata

__version__ = importlib.metadata.metadata("dummy-signposting-service")["version"]

settings = Dynaconf(settings_files=["conf/settings.toml"],
                    environments=True)
logging.basicConfig(filename=settings.LOG_FILE, level=settings.LOG_LEVEL,
                    format=settings.LOG_FORMAT)

app = FastAPI(title=settings.FASTAPI_TITLE, description=settings.FASTAPI_DESCRIPTION,
              version=__version__)

@app.get('/')
def info():
    logging.info("Dummy Signposting Generator")
    logging.debug("info")
    return {"name": "Dummy Signposting Generator", "version": __version__}

@app.get('/links/{json_filename}')
def get_links(json_filename:str):
    with open(os.path.join(settings.RESOURCES_PATH, json_filename)) as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    logging.info("Start")
    uvicorn.run("src.main:app", host="0.0.0.0", port=2907, reload=False)


