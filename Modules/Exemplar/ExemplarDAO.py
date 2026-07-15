# Arquivo: ExemplarDAO.py
from DAO.DAO import DAO  # Importa a classe genérica DAO (classe mãe) com toda a lógica de persistência (CRUD em JSON)
from Modules.Exemplar.Exemplar import Exemplar  # Importa o modelo Exemplar, que representa um exemplar físico de um Livro

class ExemplarDAO(DAO):
    arquivo = "exemplares.json"     # Nome do arquivo JSON usado para persistir os exemplares
    objetos = []                    # Lista própria da subclasse (evita conflito com a lista da classe mãe DAO)
    classe_modelo = Exemplar        # Define qual classe será usada no from_dict() (polimorfismo) ao reconstruir os objetos

    # ------------------------------------------------------------
    # LISTAR_POR_LIVRO: pesquisa parcial - filtra exemplares de um livro
    # ------------------------------------------------------------
    # Método específico de ExemplarDAO (não existe na DAO genérica),
    # pois só faz sentido para um modelo que possua o atributo id_livro.
    # Atende ao requisito de "Operação de Pesquisa Parcial" (busca
    # filtrada por um critério, e não pelo id exato).
    # ATENDE AO REQUISITO: Operação de Pesquisa Parcial
    @classmethod
    def listar_por_livro(cls, id_livro: int):
        cls.abrir()  # Recarrega os exemplares do arquivo antes de filtrar
        return [e for e in cls.objetos if e.id_livro == id_livro]  # Retorna apenas os exemplares que pertencem ao livro informado

    # ------------------------------------------------------------
    # LISTAR_DISPONIVEIS_POR_LIVRO: filtra exemplares de um livro que
    # ainda estão disponíveis para empréstimo
    # ------------------------------------------------------------
    # Combina dois critérios de filtragem: pertencer ao livro (id_livro)
    # e estar disponível (atributo booleano "disponivel" do Exemplar).
    # Usado, por exemplo, na tela de solicitação de empréstimo, para
    # mostrar ao usuário só os exemplares que podem ser emprestados.
    @classmethod
    def listar_disponiveis_por_livro(cls, id_livro: int):
        cls.abrir()  # Recarrega os exemplares do arquivo antes de filtrar
        return [e for e in cls.objetos if e.id_livro == id_livro and e.disponivel]  # Filtra por livro E disponibilidade