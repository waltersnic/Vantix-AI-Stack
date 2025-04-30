# /code/backend-fastapi/ws_log_stream.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()
active_connections = []

# Sample rotating log messages (for simulation)
MOCK_LOGS = [
    "[DropBot] Product launched successfully",
    "[TrendScout] Found trending: AI Dice",
    "[Sir Vaelin] Emotion shifted to 'sad'",
    "[Command Center] Task sent to DropBot"
]

@router.websocket("/logs/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            for log in MOCK_LOGS:
                await websocket.send_text(log)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
