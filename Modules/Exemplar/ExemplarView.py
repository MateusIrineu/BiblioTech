# Arquivo: Modules/Exemplar/ExemplarView.py
from Modules.Exemplar.ExemplarDAO import ExemplarDAO
from Modules.Exemplar.Exemplar import Exemplar
from Modules.Livro.LivroDAO import LivroDAO

class ExemplarView:

    @classmethod
    def cadastrar_exemplar(cls, id_livro: int, codigo_tombo: str):
        if not codigo_tombo.strip():
            raise ValueError("Erro: O código de tombamento é obrigatório.")

        try:
            # Validar se o Livro base existe
            livros = LivroDAO.listar()
            if not any(l.id == id_livro for l in livros):
                raise ValueError(f"Erro: Não é possível criar exemplar para um livro inexistente (ID {id_livro}).")

            # Validar se o código de tombamento já existe
            exemplares = ExemplarDAO.listar()
            if any(ex.codigo_tombo == codigo_tombo for ex in exemplares):
                raise ValueError(f"Erro: Código de tombamento '{codigo_tombo}' já está em uso.")

            # Instancia com ID 0, o DAO Base vai auto-incrementar
            novo_exemplar = Exemplar(0, id_livro, codigo_tombo, disponivel=True)
            ExemplarDAO.inserir(novo_exemplar)

        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Erro ao processar exemplar: {str(e)}")

    @classmethod
    def listar(cls):
        """Método chamado pela main.py para retornar todos os exemplares"""
        try:
            return ExemplarDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao listar exemplares: {str(e)}")

    @classmethod
    def atualizar_exemplar(cls, id_exemplar: int, id_livro: int, codigo_tombo: str):
        if not codigo_tombo.strip():
            raise ValueError("Erro: O código de tombamento é obrigatório.")

        try:
            livros = LivroDAO.listar()
            if not any(l.id == id_livro for l in livros):
                raise ValueError(f"Erro: Livro inexistente (ID {id_livro}).")

            exemplares = ExemplarDAO.listar()
            exemplar_alvo = next((ex for ex in exemplares if ex.id == id_exemplar), None)
            if not exemplar_alvo:
                raise ValueError(f"Exemplar com ID {id_exemplar} não encontrado.")

            if any(ex.codigo_tombo == codigo_tombo and ex.id != id_exemplar for ex in exemplares):
                raise ValueError(f"Erro: Código de tombamento '{codigo_tombo}' já está em uso.")

            exemplar_atualizado = Exemplar(id_exemplar, id_livro, codigo_tombo, exemplar_alvo.disponivel)
            ExemplarDAO.atualizar(exemplar_atualizado)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Erro ao atualizar exemplar: {str(e)}")

    @classmethod
    def deletar_exemplar(cls, id_exemplar: int):
        try:
            ExemplarDAO.excluir(id_exemplar)
        except Exception as e:
            raise Exception(f"Erro ao deletar exemplar: {str(e)}")
