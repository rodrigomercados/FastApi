from fastapi import HTTPException, status

from app.v1.model.usuario_model import Usuario as UsuarioModel
from app.v1.schema import usuario_schema
from app.v1.service.auth_service import get_password_hash


def create_usuario(usuario: usuario_schema.UsuarioRegister):

    get_usuario = UsuarioModel.filter((UsuarioModel.email == usuario.email) | (UsuarioModel.usuarioname == usuario.usuarioname)).first()
    if get_usuario:
        msg = "Email already registered"
        if get_usuario.username == usuario.usuarioname:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_usuario = UsuarioModel(
        username=usuario.usuarioname,
        email=usuario.email,
        password=get_password_hash(usuario.password)
    )

    db_usuario.save()
    return usuario_schema.Usuario(
        id = db_usuario.id,
        username = db_usuario.username,
        email = db_usuario.email
    )