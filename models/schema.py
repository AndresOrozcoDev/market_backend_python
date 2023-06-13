from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Supermarket(Base):
    __tablename__ = 'supermarket'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    supermarket_id = Column(Integer, ForeignKey('supermarket.id'))