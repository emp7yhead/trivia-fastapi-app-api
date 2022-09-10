"""Models for question."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Question(Base):
    """Define question model."""

    __tablename__ = 'Questions'

    id = Column(Integer, primary_key=True)
    description = Column(String())
    answers = relationship('Answers')

    def __repr__(self) -> str:
        """Question representation."""
        return f'<Question: {self.id} {self.question}>'
