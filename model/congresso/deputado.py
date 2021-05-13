from sqlalchemy import Column, Integer, String
from dao.engine import engine, Base
from dataclasses import dataclass

@dataclass
class Deputado(Base):
    __tablename__ = 'deputado'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    #phone = Column(String(50))
    #email = Column(String(50))

    def __repr__(self):
        return "<Deputado(id='%s', nome='%s')>" % (self.id, self.nome)

Base.metadata.create_all(engine)