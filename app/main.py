import uvicorn
from app.routes import task, done
from fastapi import FastAPI

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

@app.get("/hello")
async def hello():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True)