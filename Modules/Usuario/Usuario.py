# Arquivo: Usuario.py

class Usuario:
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, perfil: str):
        self.id = id_usuario    # <-- ID DO USUÁRIO
        self.nome = nome        # <-- NOME DO USUÁRIO
        self.email = email      # <-- EMAIL DO USUÁRIO
        self.senha = senha      # <-- SENHA DO USUÁRIO
        self.perfil = perfil    # <-- IDENTIFICA QUEM ESTÁ LOGANDO / 'admin' (BIBLIOTECÁRIO) OU 'leitor' (CLIENTE)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "perfil": self.perfil
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["nome"], dados["email"], dados["senha"], dados["perfil"])