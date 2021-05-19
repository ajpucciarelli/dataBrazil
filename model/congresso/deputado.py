from sqlalchemy import Column, Integer, String, Text
from dao.engine import engine, Base
from dataclasses import dataclass

@dataclass
class Deputado(Base):
    __tablename__ = 'deputado'

#    "id":204554,
#    "uri":"https://dadosabertos.camara.leg.br/api/v2/deputados/204554",
#    "nome":"Abílio Santana",
#    "siglaPartido":"PL",
#    "uriPartido":"https://dadosabertos.camara.leg.br/api/v2/partidos/37906",
#    "siglaUf":"BA",
#    "idLegislatura":56,
#    "urlFoto":"https://www.camara.leg.br/internet/deputado/bandep/204554.jpg",
#    "email":"dep.abiliosantana@camara.leg.br"

    id = Column(Integer, primary_key=True)
    nome = Column(Text(), nullable=False)
    uri = Column(Text(), nullable=True)
    siglaPartido = Column(String(50), nullable=True)
    uriPartido = Column(Text(), nullable=True)
    siglaUf = Column(String(2), nullable=False)
    idLegislatura = Column(Integer, nullable=False)
    urlFoto = Column(Text(), nullable=True)
    email = Column(Text(), nullable=True)
    
    #alembic revision --autogenerate -m "Nova colunas na tabela deputado"
    #alembic upgrade head

    def __repr__(self):
        return "<Deputado(id='%s', nome='%s')>" % (self.id, self.nome)

Base.metadata.create_all(engine)