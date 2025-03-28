from fastapi import FastAPI
import uvicorn
from user_management.routers.auth import auth_router
from user_management.routers.user import user_router
from user_management.db import Base,engine


app = FastAPI()
routers = [auth_router,user_router]

for router in routers:
    app.include_router(router)
Base.metadata.create_all(engine)
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=9009)