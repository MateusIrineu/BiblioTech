# Arquivo: Modules/Exemplar/ExemplarView.py
from Modules.Exemplar.ExemplarDAO import ExemplarDAO
from Modules.Exemplar.Exemplar import Exemplar
from Modules.Livro.LivroDAO import LivroDAO

class ExemplarView:

    @classmethod
    def cadastrar_exemplar(cls, id_exemplar: int, id_livro: int, codigo_tombamento: str):
        if not codigo_tombamento.strip():
            raise ValueError("Erro: O código de tombamento é obrigatório.")

        try:
            # Validar se o Livro base existe
            livros = LivroDAO.listar()
            if not any(l.id == id_livro for l in livros):
                raise ValueError(f"Erro: Não é possível criar exemplar para um livro inexistente (ID {id_livro}).")

            # Validar se o ID ou código de tombamento já existem
            exemplares = ExemplarDAO.listar()
            if any(ex.id == id_exemplar for ex in exemplares):
                raise ValueError(f"Erro: Já existe um exemplar com o ID {id_exemplar}.")
            if any(ex.codigo_tombamento == codigo_tombamento for ex in exemplares):
                raise ValueError(f"Erro: Código de tombamento '{codigo_tombamento}' já está em uso.")

            novo_exemplar = Exemplar(id_exemplar, id_livro, codigo_tombamento, disponivel=True)
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
            raise Exception(f"Erro ao listar categorias: {str(e)}")