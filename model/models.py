# coding: utf-8
from sqlalchemy import CHAR, Column, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TwIndex(Base):
    __tablename__ = 'tw_index'

    symbol = Column(CHAR(50), primary_key=True, nullable=False)
    name = Column(CHAR(100), nullable=False)
    category = Column(CHAR(50), nullable=False)
    date = Column(Date, primary_key=True, nullable=False)
    o = Column(Float)
    h = Column(Float)
    l = Column(Float)
    c = Column(Float)
    v = Column(Float)
