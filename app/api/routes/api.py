from fastapi import APIRouter

from app.api.routes import auth_controller, teams_controller

router = APIRouter()
router.include_router(teams_controller.router, tags=["teams"], prefix="/teams")
router.include_router(auth_controller.router, tags=["auth"], prefix="/auth")
