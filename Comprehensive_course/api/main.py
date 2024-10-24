from fastapi import FastAPI
from .routes import users, auth
import uvicorn

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
