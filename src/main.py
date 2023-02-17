import json
import logging
import os


import uvicorn
from fastapi import FastAPI, Request, HTTPException
from dynaconf import Dynaconf

import importlib.metadata

__version__ = importlib.metadata.metadata("dummy-signposting-service")["version"]

from starlette.responses import Response

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


@app.get('/linkset/{number}/json')
def get_links(number: str):
    try:
        with open(os.path.join(settings.RESOURCES_PATH, f'{number}.json')) as f:
            data = json.load(f)
    except:
        raise HTTPException(status_code=404, detail=f'linkset "{number}" not found')

    return data


@app.api_route('/page/{number}', methods=['GET', 'HEAD'])
def get_page(number: int, response: Response, request: Request):
    base_url = request.base_url
    response.headers['X-Powered-By'] = 'https://github.com/ekoi/dummy-signposting'
    response.headers['Allow'] = "GET, HEAD"
    response.headers['Link'] = f'<{base_url}linkset/{number}/json> ; rel="linkset" ; type="application/linkset+json"'

    return {"eko": number}


if __name__ == "__main__":
    logging.info("Start")
    uvicorn.run("src.main:app", host="0.0.0.0", port=2907, reload=False)
