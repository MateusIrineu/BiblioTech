# Arquivo: Modules/Categoria/CategoriaView.py
from Modules.Categoria.CategoriaDAO import CategoriaDAO
from Modules.Categoria.Categoria import Categoria

class CategoriaView:

    @classmethod
    def cadastrar_categoria(cls, nome: str):
        try:
            if not nome:
                raise ValueError("O nome da categoria não pode ser vazio.")
            
            # Instancia com ID 0, o DAO Base vai auto-incrementar
            nova_categoria = Categoria(0, nome)
            CategoriaDAO.inserir(nova_categoria)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar categoria: {str(e)}")

    @classmethod
    def listar(cls):
        """Método chamado pela main.py para retornar todas as categorias"""
        try:
            return CategoriaDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao listar categorias: {str(e)}")

    @classmethod
    def atualizar_categoria(cls, id_categoria: int, novo_nome: str):
        try:
            if not novo_nome:
                raise ValueError("O novo nome não pode ser vazio.")
            
            # Cria o objeto atualizado mantendo o ID original
            categoria_atualizada = Categoria(id_categoria, novo_nome)
            CategoriaDAO.atualizar(categoria_atualizada)
        except Exception as e:
            raise Exception(f"Erro ao atualizar categoria: {str(e)}")

    @classmethod
    def deletar_categoria(cls, id_categoria: int):
        try:
            CategoriaDAO.excluir(id_categoria)
        except Exception as e:
            raise Exception(f"Erro ao deletar categoria: {str(e)}")