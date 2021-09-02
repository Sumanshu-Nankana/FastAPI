from fastapi import APIRouter
from webapps.jobs import route_jobs

api_router = APIRouter(include_in_schema=False)

api_router.include_router(route_jobs.router, tags=["homepage"])
