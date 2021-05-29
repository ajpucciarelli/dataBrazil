from sqlalchemy.sql.expression import text
from dao.engine import session
# from model.congresso.deputado import Deputado
# from model.congresso.despesa import DespesaDeputado
# from model.congresso.despesa


def commit_close(func):
    def decorator(*args):
        try:
            func(*args)
        except:
            session.rollback()
            raise
        else:
            session.commit()
    return decorator


class DeputadoDao:
    @commit_close
    def insert_or_update(deputados):

        stmt = text("REPLACE INTO legislativo.deputado(id, nome, uri, siglaPartido, uriPartido,\
            siglaUf, idLegislatura, urlFoto, email) VALUES(:id, :nome, :uri,\
            :siglaPartido, :uriPartido, :siglaUf, :idLegislatura, :urlFoto,\
            :email);")
        stmt = stmt.bindparams(id="id", nome="nome", uri="uri",
                               siglaPartido="siglaPartido",
                               uriPartido="uriPartido",
                               siglaUf="siglaUf",
                               idLegislatura="idLegislatura",
                               urlFoto="urlFoto",
                               email="email")
        session.execute(stmt, deputados['dados'])
        # for deputado in deputados['dados']:
        #     session.add_all(
        #         [
        #             Deputado(
        #                 id=deputado['id'],
        #                 nome=deputado['nome'],
        #                 uri=deputado['uri'],
        #                 siglaPartido=deputado['siglaPartido'],
        #                 uriPartido=deputado['uriPartido'],
        #                 siglaUf=deputado['siglaUf'],
        #                 idLegislatura=deputado['idLegislatura'],
        #                 urlFoto=deputado['urlFoto'],
        #                 email=deputado['email']
        #             )
        #         ]
        #     )
        session.flush()


class DeputadoDespesaDao:
    @commit_close
    def insert_or_update(despesas, id_deputado):
        stmt = text("REPLACE INTO legislativo.deputado_despesa(codDocumento, \
            ano, mes, id_deputado, tipoDespesa, tipoDocumento, \
            codTipoDocumento, dataDocumento, numDocumento, valorDocumento, \
            urlDocumento, nomeFornecedor, cnpjCpfFornecedor, valorLiquido, \
            valorGlosa, numRessarcimento, codLote, parcela) VALUES( \
            :codDocumento, :ano, :mes, "+str(id_deputado)+", :tipoDespesa, \
            :tipoDocumento, :codTipoDocumento, :dataDocumento, :numDocumento, \
            :valorDocumento, :urlDocumento, :nomeFornecedor, \
            :cnpjCpfFornecedor, :valorLiquido, :valorGlosa, \
            :numRessarcimento, :codLote, :parcela);")
        stmt = stmt.bindparams(
            codDocumento="codDocumento",
            ano="ano",
            mes="mes",
            # id_deputado="id_deputado",
            tipoDespesa="tipoDespesa",
            tipoDocumento="tipoDocumento",
            codTipoDocumento="codTipoDocumento",
            dataDocumento="dataDocumento",
            numDocumento="numDocumento",
            valorDocumento="valorDocumento",
            urlDocumento="urlDocumento",
            nomeFornecedor="nomeFornecedor",
            cnpjCpfFornecedor="cnpjCpfFornecedor",
            valorLiquido="valorLiquido",
            valorGlosa="valorGlosa",
            numRessarcimento="numRessarcimento",
            codLote="codLote",
            parcela="parcela")
        session.execute(stmt, despesas)
        session.flush()
