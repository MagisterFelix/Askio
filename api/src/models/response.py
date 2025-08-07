from uuid import UUID

from pydantic import BaseModel


class Response(BaseModel):
    session_id: UUID
    message: str
