# Arquivo: Modules/Categoria/CategoriaView.py
from Modules.Categoria.CategoriaDAO import CategoriaDAO  # Camada de persistência específica de Categoria (usa apenas os métodos genéricos da DAO)
from Modules.Categoria.Categoria import Categoria  # Modelo/entidade Categoria

class CategoriaView:

    # ------------------------------------------------------------
    # CADASTRAR_CATEGORIA: valida o nome e cria uma nova Categoria
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_categoria(cls, nome: str):
        try:
            if not nome:  # Validação básica de campo obrigatório
                raise ValueError("O nome da categoria não pode ser vazio.")
            
            # Instancia com ID 0, o DAO Base vai auto-incrementar
            nova_categoria = Categoria(0, nome)  # ID 0 é placeholder; DAO genérico substitui pelo ID real no inserir()
            CategoriaDAO.inserir(nova_categoria)  # Delega a persistência para a camada de dados
        except Exception as e:
            raise Exception(f"Erro ao cadastrar categoria: {str(e)}")

    # ------------------------------------------------------------
    # LISTAR: repassa a listagem de categorias vinda da DAO
    # ------------------------------------------------------------
    @classmethod
    def listar(cls):
        """Método chamado pela main.py para retornar todas as categorias"""
        try:
            return CategoriaDAO.listar()  # Apenas repassa a chamada para a DAO, sem lógica adicional
        except Exception as e:
            raise Exception(f"Erro ao listar categorias: {str(e)}")

    # ------------------------------------------------------------
    # ATUALIZAR_CATEGORIA: valida o novo nome e atualiza mantendo o ID original
    # ------------------------------------------------------------
    @classmethod
    def atualizar_categoria(cls, id_categoria: int, novo_nome: str):
        try:
            if not novo_nome:  # Validação básica de campo obrigatório
                raise ValueError("O novo nome não pode ser vazio.")
            
            # Cria o objeto atualizado mantendo o ID original
            categoria_atualizada = Categoria(id_categoria, novo_nome)  # Reaproveita o id_categoria recebido (não é uma criação nova)
            CategoriaDAO.atualizar(categoria_atualizada)  # A DAO localiza pelo id e substitui o objeto antigo por este
        except Exception as e:
            raise Exception(f"Erro ao atualizar categoria: {str(e)}")

    # ------------------------------------------------------------
    # DELETAR_CATEGORIA: remove uma categoria pelo ID
    # ------------------------------------------------------------
    @classmethod
    def deletar_categoria(cls, id_categoria: int):
        try:
            CategoriaDAO.excluir(id_categoria)  # Apenas repassa o ID para a DAO remover o registro correspondente
        except Exception as e:
            raise Exception(f"Erro ao deletar categoria: {str(e)}")