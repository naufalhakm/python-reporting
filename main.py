from fastapi import FastAPI, Depends
from models.BaseModel import init
from config.Environment import get_environment_variables
from routes.v1.ReportRouter import ReportRouter
# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
)

# Add Routers
app.include_router(ReportRouter)

init()