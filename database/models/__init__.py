from __future__ import annotations

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower() + "_table"


def get_model_by_name(model_name: str):
    models = {
        str(Group): Group,
        str(Human): Human,
        str(Course): Course,
        # str(Student): Student,
    }
    models.get(model_name)


from .group import Group
from .human import Human
from .course import Course
from .student import Student
