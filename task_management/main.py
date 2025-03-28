from fastapi import FastAPI
import uvicorn
from routers.tasks import tasks_router
from db import Base, engine
import config

config.check_config()


routers = [tasks_router]
Base.metadata.create_all(engine)


app = FastAPI()
for router in routers:
    app.include_router(router)

if __name__=="__main__":
    uvicorn.run(app,port=9001,host="0.0.0.0")
