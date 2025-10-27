from fastapi import WebSocket
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        # Diccionario: local_id -> lista de WebSocket
        self.active_connections: dict[int, list[WebSocket]] = defaultdict(list)

    async def connect(self, websocket: WebSocket, local_id: int):
        await websocket.accept()
        self.active_connections[local_id].append(websocket)

    def disconnect(self, websocket: WebSocket, local_id: int):
        if websocket in self.active_connections[local_id]:
            self.active_connections[local_id].remove(websocket)
            # Elimina la lista si queda vacía
            if not self.active_connections[local_id]:
                del self.active_connections[local_id]

    async def send_message(self, message: str, local_id: int):
        for connection in self.active_connections.get(local_id, []):
            try:
                await connection.send_text(message)
            except:
                self.disconnect(connection, local_id)
