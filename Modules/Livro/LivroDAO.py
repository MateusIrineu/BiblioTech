# Arquivo: LivroDAO.py
from DAO.DAO import DAO
from Modules.Livro.Livro import Livro

class LivroDAO(DAO):
    arquivo = "livros.json"
    objetos = []
    classe_modelo = Livro

    # ATENDE AO REQUISITO: Operação de Pesquisa Parcial
    @classmethod
    def pesquisar_por_titulo(cls, termo: str):
        cls.abrir()
        return [l for l in cls.objetos if termo.lower() in l.titulo.lower()]
    
    @classmethod
    def listar_livros(cls):
        try:
            return LivroDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao buscar livros: {str(e)}")
        
    @classmethod
    def atualizar_livro(cls, id_livro: int, novo_titulo: str, novo_id_categoria: int, novo_id_autor: int, novo_id_editora: int):
        if not novo_titulo.strip():
            raise ValueError("O título do livro não pode ser vazio.")
            
        try:
            livros = LivroDAO.listar()
            livro_alvo = next((l for l in livros if l.id == id_livro), None)
            
            if not livro_alvo:
                raise ValueError(f"Livro com ID {id_livro} não encontrado no acervo.")
            
            # Atualiza os dados do objeto em memória
            livro_alvo.titulo = novo_titulo
            livro_alvo.id_categoria = novo_id_categoria
            livro_alvo.id_autor = novo_id_autor
            livro_alvo.id_editora = novo_id_editora
            
            # Repassa para o DAO salvar no JSON
            LivroDAO.atualizar(livro_alvo)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Erro ao atualizar livro: {str(e)}")

    @classmethod
    def deletar_livro(cls, id_livro: int):
        try:
            livros = LivroDAO.listar()
            livro_alvo = next((l for l in livros if l.id == id_livro), None)
            
            if not livro_alvo:
                raise ValueError(f"Livro com ID {id_livro} não encontrado no acervo.")
            
            # IMPORTANTE: Em um sistema real, você bloquearia a exclusão se houvesse 
            # exemplares cadastrados para este livro.
            LivroDAO.excluir(id_livro)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Erro ao excluir livro: {str(e)}")