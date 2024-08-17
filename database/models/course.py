from typing import List
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import ForeignKey

from . import (
    Base,
    Mapped,
)


class Course(Base):
    name: Mapped[str]

    students: Mapped[List["Student"]] = relationship()
