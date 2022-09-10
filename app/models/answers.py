"""Models for answer."""
from sqlalchemy import Boolean, Column, Integer, String

from app.database.base_class import Base


class Answer(Base):
    """Define answer model."""

    __tablename__ = 'Answers'

    id = Column(Integer, primary_key=True)
    text = Column(String())
    is_correct = Column(Boolean())

    def __repr__(self) -> str:
        """Answer representation."""
        return f'Answer {self.id} {self.answer} is {self.is_correct}'
