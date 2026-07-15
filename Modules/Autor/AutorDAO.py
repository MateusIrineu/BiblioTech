# Arquivo: AutorDAO.py
from DAO.DAO import DAO
from Modules.Autor.Autor import Autor

class AutorDAO(DAO):
    arquivo = "autores.json"    # Nome do arquivo JSON usado para persistir os autores
    objetos = []                # Lista própria da subclasse (evita conflito com a lista da classe mãe DAO)
    classe_modelo = Autor       # Define qual classe será usada no from_dict() (polimorfismo) ao reconstruir os objetos