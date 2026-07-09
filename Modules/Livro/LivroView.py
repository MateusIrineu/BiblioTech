# Arquivo: Modules/Livro/LivroView.py
from Modules.Livro.LivroDAO import LivroDAO
from Modules.Livro.Livro import Livro

class LivroView:

    @classmethod
    def cadastrar_livro(cls, titulo: str, id_categoria: int, id_autor: int, id_editora: int):
        try:
            if not titulo:
                raise ValueError("O título do livro não pode ser vazio.")
            
            # Instancia com ID 0. O DAO Base vai interceptar e auto-incrementar!
            novo_livro = Livro(0, titulo, id_categoria, id_autor, id_editora)
            LivroDAO.inserir(novo_livro)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar livro: {str(e)}")

    @classmethod
    def listar(cls):
        """Método padrão chamado pela main.py para listar todos os livros"""
        try:
            return LivroDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao listar livros: {str(e)}")

    @classmethod
    def atualizar_livro(cls, id_livro: int, novo_titulo: str, novo_id_categoria: int, novo_id_autor: int, novo_id_editora: int):
        try:
            if not novo_titulo:
                raise ValueError("O título do livro não pode ser vazio.")
            
            livro_atualizado = Livro(id_livro, novo_titulo, novo_id_categoria, novo_id_autor, novo_id_editora)
            LivroDAO.atualizar(livro_atualizado)
        except Exception as e:
            raise Exception(f"Erro ao atualizar livro: {str(e)}")

    @classmethod
    def deletar_livro(cls, id_livro: int):
        try:
            LivroDAO.excluir(id_livro)
        except Exception as e:
            raise Exception(f"Erro ao deletar livro: {str(e)}")