from fastapi import FastAPI
from loguru import logger

# from app.api.api_v1.api import api_router
from app.core.config import get_app_settings
from app.db.session import SessionLocal

# from starlette.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    # load settings
    settings = get_app_settings()
    settings.configure_logging()  ## replace this implicit

    logger.info(settings.fastapi_kwargs)

    # init App
    app = FastAPI(**settings.fastapi_kwargs)

    # init middleware

    # init external services : DB, email ,...
    @app.on_event("startup")
    def startup_event():
        try:
            db = SessionLocal()
            con = db.execute("SELECT 1")
            logger.info(str(con))
        except Exception as e:
            logger.error(e)
            raise e

    @app.on_event("shutdown")
    def shutdown_event():
        logger.info("Shutting Down")

    # init exceptions

    @app.get("/hello_world")
    def hello_world():
        return {"message": "Hello World"}

    return app


app = create_app()
