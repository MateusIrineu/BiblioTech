# Arquivo: Autor.py

class Autor:
    def __init__(self, id_autor: int, nome: str, nacionalidade: str):
        self.id = id_autor                  # <-- ID DO AUTOR
        self.nome = nome                    # <-- NOME DO AUTOR
        self.nacionalidade = nacionalidade  # <-- NACIONALIDADE DO AUTOR

    def to_dict(self) -> dict:
        return {
            "id": self.id, 
            "nome": self.nome, 
            "nacionalidade": self.nacionalidade
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["nome"], dados["nacionalidade"])