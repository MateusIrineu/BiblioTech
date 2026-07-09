from Modules.Editora.EditoraDAO import EditoraDAO
from Modules.Editora.Editora import Editora

class EditoraView:
    @classmethod
    def cadastrar_editora(cls, id_editora: int, nome: str, cidade: str):
        if not nome.strip() or not cidade.strip():
            raise ValueError("Nome e cidade são obrigatórios.")

        try:
            editoras = EditoraDAO.listar()
            if any(e.id == id_editora for e in editoras):
                raise ValueError(f"O ID {id_editora} já está sendo utilizado.")
            
            nova_editora = Editora(id_editora, nome, cidade)
            EditoraDAO.inserir(nova_editora)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Erro ao cadastrar editora: {str(e)}")