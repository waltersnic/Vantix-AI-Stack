# /code/backend-fastapi/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from code.backend_fastapi import agent_router, memory_api, ws_log_stream

app = FastAPI()

# Allow web UI to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(agent_router.router, prefix="/api")
app.include_router(memory_api.router, prefix="/api")
app.include_router(ws_log_stream.router)
