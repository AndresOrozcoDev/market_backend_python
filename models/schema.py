from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Supermarket(Base):
    __tablename__ = 'supermarket'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    unit = Column(String)
    supermarket_id = Column(Integer, ForeignKey('supermarket.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

