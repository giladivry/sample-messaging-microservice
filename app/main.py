from fastapi import FastAPI
from app.api.messages import messages
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/messages/openapi.json", docs_url="/messages/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(messages, prefix='/api/messages', tags=['messages'])
