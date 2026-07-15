# Arquivo: EditoraDAO.py
from DAO.DAO import DAO  # Importa a classe genérica DAO (classe mãe) com toda a lógica de persistência (CRUD em JSON)
from Modules.Editora.Editora import Editora  # Importa o modelo Editora

class EditoraDAO(DAO):
    arquivo = "editoras.json"   # Nome do arquivo JSON usado para persistir as editoras
    objetos = []                # Lista própria da subclasse (evita conflito com a lista da classe mãe DAO)
    classe_modelo = Editora     # Define qual classe será usada no from_dict() (polimorfismo) ao reconstruir os objetos

    # ------------------------------------------------------------
    # INSERIR: sobrescreve o inserir() genérico da DAO para adicionar
    # validações de negócio antes de efetivamente persistir a Editora
    # ------------------------------------------------------------
    # Note que esta versão NÃO gera o ID automaticamente como a DAO
    # genérica faz (max + 1); aqui já se espera receber "nova_editora"
    # com um id definido, e esse id é justamente o que será validado.
    @classmethod
    def inserir(cls, nova_editora):
        try:
            cls.abrir()  # Carrega as editoras já existentes no arquivo, para poder validar contra elas
            
            # Barreira de Segurança
            # Verifica se já existe alguma editora cadastrada com o mesmo ID
            if any(e.id == nova_editora.id for e in cls.objetos):
                raise ValueError(f"O ID {nova_editora.id} já está sendo utilizado por outra Editora.")
                
            # Verifica duplicidade por nome + cidade (case-insensitive, via lower()),
            # evitando cadastrar a mesma editora (mesma sede) duas vezes
            if any(e.nome.lower() == nova_editora.nome.lower() and e.cidade.lower() == nova_editora.cidade.lower() for e in cls.objetos):
                raise ValueError(f"A editora '{nova_editora.nome}' com sede em '{nova_editora.cidade}' já está cadastrada.")
                
            # Se passou pelas validações, delega para o inserir() da classe mãe (DAO),
            # que fará o append na lista e o salvar() no arquivo JSON
            super().inserir(nova_editora)
            
        except ValueError as ve:
            # Repropaga o erro de validação (regra de negócio) para quem chamou o método,
            # sem "abafar" a mensagem original (ex.: para ser tratada/exibida pela View)
            raise ve
        except Exception as e:
            # Qualquer outro erro inesperado (ex.: falha de I/O) é encapsulado
            # em uma exceção genérica com uma mensagem mais informativa
            raise Exception(f"Erro crítico ao tentar inserir a editora: {str(e)}")