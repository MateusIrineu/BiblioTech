# Arquivo: Modules/Exemplar/ExemplarView.py
from Modules.Exemplar.ExemplarDAO import ExemplarDAO  # Camada de persistência específica de Exemplar
from Modules.Exemplar.Exemplar import Exemplar  # Modelo/entidade Exemplar
from Modules.Livro.LivroDAO import LivroDAO  # Necessário para validar se o Livro associado ao exemplar realmente existe

class ExemplarView:

    # ------------------------------------------------------------
    # CADASTRAR_EXEMPLAR: valida integridade referencial e duplicidade
    # antes de criar um novo Exemplar
    # ------------------------------------------------------------
    @classmethod
    def cadastrar_exemplar(cls, id_exemplar: int, id_livro: int, codigo_tombamento: str):
        if not codigo_tombamento.strip():  # Validação de campo obrigatório (fora do try, é um erro "de entrada" imediato)
            raise ValueError("Erro: O código de tombamento é obrigatório.")

        try:
            # Validar se o Livro base existe
            livros = LivroDAO.listar()  # Busca todos os livros cadastrados
            if not any(l.id == id_livro for l in livros):  # Verifica se algum deles tem o id_livro informado (integridade referencial)
                raise ValueError(f"Erro: Não é possível criar exemplar para um livro inexistente (ID {id_livro}).")

            # Validar se o ID ou código de tombamento já existem
            exemplares = ExemplarDAO.listar()  # Busca todos os exemplares já cadastrados
            if any(ex.id == id_exemplar for ex in exemplares):  # Impede reaproveitar um ID já existente
                raise ValueError(f"Erro: Já existe um exemplar com o ID {id_exemplar}.")
            if any(ex.codigo_tombamento == codigo_tombamento for ex in exemplares):  # Impede duplicar o código de tombamento (deve ser único)
                raise ValueError(f"Erro: Código de tombamento '{codigo_tombamento}' já está em uso.")

            novo_exemplar = Exemplar(id_exemplar, id_livro, codigo_tombamento, disponivel=True)  # Todo exemplar novo nasce como disponível
            ExemplarDAO.inserir(novo_exemplar)  # Delega a persistência para a camada de dados
            
        except ValueError as ve:
            raise ve  # Repropaga erros de validação (regra de negócio) sem alterar a mensagem
        except Exception as e:
            raise ValueError(f"Erro ao processar exemplar: {str(e)}")  # Qualquer outro erro inesperado é convertido em ValueError com mensagem genérica
        
    # ------------------------------------------------------------
    # LISTAR: repassa a listagem de exemplares vinda da DAO
    # ------------------------------------------------------------
    @classmethod
    def listar(cls):
        """Método chamado pela main.py para retornar todos os exemplares"""
        try:
            return ExemplarDAO.listar()  # Apenas repassa a chamada para a DAO, sem lógica adicional
        except Exception as e:
            raise Exception(f"Erro ao listar exemplares: {str(e)}")