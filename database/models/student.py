from . import Base, Mapped, get_model_by_name
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import ForeignKey


class Student(Base):
    course_id: Mapped[int] = mapped_column(ForeignKey("course_table.id"))
    course: Mapped["Course"] = relationship()

    human_id: Mapped[int] = mapped_column(ForeignKey("human_table.id"))
    human: Mapped["Human"] = relationship()

    group_id: Mapped[int] = mapped_column(ForeignKey("group_table.id"))
    group: Mapped["Group"] = relationship()
