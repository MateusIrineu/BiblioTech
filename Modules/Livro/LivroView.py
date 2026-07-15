# Arquivo: Modules/Livro/LivroView.py
from Modules.Livro.LivroDAO import LivroDAO  # Camada de persistência específica de Livro (herda de DAO)
from Modules.Livro.Livro import Livro  # Modelo/entidade Livro

class LivroView:

    # ------------------------------------------------------------
    # CADASTRAR_LIVRO: valida os dados e cria um novo Livro
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_livro(cls, titulo: str, id_categoria: int, id_autor: int, id_editora: int):
        try:
            if not titulo:  # Validação básica de campos obrigatórios
                raise ValueError("O título do livro não pode ser vazio.")
            
            # Instancia o Livro com ID 0. O DAO Base vai auto-incrementar! (ID 0 é só um placeholder)
            novo_livro = Livro(0, titulo, id_categoria, id_autor, id_editora)
            LivroDAO.inserir(novo_livro)  # Delega a persistência para a camada de dados
        except Exception as e:
            raise Exception(f"Erro ao cadastrar livro: {str(e)}")  # Padroniza a mensagem de erro para a camada superior (menu)

    # ------------------------------------------------------------
    # LISTAR: repassa a listagem de livros vinda da DAO
    # ------------------------------------------------------------
    @classmethod
    def listar(cls):
        """Método padrão chamado pela main.py para listar todos os livros"""
        try:
            return LivroDAO.listar()  # Apenas repassa a chamada para a DAO, sem lógica adicional
        except Exception as e:
            raise Exception(f"Erro ao listar livros: {str(e)}")  # Padroniza a exceção para a camada superior

    # ------------------------------------------------------------
    # ATUALIZAR_LIVRO: valida e monta um Livro atualizado, mantendo o ID original
    # ------------------------------------------------------------
    @classmethod
    def atualizar_livro(cls, id_livro: int, novo_titulo: str, novo_id_categoria: int, novo_id_autor: int, novo_id_editora: int):
        try:
            if not novo_titulo:  # Validação básica de campos obrigatórios
                raise ValueError("O título do livro não pode ser vazio.")
            
            livro_atualizado = Livro(id_livro, novo_titulo, novo_id_categoria, novo_id_autor, novo_id_editora)  # Aqui o ID é o original (não é 0), pois é uma edição
            LivroDAO.atualizar(livro_atualizado)  # A DAO localiza pelo id e substitui o objeto antigo por este
        except Exception as e:
            raise Exception(f"Erro ao atualizar livro: {str(e)}")  # Padroniza a mensagem de erro para a camada superior (menu)

    # ------------------------------------------------------------
    # DELETAR_LIVRO: remove um livro pelo ID
    # ------------------------------------------------------------
    @classmethod
    def deletar_livro(cls, id_livro: int):
        try:
            LivroDAO.excluir(id_livro)  # Apenas repassa o ID para a DAO remover o registro correspondente
        except Exception as e:
            raise Exception(f"Erro ao deletar livro: {str(e)}")  # Padroniza a mensagem de erro para a camada superior (menu)
