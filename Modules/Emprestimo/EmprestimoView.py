from Modules.Emprestimo.EmprestimoDAO import EmprestimoDAO
from Modules.Emprestimo.Emprestimo import Emprestimo

class EmprestimoView:

    @classmethod
    def solicitar_emprestimo(cls, id_exemplar: int, id_usuario: int, data_retirada: str):
        try:
            # 1. Instanciamos o objeto com ID 0 (o DAO vai substituir pelo auto-incremento).
            # Mudei de 'id_livro' para 'id_exemplar' para bater com a sua main.py e DAO.
            novo_emprestimo = Emprestimo(0, id_exemplar, id_usuario, data_retirada, ativo=True)
            
            # 2. Chamamos o método do DAO que faz toda a regra de negócio!
            sucesso = EmprestimoDAO.registrar_emprestimo(novo_emprestimo)
            
            if not sucesso:
                raise ValueError("A operação foi recusada pelo banco de dados (Exemplar indisponível ou erro interno).")

        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Falha crítica na transação de empréstimo: {str(e)}")

    @classmethod
    def registrar_devolucao(cls, id_emprestimo: int):
        try:
            # O DAO também já possui a regra de negócio completa para devolução
            sucesso = EmprestimoDAO.registrar_devolucao(id_emprestimo)
            
            if not sucesso:
                raise ValueError("Não foi possível processar a devolução. Verifique se o ID está correto e ativo.")

        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Erro ao processar devolução: {str(e)}")
        
    @classmethod
    def listar_emprestimos(cls):
        try:
            return EmprestimoDAO.listar_emprestimos()
        except Exception as e:
            raise Exception(f"Erro ao buscar o histórico de empréstimos: {str(e)}")