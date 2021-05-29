from sqlalchemy import Column, Integer, Text, Date, Float, ForeignKey
from dao.engine import engine, Base
from dataclasses import dataclass


@dataclass
class DespesaDeputado(Base):
    __tablename__ = 'deputado_despesa'

    # 'ano': 2020,
    # 'mes': 1,
    # 'tipoDespesa': 'MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE PARLAMENTAR',
    # 'codDocumento': 7004672,
    # 'tipoDocumento': 'Nota Fiscal',
    # 'codTipoDocumento': 0,
    # 'dataDocumento': '2020-01-15',
    # 'numDocumento': '417815556',
    # 'valorDocumento': 132.76,
    # 'urlDocumento': 'https://www.camara.leg.br/cota-parlamentar/documentos/publ/3282/2020/7004672.pdf',
    # 'nomeFornecedor': 'COMPANHIA DE ELETRICIDADE DO ESTADO DA BAHIA',
    # 'cnpjCpfFornecedor': '15139629000194',
    # 'valorLiquido': 118.35,
    # 'valorGlosa': 14.41,
    # 'numRessarcimento': '',
    # 'codLote': 1671810,
    # 'parcela': 0
#    "id_deputado":204554,

    codDocumento = Column(Integer, primary_key=True)
    ano = Column(Integer)
    mes = Column(Integer)
    id_deputado = Column(Integer, ForeignKey('deputado.id'))
    tipoDespesa = Column(Text(), nullable=False)
    tipoDocumento = Column(Text(), nullable=True)
    codTipoDocumento = Column(Integer)
    dataDocumento = Column(Date)
    numDocumento = Column(Text(), nullable=True)
    valorDocumento = Column(Float)
    urlDocumento = Column(Text(), nullable=True)
    nomeFornecedor = Column(Text(), nullable=False)
    cnpjCpfFornecedor = Column(Text(), nullable=False)
    valorLiquido = Column(Float)
    valorGlosa = Column(Float)
    numRessarcimento = Column(Text(), nullable=True)
    codLote = Column(Integer)
    parcela = Column(Integer)

    # alembic revision --autogenerate -m "Nova colunas na tabela deputado"
    # alembic upgrade head

    def __repr__(self):
        return "<DespesaDeputado(ano='%s', mês='%s', tipoDespesa='%s',\
            valorDocumento='%s')>" % (self.ano, self.mes,
                                      self.tipoDespesa,
                                      self.valorDocumento)


Base.metadata.create_all(engine)
