"""Run script using:

> uvicorn main:app
"""


from fastapi import FastAPI
from parapy.webgui.core import WebGUI
from fpc.app import App


app = FastAPI()
api = WebGUI()
api.init_app(app, App)


if __name__ == "__main__":
    from parapy.webgui.core import open_web_browser_when_served
    from uvicorn import run

    open_web_browser_when_served(polling_interval=1, timeout=5)
    run(app)
