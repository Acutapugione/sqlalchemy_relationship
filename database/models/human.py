from . import Base, Mapped


class Human(Base):
    name: Mapped[str]
    age: Mapped[int]
