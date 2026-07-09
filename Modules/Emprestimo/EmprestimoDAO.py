from DAO.DAO import DAO
from Modules.Emprestimo.Emprestimo import Emprestimo
from Modules.Exemplar.ExemplarDAO import ExemplarDAO

class EmprestimoDAO(DAO):
    arquivo = "emprestimos.json"
    objetos = []
    classe_modelo = Emprestimo

    # ATENDE AO REQUISITO: Regra de negócio complexa envolvendo múltiplas entidades
    @classmethod
    def registrar_emprestimo(cls, novo_emprestimo):
        cls.abrir()

        # 1. Busca o exemplar correspondente via ExemplarDAO para verificar a disponibilidade
        exemplares = ExemplarDAO.listar()
        exemplar_encontrado = None
        for e in exemplares:
            if e.id == novo_emprestimo.id_exemplar:
                exemplar_encontrado = e
                break

        # 2. Aplica a Regra de Negócio: Se o exemplar existe e está disponível, realiza a operação
        if exemplar_encontrado and exemplar_encontrado.disponivel:
            # Altera a entidade Exemplar (Status passa a ser Indisponível)
            exemplar_encontrado.disponivel = False
            ExemplarDAO.atualizar(exemplar_encontrado)

            # 3. Insere o novo empréstimo (A classe DAO mãe vai gerar o ID automaticamente aqui!)
            cls.inserir(novo_emprestimo)
            
            print(f"-> SUCESSO: O exemplar '{exemplar_encontrado.codigo_tombo}' foi emprestado.")
            return True
        else:
            print(f"-> ERRO: Não foi possível emprestar. Exemplar ocupado ou inexistente.")
            return False

    # ATENDE AO REQUISITO: Regra de negócio complementar (devolução)
    @classmethod
    def registrar_devolucao(cls, id_emprestimo: int):
        cls.abrir()

        emprestimo_encontrado = None
        for emp in cls.objetos:
            if emp.id == id_emprestimo and emp.ativo:
                emprestimo_encontrado = emp
                break

        if not emprestimo_encontrado:
            print("-> ERRO: Empréstimo ativo não encontrado.")
            return False

        exemplares = ExemplarDAO.listar()
        for e in exemplares:
            if e.id == emprestimo_encontrado.id_exemplar:
                e.disponivel = True
                ExemplarDAO.atualizar(e)
                break

        emprestimo_encontrado.ativo = False
        cls.atualizar(emprestimo_encontrado)
        print(f"-> SUCESSO: Devolução do empréstimo {id_emprestimo} registrada.")
        return True
    
    @classmethod
    def listar_emprestimos(cls):
        try:
            return cls.listar()
        except Exception as e:
            raise Exception(f"Erro ao buscar o histórico de empréstimos: {str(e)}")