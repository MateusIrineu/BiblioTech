# Arquivo: Categoria.py

class Categoria:
    def __init__(self, id_categoria: int, nome: str):
        self.id = id_categoria  # <-- ID DA CATEGORIA
        self.nome = nome        # <-- NOME DA CATEGORIA

    def to_dict(self) -> dict:
        return {
            "id": self.id, 
            "nome": self.nome
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["nome"])