from sqlalchemy import  Column,Integer, String

from database import Base


class Variable(Base):
    __tablename__ = "variable"

   # id = Column(Integer, primary_key=True, index=True)
    kursi = Column(String, unique=True,index=True)
    kondisi = Column(String)