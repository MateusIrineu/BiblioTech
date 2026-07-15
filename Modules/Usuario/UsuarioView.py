# Arquivo: Modules/Usuario/UsuarioView.py
from Modules.Usuario.UsuarioDAO import UsuarioDAO  # Camada de persistência específica de Usuario (herda de DAO)
from Modules.Usuario.Usuario import Usuario  # Modelo/entidade Usuario

class UsuarioView:

    # ------------------------------------------------------------
    # CADASTRAR_USUARIO: valida os dados e cria um novo Usuario
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_usuario(cls, nome: str, email: str, senha: str, perfil: str):
        try:
            if not nome or not email:  # Validação básica de campos obrigatórios
                raise ValueError("Nome e E-mail são obrigatórios para o cadastro.")
            
            # Instancia o Usuário com ID 0. O DAO Base vai auto-incrementar!
            novo_usuario = Usuario(0, nome, email, senha, perfil)  # ID 0 é só um placeholder; o DAO genérico substitui pelo ID real no inserir()
            UsuarioDAO.inserir(novo_usuario)  # Delega a persistência para a camada de dados
        except Exception as e:
            raise Exception(f"Erro ao cadastrar usuário: {str(e)}")  # Padroniza a mensagem de erro para a camada superior (menu)

    # ------------------------------------------------------------
    # LISTAR: repassa a listagem de usuários vinda da DAO
    # ------------------------------------------------------------
    @classmethod
    def listar(cls):
        """Método padrão chamado pela main.py para listar todos os usuários"""
        try:
            return UsuarioDAO.listar()  # Apenas repassa a chamada para a DAO, sem lógica adicional
        except Exception as e:
            raise Exception(f"Erro ao listar usuários: {str(e)}")

    # ------------------------------------------------------------
    # ATUALIZAR_USUARIO: valida e monta um Usuario atualizado, mantendo o ID original
    # ------------------------------------------------------------
    @classmethod
    def atualizar_usuario(cls, id_usuario: int, novo_nome: str, novo_email: str, nova_senha: str, novo_perfil: str):
        try:
            if not novo_nome or not novo_email:  # Validação básica de campos obrigatórios
                raise ValueError("Nome e E-mail não podem ser vazios na atualização.")
            
            usuario_atualizado = Usuario(id_usuario, novo_nome, novo_email, nova_senha, novo_perfil)  # Aqui o ID é o original (não é 0), pois é uma edição, não um novo cadastro
            UsuarioDAO.atualizar(usuario_atualizado)  # A DAO localiza pelo id e substitui o objeto antigo por este
        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {str(e)}")

    # ------------------------------------------------------------
    # DELETAR_USUARIO: remove um usuário pelo ID
    # ------------------------------------------------------------
    @classmethod
    def deletar_usuario(cls, id_usuario: int):
        try:
            UsuarioDAO.excluir(id_usuario)  # Apenas repassa o ID para a DAO remover o registro correspondente
        except Exception as e:
            raise Exception(f"Erro ao deletar usuário: {str(e)}")