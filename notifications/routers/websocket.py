# app/notifications/routers/websocket.py
import traceback
from fastapi import WebSocket, WebSocketDisconnect,APIRouter
import redis
from notifications import config
from shared.redis_manager import RedisConnectionManager
from shared.redis_pubsub import RedisPubsub
import asyncio

router = APIRouter(prefix="/ws")
redisConnectionManager = RedisConnectionManager(host=config.redis_host, port=config.redis_port)
redisPubsub = RedisPubsub(host=config.redis_host, port=config.redis_port, channel="notifications")

@router.get("/")
async def get():
    return {"message": "WebSocket server is running"}

@router.websocket("/connect")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # connection_id = str(websocket.id)
    try:
        # redisConnectionManager.store_user_connection(user_id, connection_id)
        print("Client connected")
        async def handle_message(message):
            print(f"Received message: {message}")
            await websocket.send_text(message)
        redisPubsub.subscribe(handle_message)
        while True:
            await asyncio.sleep(1)  #        
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception:
        traceback.print_exc()
    finally:
        await websocket.close()
        print("Connection closed")