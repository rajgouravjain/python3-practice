from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from rest_api_demo.models.category import Category  # noqa
    from rest_api_demo.models.post import Post  # noqa
    db.drop_all()
    db.create_all()
