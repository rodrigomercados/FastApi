from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UsuarioBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="myemail@cosasdedevs.com"
    )
    usuarioname: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="MyTypicalUsername"
    )


class Usuario(UsuarioBase):
    id: int = Field(
        ...,
        example="5"
    )


class UsuarioRegister(UsuarioBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )