from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    HOST: str = Field(default=..., alias="API_HOST")
    PORT: int = Field(default=..., alias="API_PORT")

    model_config = SettingsConfigDict(
        env_file="../.env", env_prefix="API_", extra="ignore"
    )


class MQSettings(BaseSettings):
    USER: str = Field(default=..., alias="RABBITMQ_USER")
    PASS: str = Field(default=..., alias="RABBITMQ_PASSWORD")
    HOST: str = Field(default=..., alias="RABBITMQ_HOST")
    PORT: int = Field(default=..., alias="RABBITMQ_PORT")

    @property
    def URL(self) -> str:
        return f"amqp://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}"

    model_config = SettingsConfigDict(
        env_file="../.env", env_prefix="RABBITMQ_", extra="ignore"
    )


api_settings = APISettings()
mq_settings = MQSettings()
