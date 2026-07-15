from Modules.Editora.Editora import Editora  # Modelo/entidade Editora
from Modules.Editora.EditoraDAO import EditoraDAO  # Camada de persistência específica de Editora (herda de DAO)

class EditoraView:

    # ------------------------------------------------------------
    # CADASTRAR_EDITORA: valida dados, verifica ID duplicado e cria Editora
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_editora(cls, id_editora: int, nome: str, cidade: str):
        # Validação básica de campos obrigatórios (removendo espaços em branco)
        if not nome.strip() or not cidade.strip():
            raise ValueError("Nome e cidade são obrigatórios.")

        try:
            # Recupera a lista atual para verificar se o ID fornecido já existe
            editoras = EditoraDAO.listar()
            if any(e.id == id_editora for e in editoras):
                raise ValueError(f"O ID {id_editora} já está sendo utilizado.")
            
            # Instancia o objeto Editora com o ID manual informado
            nova_editora = Editora(id_editora, nome, cidade)
            EditoraDAO.inserir(nova_editora)  # Delega a persistência para a camada de dados
            
        except ValueError as ve:
            raise ve  # Repassa o erro de validação específico (como ID duplicado ou campos vazios)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar editora: {str(e)}")  # Padroniza a mensagem de erro para a camada superior (menu)