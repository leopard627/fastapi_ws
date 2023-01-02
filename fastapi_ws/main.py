import ast
import asyncio
import json
import os
import time
from datetime import datetime

from broadcaster import Broadcast
from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.websockets import WebSocket
from loguru import logger
from starlette.concurrency import run_until_first_complete
from starlette.websockets import WebSocketDisconnect


REDIS_URL = os.getenv("REDIS_URL")
broadcast = Broadcast(url=REDIS_URL)
app = FastAPI()


async def chatroom_ws_receiver(websocket: WebSocket, chatroom_id: str):
    async for message in websocket.iter_text():
        await broadcast.publish(channel=chatroom_id, message=message)


async def chatroom_ws_sender(websocket: WebSocket, chatroom_id: str):
    async with broadcast.subscribe(channel=chatroom_id) as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)


@app.websocket("/chatrooms/{chatroom_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    chatroom_id: str,
):
    await websocket.accept()
    try:
        await run_until_first_complete(
            (
                chatroom_ws_receiver,
                {"websocket": websocket, "chatroom_id": chatroom_id},
            ),
            (chatroom_ws_sender, {"websocket": websocket, "chatroom_id": chatroom_id}),
        )

    except WebSocketDisconnect as err:
        print(err)
        await websocket.close()


@app.on_event("startup")
async def startup():
    print("connect")
    await broadcast.connect()


@app.on_event("shutdown")
async def shutdown():
    print("disconnect")
    await broadcast.disconnect()
