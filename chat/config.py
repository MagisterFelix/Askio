from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ChatSettings(BaseSettings):
    HOST: str = Field(default=..., alias="OLLAMA_HOST")
    PORT: int = Field(default=..., alias="OLLAMA_PORT")
    MODEL: str = Field(default=..., alias="OLLAMA_MODEL")

    @property
    def URL(self) -> str:
        return f"{self.HOST}:{self.PORT}"

    model_config = SettingsConfigDict(
        env_file="../.env", env_prefix="OLLAMA_", extra="ignore"
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


chat_settings = ChatSettings()
mq_settings = MQSettings()
