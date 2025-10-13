from fastapi import FastAPI
from api.exceptions import register_exception_handlers
from api.lifespan import lifespan
from api.middlewares import register_middlewares
from api.routes import register_routes

app = FastAPI(title="Cuida Caucaia: API", lifespan=lifespan)

register_middlewares(app)
register_exception_handlers(app)
register_routes(app)
