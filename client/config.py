from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ClientSettings(BaseSettings):
    HOST: str = Field(default=..., alias="CLIENT_HOST")
    PORT: int = Field(default=..., alias="CLIENT_PORT")

    model_config = SettingsConfigDict(
        env_file="../.env", env_prefix="CLIENT_", extra="ignore"
    )


class APISettings(BaseSettings):
    HOST: str = Field(default=..., alias="API_NAME")
    PORT: int = Field(default=..., alias="API_PORT")

    @property
    def URL(self) -> str:
        return f"http://{self.HOST}:{self.PORT}"

    model_config = SettingsConfigDict(
        env_file="../.env", env_prefix="API_", extra="ignore"
    )


client_settings = ClientSettings()
api_settings = APISettings()
