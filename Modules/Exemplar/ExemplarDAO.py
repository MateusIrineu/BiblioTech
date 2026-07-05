# Arquivo: ExemplarDAO.py
from DAO.DAO import DAO
from Modules.Exemplar.Exemplar import Exemplar

class ExemplarDAO(DAO):
    arquivo = "exemplares.json"
    objetos = []
    classe_modelo = Exemplar

    # ATENDE AO REQUISITO: Operação de Pesquisa Parcial
    @classmethod
    def listar_por_livro(cls, id_livro: int):
        cls.abrir()
        return [e for e in cls.objetos if e.id_livro == id_livro]

    @classmethod
    def listar_disponiveis_por_livro(cls, id_livro: int):
        cls.abrir()
        return [e for e in cls.objetos if e.id_livro == id_livro and e.disponivel]
