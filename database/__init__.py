from .models import (
    Base,
    Human,
    Group,
    Course,
    Student,
)
from .config import Config


def migrate():
    Base.metadata.drop_all(Config.ENGINE)
    Base.metadata.create_all(Config.ENGINE)
