from pydantic import BaseModel


class LoginRequest(
    BaseModel
):

    username: str

    password: str


class LoginResponse(
    BaseModel
):

    access_token: str

    token_type: str


class ForgotPasswordRequest(
    BaseModel
):

    email: str


class ResetPasswordRequest(
    BaseModel
):

    token: str

    new_password: str


class PasswordResetResponse(
    BaseModel
):

    message: str