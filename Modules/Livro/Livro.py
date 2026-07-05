# Arquivo: Livro.py

class Livro:
    def __init__(self, id_livro: int, titulo: str, id_categoria: int, id_autor: int, id_editora: int):
        self.id = id_livro
        self.titulo = titulo
        self.id_categoria = id_categoria  # Associação 1 para N
        self.id_autor = id_autor          # Associação 1 para N
        self.id_editora = id_editora      # Associação 1 para N
        # disponibilidade agora é responsabilidade do Exemplar (cópia física do livro)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "id_categoria": self.id_categoria,
            "id_autor": self.id_autor,
            "id_editora": self.id_editora
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
            dados["id"], dados["titulo"], dados["id_categoria"], 
            dados["id_autor"], dados["id_editora"]
        )