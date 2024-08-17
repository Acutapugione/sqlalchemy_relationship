from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Config:
    ENGINE = create_engine(
        # "sqlite://",
        "sqlite:///my_db.sql",
        # echo=True,
    )

    SESSION = sessionmaker(bind=ENGINE)
