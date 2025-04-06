from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from notifications.db import Base, engine
from notifications.routers import websocket


routers = [websocket.router]
Base.metadata.create_all(engine)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
for router in routers:
    app.include_router(router)
if __name__=="__main__":
    uvicorn.run(app,port=9002,host="0.0.0.0", ws="websockets")
