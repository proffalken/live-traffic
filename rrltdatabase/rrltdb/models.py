from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tiploc(Base):
    __tablename__ = "tiploc"
    internal_tiploc_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    tiploc_code = Column(String(10))
    nalco = Column(String(10))
    stanox = Column(String(10))
    crs_code = Column(String(10))
    description = Column(String(100))
    tps_description = Column(String(100))
