"""Models for category."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base

CATEGORY_LENGHT = 20


class Category(Base):
    """Define category model."""

    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True)
    name = Column(String(CATEGORY_LENGHT))
    description = Column(String())
    questions = relationship('Question', backref='questions')

    def __repr__(self) -> str:
        """Category representation."""
        return f'Category {self.id} {self.name} {self.description}'
