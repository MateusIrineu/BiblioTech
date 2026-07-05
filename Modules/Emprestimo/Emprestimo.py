# Arquivo: Emprestimo.py

class Emprestimo:
    def __init__(self, id_emprestimo: int, id_exemplar: int, id_usuario: int, data_retirada: str, ativo: bool = True):
        self.id = id_emprestimo
        self.id_exemplar = id_exemplar  # Associação com Exemplar (cópia física do Livro)
        self.id_usuario = id_usuario    # Associação com Usuário
        self.data_retirada = data_retirada
        self.ativo = ativo

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "id_exemplar": self.id_exemplar,
            "id_usuario": self.id_usuario,
            "data_retirada": self.data_retirada,
            "ativo": self.ativo
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["id_exemplar"], dados["id_usuario"], dados["data_retirada"], dados["ativo"])