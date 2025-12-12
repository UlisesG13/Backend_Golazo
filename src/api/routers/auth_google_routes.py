from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from src.infra.google.repositories.google_oauth_service import GoogleOAuthService
from src.usecases.auth_google_usecase import AuthGoogleUseCase
from src.core.dependency_inyection.user_di import get_user_service
from src.usecases.user_usecase import UserUsecases
router = APIRouter(prefix="/auth/google", tags=["auth"])

@router.get("/login")
def login(service: GoogleOAuthService = Depends()):
    return RedirectResponse(service.build_auth_url())

@router.get("/callback")
def callback(
    request: Request,
    service: GoogleOAuthService = Depends(),
    user_usecase: UserUsecases = Depends(get_user_service)
):
    code = request.query_params.get("code")
    tokens = service.exchange_code(code)
    user_info = service.verify_id(tokens["id_token"])

    usecase = AuthGoogleUseCase(user_usecase)
    jwt = usecase.execute(user_info)

    return {"token": jwt}
