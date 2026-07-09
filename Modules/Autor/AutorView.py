# Arquivo: Modules/Autor/AutorView.py
from Modules.Autor.AutorDAO import AutorDAO
from Modules.Autor.Autor import Autor

class AutorView:

    @classmethod
    def cadastrar_autor(cls, nome: str, nacionalidade: str):
        try:
            if not nome:
                raise ValueError("O nome do autor não pode ser vazio.")
            
            # Instancia com ID 0. O DAO Base vai auto-incrementar e salvar!
            novo_autor = Autor(0, nome, nacionalidade)
            AutorDAO.inserir(novo_autor)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar autor: {str(e)}")

    @classmethod
    def listar(cls):
        try:
            return AutorDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao listar autores: {str(e)}")

    @classmethod
    def atualizar_autor(cls, id_autor: int, novo_nome: str, nova_nacionalidade: str):
        try:
            if not novo_nome:
                raise ValueError("O novo nome não pode ser vazio.")
            
            autor_atualizado = Autor(id_autor, novo_nome, nova_nacionalidade)
            AutorDAO.atualizar(autor_atualizado)
        except Exception as e:
            raise Exception(f"Erro ao atualizar autor: {str(e)}")

    @classmethod
    def deletar_autor(cls, id_autor: int):
        try:
            AutorDAO.excluir(id_autor)
        except Exception as e:
            raise Exception(f"Erro ao deletar autor: {str(e)}")