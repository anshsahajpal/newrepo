from pydantic import BaseModel, SecretStr, UUID4


class User(BaseModel):
    username: str
    email: str


class GetUser(User):
    id: UUID4


class CreateUser(User):
    password: SecretStr

