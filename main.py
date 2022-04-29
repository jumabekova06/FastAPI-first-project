import fastapi
import uvicorn

from api import motd
from views import home # New

from starlette.staticfiles import StaticFiles
from environs import Env

from api import digital_ocean_images
from services import digital_ocean_service

main_app = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_env_vars()

def configure_routing():
    main_app.mount('/static', StaticFiles(directory='static'), name='static') # New
    main_app.include_router(motd.router)
    main_app.include_router(home.router) # New
    main_app.include_router(digital_ocean_images.router)

def configure_env_vars():
    env = Env()
    env.read_env()
    if not env("ENV_SECRET"):
        print(f"WARNING: environment variable ENV_SECRET not found")
        raise Exception("environment variable ENV_SECRET not found.")
    else:
        home.secret = env("ENV_SECRET")
    if not env("DO_API_ACCESS_TOKEN"):
        print(f"WARNING: environment variable DO_API_ACCESS_TOKEN not found")
        raise Exception("environment variable DO_API_ACCESS_TOKEN not found.")
    else:
        digital_ocean_service.do_api_token = env("DO_API_ACCESS_TOKEN")

if __name__ == '__main__':
    configure()
    uvicorn.run(main_app, host='127.0.0.1', port=7000)
else:
    configure()