from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Date, Boolean, BigInteger
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    birthday = Column(String, nullable=False)
    reg_date = Column(DateTime)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_title = Column(String, nullable=False)
    category_created_at = Column(DateTime)


class Procedure(Base):
    __tablename__ = "procedures"
    id = Column(Integer, autoincrement=True, primary_key=True)
    procedure_title = Column(String, nullable=False)
    procedure_description = Column(String, nullable=False)
    procedure_price = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_title"))
    procedure_created_at = Column(DateTime)

    category_fk = relationship(Category, lazy="subquery")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, autoincrement=True, primary_key=True)
    article_title = Column(String, nullable=False)
    article_text = Column(String, nullable=False)
    article_author = Column(String, nullable=True)
    article_created_at = Column(DateTime)


class ProcedurePhoto(Base):
    __tablename__ = "procedure_photos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    procedure_id = Column(Integer, ForeignKey("procedures.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    photo_path = Column(String, nullable=False)
    created_at = Column(DateTime)

    procedure_fk = relationship(Procedure, lazy="subquery")
    article_fk = relationship(Article, lazy="subquery")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    procedure_id = Column(Integer, ForeignKey("procedures.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    comment_text = Column(String, nullable=False)
    comment_created_at = Column(DateTime)

    user_fk = relationship(User, lazy="subquery")
    procedure_fk = relationship(Procedure, lazy="subquery")


class Cart(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    procedure_id = Column(Integer, ForeignKey("procedures.id"))
    user_add_date = Column(DateTime)
