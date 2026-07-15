# Arquivo: Exemplar.py

class Exemplar:
    def __init__(self, id_exemplar: int, id_livro: int, codigo_tombo: str, disponivel: bool = True):
        self.id = id_exemplar             # <-- ID DO EXEMPLAR
        self.id_livro = id_livro          # <-- ID DO LIVRO  / Associação 1 para N com Livro
        self.codigo_tombo = codigo_tombo  # <-- CÓDIGO TOMBO / Identifica fisicamente a cópia (ex: patrimônio)
        self.disponivel = disponivel      # <-- IDENTIFICA SE EXEMPLAR ESTÁ OU NÃO DISPONÍVEL

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "id_livro": self.id_livro,
            "codigo_tombo": self.codigo_tombo,
            "disponivel": self.disponivel
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
            dados["id"], dados["id_livro"], dados["codigo_tombo"], dados["disponivel"]
        )
