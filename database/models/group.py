from . import Base, Mapped


class Group(Base):
    name: Mapped[str]
    subject: Mapped[str]
