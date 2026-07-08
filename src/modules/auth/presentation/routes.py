from src.modules.auth.domain.models import AuthenticatedUser
from src.core.security import get_current_user
from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import RedirectResponse
from pydantic import EmailStr

from src.modules.auth.presentation.dependencies import (
    login_user_service,
    register_user_service,
    login_with_google_service,
    get_google_auth_url_service,
    generate_recovery_code_service,
    send_recovery_code_service,
    verify_recovery_code_service,
    reset_password_service,
    verify_user_service
)

from src.modules.auth.presentation.schemas import (
    UserRegister,
    UserLogin,
    LoginResponseDTO,
)

router = APIRouter()


@router.post("/register", response_model=LoginResponseDTO, status_code=status.HTTP_201_CREATED)
async def register(
        data: UserRegister,
        usecase=Depends(register_user_service),
):
    return await usecase.execute(
        data
    )


@router.post("/login", response_model=LoginResponseDTO, status_code=status.HTTP_201_CREATED)
async def login(
        data: UserLogin,
        usecase=Depends(login_user_service),
):
    return await usecase.execute(
        data
    )


@router.get("/me")
async def me(
        user: AuthenticatedUser = Depends(get_current_user),
):
    return user


@router.get("/google/login")
async def google_login(
        usecase=Depends(get_google_auth_url_service),
):
    url = await usecase.execute()
    return RedirectResponse(url)


@router.get("/google/callback", response_model=LoginResponseDTO)
async def google_callback(
        request: Request,
        usecase=Depends(login_with_google_service),
):
    code = request.query_params.get("code")
    return await usecase.execute(code)


@router.post("/recovery/request", status_code=status.HTTP_201_CREATED)
async def request_recovery(
        email: EmailStr,
        generate_uc=Depends(generate_recovery_code_service),
        send_uc=Depends(send_recovery_code_service),
):
    code = await generate_uc.execute(email)
    return await send_uc.execute(email, code)


@router.post("/recovery/verify", status_code=status.HTTP_201_CREATED)
async def verify_code(
        usuario_id: str,
        code: str,
        usecase_code=Depends(verify_recovery_code_service),
        usecase_auth=Depends(verify_user_service)
):
    if await usecase_code.execute(usuario_id, code):
        return await usecase_auth.execute(usuario_id)
    return None


@router.post("/recovery/reset", status_code=status.HTTP_201_CREATED)
async def reset_password(
        usuario_id: str,
        new_password: str,
        usecase=Depends(reset_password_service),
):
    return await usecase.execute(usuario_id, new_password)
