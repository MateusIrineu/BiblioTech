# Arquivo: Modules/Usuario/UsuarioView.py
from Modules.Usuario.UsuarioDAO import UsuarioDAO
from Modules.Usuario.Usuario import Usuario

class UsuarioView:

    @classmethod
    def cadastrar_usuario(cls, nome: str, email: str, senha: str, perfil: str):
        try:
            if not nome or not email:
                raise ValueError("Nome e E-mail são obrigatórios para o cadastro.")
            
            # Instancia o Usuário com ID 0. O DAO Base vai auto-incrementar!
            novo_usuario = Usuario(0, nome, email, senha, perfil)
            UsuarioDAO.inserir(novo_usuario)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar usuário: {str(e)}")

    @classmethod
    def listar(cls):
        """Método padrão chamado pela main.py para listar todos os usuários"""
        try:
            return UsuarioDAO.listar()
        except Exception as e:
            raise Exception(f"Erro ao listar usuários: {str(e)}")

    @classmethod
    def atualizar_usuario(cls, id_usuario: int, novo_nome: str, novo_email: str, nova_senha: str, novo_perfil: str):
        try:
            if not novo_nome or not novo_email:
                raise ValueError("Nome e E-mail não podem ser vazios na atualização.")
            
            usuario_atualizado = Usuario(id_usuario, novo_nome, novo_email, nova_senha, novo_perfil)
            UsuarioDAO.atualizar(usuario_atualizado)
        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {str(e)}")

    @classmethod
    def deletar_usuario(cls, id_usuario: int):
        try:
            UsuarioDAO.excluir(id_usuario)
        except Exception as e:
            raise Exception(f"Erro ao deletar usuário: {str(e)}")