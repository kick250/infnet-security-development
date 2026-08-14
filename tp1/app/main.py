from fastapi import FastAPI
from routes.events_router import EventsRouter

events_router = EventsRouter.get_router()

app = FastAPI()

@app.get("/health")
def read_root():
    return { "status": "Server OK" }


app.include_router(events_router)