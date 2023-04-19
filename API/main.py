import asyncio

from fastapi import FastAPI
from uvicorn import Server, Config
from fastapi.middleware.cors import CORSMiddleware

from database.Mongo import Mongo
from endpoints import game_points, auth_points
from settings import Settings, main_settings
from api_loggers.log import main_logger

app = FastAPI()
app.include_router(game_points.router)
app.include_router(auth_points.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def server_setup(settings: Settings = main_settings):
    main_logger.infolog.info('Logger is ready!')

    outer_port = settings.API_PORT or 8000

    debug_mode = settings.DEBUG_MODE
    container_enviroment = settings.DOCKER

    asyncio.run((Mongo().database_setup(settings)))

    if container_enviroment:
        host = "0.0.0.0"
        port = 8000
    else:
        debug_mode = True
        host = 'localhost'
        port = outer_port

    if debug_mode:
        main_logger.infolog.info(f'[S] API ROOT http://localhost:{outer_port}')
        main_logger.infolog.info(f'[S] API DOCS http://localhost:{outer_port}/docs')
        log_level = 'warning'
        reload_policy = False if container_enviroment else True  # Известная проблема см. README (1)
    else:
        main_logger.infolog.info(f'API WIIL BE STARTED IN PRODUCTION MODE AT PORT :{outer_port}')
        log_level = 'info'
        reload_policy = False

    return Server(config=Config('main:app', host=host, port=port, log_level=log_level, reload=reload_policy))


if __name__ == "__main__":
    server = server_setup()
    server.run()
