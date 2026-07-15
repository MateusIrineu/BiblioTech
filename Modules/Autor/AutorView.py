# Arquivo: Modules/Autor/AutorView.py
from Modules.Autor.AutorDAO import AutorDAO  # Camada de persistência específica de Autor (usa apenas os métodos genéricos da DAO)
from Modules.Autor.Autor import Autor  # Modelo/entidade Autor

class AutorView:

    # ------------------------------------------------------------
    # CADASTRAR_AUTOR: valida o nome e cria um novo Autor
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_autor(cls, nome: str, nacionalidade: str):
        try:
            if not nome:  # Validação básica de campo obrigatório
                raise ValueError("O nome do autor não pode ser vazio.")
            
            # Instancia com ID 0. O DAO Base vai auto-incrementar e salvar!
            novo_autor = Autor(0, nome, nacionalidade)  # ID 0 é placeholder; DAO genérico substitui pelo ID real no inserir()
            AutorDAO.inserir(novo_autor)  # Delega a persistência para a camada de dados
        except Exception as e:
            raise Exception(f"Erro ao cadastrar autor: {str(e)}")

    # ------------------------------------------------------------
    # LISTAR: repassa a listagem de autores vinda da DAO
    # ------------------------------------------------------------
    @classmethod
    def listar(cls):
        try:
            return AutorDAO.listar()  # Apenas repassa a chamada para a DAO, sem lógica adicional
        except Exception as e:
            raise Exception(f"Erro ao listar autores: {str(e)}")

    # ------------------------------------------------------------
    # ATUALIZAR_AUTOR: valida o novo nome e atualiza mantendo o ID original
    # ------------------------------------------------------------
    @classmethod
    def atualizar_autor(cls, id_autor: int, novo_nome: str, nova_nacionalidade: str):
        try:
            if not novo_nome:  # Validação básica de campo obrigatório
                raise ValueError("O novo nome não pode ser vazio.")
            
            autor_atualizado = Autor(id_autor, novo_nome, nova_nacionalidade)  # Reaproveita o id_autor recebido (não é uma criação nova)
            AutorDAO.atualizar(autor_atualizado)  # A DAO localiza pelo id e substitui o objeto antigo por este
        except Exception as e:
            raise Exception(f"Erro ao atualizar autor: {str(e)}")

    # ------------------------------------------------------------
    # DELETAR_AUTOR: remove um autor pelo ID
    # ------------------------------------------------------------
    @classmethod
    def deletar_autor(cls, id_autor: int):
        try:
            AutorDAO.excluir(id_autor)  # Apenas repassa o ID para a DAO remover o registro correspondente
        except Exception as e:
            raise Exception(f"Erro ao deletar autor: {str(e)}")