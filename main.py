import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.route import router

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app,
        host=os.environ.get("HOST", DEFAULT_HOST), 
        port=int(os.environ.get("PORT", DEFAULT_PORT))
    )