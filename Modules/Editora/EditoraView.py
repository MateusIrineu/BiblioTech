from Modules.Editora.EditoraDAO import EditoraDAO
from Modules.Editora.Editora import Editora

class EditoraView:

    @classmethod
    def cadastrar_editora(cls, nome: str, cidade: str):
        try:
            if not nome or not cidade:
                raise ValueError("Nome e cidade são obrigatórios.")

            # Instancia com ID 0, o DAO Base vai auto-incrementar
            nova_editora = Editora(0, nome, cidade)
            EditoraDAO.inserir(nova_editora)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar editora: {str(e)}")

    @classmethod
    def listar(cls):
        """Método chamado pela main.py para retornar todas as editoras"""
        try:
            return EditoraDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao listar editoras: {str(e)}")

    @classmethod
    def atualizar_editora(cls, id_editora: int, novo_nome: str, nova_cidade: str):
        try:
            if not novo_nome or not nova_cidade:
                raise ValueError("Nome e cidade são obrigatórios.")

            editora_atualizada = Editora(id_editora, novo_nome, nova_cidade)
            EditoraDAO.atualizar(editora_atualizada)
        except Exception as e:
            raise Exception(f"Erro ao atualizar editora: {str(e)}")

    @classmethod
    def deletar_editora(cls, id_editora: int):
        try:
            EditoraDAO.excluir(id_editora)
        except Exception as e:
            raise Exception(f"Erro ao deletar editora: {str(e)}")
