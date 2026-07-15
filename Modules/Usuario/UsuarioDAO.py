# Arquivo: UsuarioDAO.py
from DAO.DAO import DAO
from Modules.Usuario.Usuario import Usuario

class UsuarioDAO(DAO):
    arquivo = "usuarios.json"   # Nome do arquivo JSON usado para persistir os usuários
    objetos = []                # Lista própria da subclasse (evita conflito com a lista da classe mãe DAO)
    classe_modelo = Usuario     # Define qual classe será usada no from_dict() (polimorfismo) ao reconstruir os objetos