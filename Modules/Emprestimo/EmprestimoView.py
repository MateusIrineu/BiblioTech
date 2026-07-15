from Modules.Emprestimo.EmprestimoDAO import EmprestimoDAO  # Camada de persistência específica de Emprestimo
from Modules.Emprestimo.Emprestimo import Emprestimo  # Modelo/entidade Emprestimo

class EmprestimoView:

    # ------------------------------------------------------------
    # SOLICITAR_EMPRESTIMO: cria um novo empréstimo e delega regras à DAO
    # ------------------------------------------------------------
    @classmethod
    def solicitar_emprestimo(cls, id_exemplar: int, id_usuario: int, data_retirada: str):
        try:
            # Instancia o Emprestimo com ID 0. O DAO Base vai auto-incrementar!
            # ID 0 é só um placeholder; o DAO genérico substitui pelo ID real no inserir()
            novo_emprestimo = Emprestimo(0, id_exemplar, id_usuario, data_retirada, ativo=True)
            
            # Delega a persistência e validação de regras de negócio para a camada de dados
            sucesso = EmprestimoDAO.registrar_emprestimo(novo_emprestimo)
            
            if not sucesso:
                raise ValueError("A operação foi recusada pelo banco de dados (Exemplar indisponível ou erro interno).")

        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Falha crítica na transação de empréstimo: {str(e)}")  # Padroniza o erro para a camada superior

    # ------------------------------------------------------------
    # REGISTRAR_DEVOLUCAO: finaliza um empréstimo ativo
    # ------------------------------------------------------------
    @classmethod
    def registrar_devolucao(cls, id_emprestimo: int):
        try:
            # Delega a lógica de devolução e atualização do status do exemplar para a DAO
            sucesso = EmprestimoDAO.registrar_devolucao(id_emprestimo)
            
            if not sucesso:
                raise ValueError("Não foi possível processar a devolução. Verifique se o ID está correto e ativo.")

        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Erro ao processar devolução: {str(e)}")  # Padroniza o erro para a camada superior

    # ------------------------------------------------------------
    # LISTAR_EMPRESTIMOS: repassa a listagem de empréstimos vinda da DAO
    # ------------------------------------------------------------
    @classmethod
    def listar_emprestimos(cls):
        """Método padrão chamado pela main.py para listar todos os empréstimos"""
        try:
            return EmprestimoDAO.listar_emprestimos()  # Apenas repassa a chamada para a DAO, sem lógica adicional
        except Exception as e:
            raise Exception(f"Erro ao buscar o histórico de empréstimos: {str(e)}")