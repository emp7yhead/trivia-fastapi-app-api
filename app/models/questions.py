"""Models for question."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base

CATEGORY_LENGHT = 20


class Question(Base):
    """Define question model."""

    __tablename__ = 'Questions'

    id = Column(Integer, primary_key=True)
    category = Column(String(CATEGORY_LENGHT))
    question = Column(String())
    answers = relationship('Answers')

    def __repr__(self) -> str:
        """Question representation."""
        return f'Question: {self.id} {self.category} {self.question} {self.answers}'
