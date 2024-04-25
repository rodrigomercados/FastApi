from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from app.v1.schema import usuario_schema
from app.v1.service import usuario_service
from app.v1.service import auth_service
from app.v1.schema.token_schema import Token

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["usuario"]
)

@router.post(
    "/usuario/",
    status_code=status.HTTP_201_CREATED,
    response_model=usuario_schema.Usuario,
    dependencies=[Depends(get_db)],
    summary="Create a new usuario"
)
def create_usuario(usuario: usuario_schema.UsuarioRegister = Body(...)):
    """
    ## Create a new user in the app

    ### Args
    The app can receive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return usuario_service.create_usuario(usuario)

@router.post(
    "/login",
    tags=["usuario"],
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login for access token

    ### Args
    The app can receive next fields by form data
    - username: Your username or email
    - password: Your password

    ### Returns
    - access token and token type
    """
    access_token = auth_service.generate_token(form_data.usuarioname, form_data.password)
    return Token(access_token=access_token, token_type="bearer")