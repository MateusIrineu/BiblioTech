# Arquivo: Exemplar.py

class Exemplar:
    def __init__(self, id_exemplar: int, id_livro: int, codigo_tombo: str, disponivel: bool = True):
        self.id = id_exemplar
        self.id_livro = id_livro          # Associação 1 para N com Livro
        self.codigo_tombo = codigo_tombo  # Identifica fisicamente a cópia (ex: patrimônio)
        self.disponivel = disponivel

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
