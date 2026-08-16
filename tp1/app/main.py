from fastapi import FastAPI
from routes.events_router import EventsRouter
from routes.events_alternative_router import EventsAlternativeRouter

events_router = EventsRouter.get_router()
events_alternative_router = EventsAlternativeRouter.get_router()

app = FastAPI()

@app.get("/health")
def read_root():
    return { "status": "Server OK" }


app.include_router(events_router)
app.include_router(events_alternative_router)