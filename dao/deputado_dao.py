from sqlalchemy.sql.expression import text
from dao.engine import session
from model.congresso.deputado import Deputado
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

        #stmt = text("SELECT * FROM Deputado WHERE users.name BETWEEN :x AND :y")
        #stmt = stmt.bindparams(x="m", y="z")
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
