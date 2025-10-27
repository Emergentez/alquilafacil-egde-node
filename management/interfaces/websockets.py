from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from management.infrastructure.websockets import ConnectionManager

ws_router = APIRouter()
manager = ConnectionManager()

@ws_router.websocket("/ws/notifications/{local_id}")
async def websocket_endpoint(websocket: WebSocket, local_id: int):
    await manager.connect(websocket, local_id)
    try:
        while True:
            await websocket.receive_text()  # puedes ignorar lo que recibe si solo envías
    except WebSocketDisconnect:
        manager.disconnect(websocket, local_id)

