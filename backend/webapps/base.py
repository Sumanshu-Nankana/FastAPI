from fastapi import APIRouter
from webapps.jobs import route_jobs
from webapps.users import route_users
from webapps.auth import route_login

api_router = APIRouter(include_in_schema=False)

api_router.include_router(route_jobs.router, tags=["homepage"])
api_router.include_router(route_users.router, tags=["users"])
api_router.include_router(route_login.router, tags=["Auth"])
