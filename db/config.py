from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    USER: str = Field(default=..., alias="POSTGRES_USER")
    PASS: str = Field(default=..., alias="POSTGRES_PASSWORD")
    NAME: str = Field(default=..., alias="POSTGRES_DB")
    HOST: str = Field(default=..., alias="POSTGRES_HOST")
    PORT: int = Field(default=..., alias="POSTGRES_PORT")

    @property
    def URL(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"

    model_config = SettingsConfigDict(
        env_file="../.env", env_prefix="POSTGRES_", extra="ignore"
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


db_settings = DBSettings()
mq_settings = MQSettings()
