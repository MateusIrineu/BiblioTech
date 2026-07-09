from DAO.DAO import DAO
from Modules.Editora.Editora import Editora

class EditoraDAO(DAO):
    arquivo = "editoras.json"
    objetos = []
    classe_modelo = Editora

    @classmethod
    def inserir(cls, nova_editora):
        try:
            cls.abrir()
            
            # Barreira de Segurança
            if any(e.id == nova_editora.id for e in cls.objetos):
                raise ValueError(f"O ID {nova_editora.id} já está sendo utilizado por outra Editora.")
                
            if any(e.nome.lower() == nova_editora.nome.lower() and e.cidade.lower() == nova_editora.cidade.lower() for e in cls.objetos):
                raise ValueError(f"A editora '{nova_editora.nome}' com sede em '{nova_editora.cidade}' já está cadastrada.")
                
            super().inserir(nova_editora)
            
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Erro crítico ao tentar inserir a editora: {str(e)}")