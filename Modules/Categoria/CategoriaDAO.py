# Dentro de Modules/Categoria/CategoriaDAO.py
from DAO.DAO import DAO  # Aponta para a pasta DAO e depois para o arquivo DAO.py
from Modules.Categoria.Categoria import Categoria # Aponta o caminho completo da entidade

class CategoriaDAO(DAO):
    arquivo = "categorias.json"     # Nome do arquivo JSON usado para persistir as categorias
    objetos = []                    # Lista própria da subclasse (evita conflito com a lista da classe mãe DAO)
    classe_modelo = Categoria       # Define qual classe será usada no from_dict() (polimorfismo) ao reconstruir os objetos