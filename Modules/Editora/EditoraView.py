from Modules.Editora.EditoraDAO import EditoraDAO  # Camada de persistência específica de Editora (com validações próprias no inserir())
from Modules.Editora.Editora import Editora  # Modelo/entidade Editora

class EditoraView:
    # ------------------------------------------------------------
    # CADASTRAR_EDITORA: valida campos obrigatórios e duplicidade de ID
    # antes de delegar a criação para a EditoraDAO
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_editora(cls, id_editora: int, nome: str, cidade: str):
        if not nome.strip() or not cidade.strip():  # Validação de campos obrigatórios (fora do try, erro de entrada imediato)
            raise ValueError("Nome e cidade são obrigatórios.")

    @classmethod
    def cadastrar_editora(cls, nome: str, cidade: str):
        try:
            editoras = EditoraDAO.listar()  # Busca todas as editoras já cadastradas
            if any(e.id == id_editora for e in editoras):  # Verifica se o ID informado já está em uso (validação também repetida no DAO)
                raise ValueError(f"O ID {id_editora} já está sendo utilizado.")
            
            nova_editora = Editora(id_editora, nome, cidade)  # Monta o objeto com o ID já definido pelo usuário/chamador
            EditoraDAO.inserir(nova_editora)  # Delega a persistência (que fará validações adicionais de negócio)
        except ValueError as ve:
            raise ve  # Repropaga erros de validação sem alterar a mensagem
        except Exception as e:
            raise Exception(f"Erro ao cadastrar editora: {str(e)}")  # Encapsula qualquer outro erro inesperado
