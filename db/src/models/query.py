from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.base import Base


class Query(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[UUID] = mapped_column(
        ForeignKey("session.id", ondelete="CASCADE")
    )
    message: Mapped[str]
    answer: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
