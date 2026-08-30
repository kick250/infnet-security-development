from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# authentication
from routes.authentication_router import AuthenticationRouter

# api
from routes.events_router import EventsRouter
from routes.events_alternative_router import EventsAlternativeRouter

# view
from routes.view_routes.events_view_router import EventsViewRouter


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def read_root():
    return { "status": "Server OK" }

# authentication
app.include_router(AuthenticationRouter.get_router())

# api
app.include_router(EventsRouter.get_router())
app.include_router(EventsAlternativeRouter.get_router())

# view
app.include_router(EventsViewRouter.get_router())