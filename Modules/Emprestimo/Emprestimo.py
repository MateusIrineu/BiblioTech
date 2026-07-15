# Arquivo: Emprestimo.py

class Emprestimo:
    def __init__(self, id_emprestimo: int, id_exemplar: int, id_usuario: int, data_retirada: str, ativo: bool = True):
        self.id = id_emprestimo             # <-- ID DO EMPRÉSTIMO ESPEFÍFICO
        self.id_exemplar = id_exemplar      # <-- ID DO EXEMPLAR QUE ESTÁ LEVANDO / Associação com Exemplar (cópia física do Livro)
        self.id_usuario = id_usuario        # <-- ID DO USUÁRIO QUE ESTÁ FAZENDO EMPRÉSTIMO / Associação com Usuário
        self.data_retirada = data_retirada  # <-- DATA EM QUE SE FEZ O EMPRÉSTIMO
        self.ativo = ativo                  # <-- INDICA SE O EMPRÉSTIMO AINDA CORRE OU JÁ FOI FECHADO

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