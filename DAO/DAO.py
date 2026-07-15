# Arquivo: DAO.py
import json
import os

class DAO:
    # Atributos de classe (compartilhados/sobrescritos pelas subclasses):
    arquivo = ""        # Nome do arquivo JSON onde os dados serão persistidos (definido em cada DAO filha)
    objetos = []         # Lista em memória com os objetos atualmente carregados do arquivo
    classe_modelo = None  # Referência à classe do modelo (ex.: Livro, Autor) usada para reconstrução via polimorfismo

    # ------------------------------------------------------------
    # INSERIR: adiciona um novo objeto à lista e persiste no JSON
    # ------------------------------------------------------------
    # Recebe "obj", uma instância do modelo (ex.: um objeto Livro),
    # já criada pela camada de View/Controller (ex.: LivroView).
    @classmethod
    def inserir(cls, obj):
        cls.abrir()  # Primeiro carrega os dados já existentes do arquivo, garantindo que a lista esteja atualizada
        
        # --- LÓGICA DE AUTO-INCREMENTO GENÉRICO ---
        # Varre os objetos da classe filha, pega o maior ID e soma 1.
        # Caso a lista esteja vazia, assume 0 e soma 1 (primeiro ID será 1).
        novo_id = max([o.id for o in cls.objetos], default=0) + 1
        
        # Atribui o novo ID gerado ao objeto antes de salvá-lo
        obj.id = novo_id
        
        cls.objetos.append(obj)  # Adiciona o novo objeto (já com ID definido) à lista em memória
        cls.salvar()  # Grava a lista atualizada de volta no arquivo JSON

    # ------------------------------------------------------------
    # LISTAR: retorna todos os objetos persistidos no arquivo
    # ------------------------------------------------------------
    # Usado pelas Views para exibir listas (ex.: listar() em LivroView,
    # AutorView, EditoraView, UsuarioView, conforme diagrama de classes)
    @classmethod
    def listar(cls):
        cls.abrir()  # Recarrega os dados do arquivo antes de retornar, garantindo informação atualizada
        return cls.objetos

    # ------------------------------------------------------------
    # ATUALIZAR: substitui um objeto existente por uma versão nova
    # ------------------------------------------------------------
    # Recebe "obj_atualizado", um objeto do mesmo tipo já com os
    # novos valores e o MESMO id do objeto original (ex.: chamado
    # por atualizar_livro(), atualizar_autor() etc. nas Views)
    @classmethod
    def atualizar(cls, obj_atualizado):
        cls.abrir()  # Carrega o estado atual do arquivo
        for i, obj in enumerate(cls.objetos):
            if obj.id == obj_atualizado.id:  # Localiza o objeto pelo ID (chave de identidade)
                cls.objetos[i] = obj_atualizado  # Substitui o objeto antigo pelo atualizado na mesma posição
                break  # Para o laço assim que encontra e atualiza (ids são únicos)
        cls.salvar()  # Persiste a lista já modificada no arquivo JSON

    # ------------------------------------------------------------
    # EXCLUIR: remove um objeto da lista a partir do seu ID
    # ------------------------------------------------------------
    # Recebe apenas o "id_obj" (int), não o objeto inteiro, pois é
    # o suficiente para localizar e remover o registro correspondente.
    @classmethod
    def excluir(cls, id_obj):
        cls.abrir()  # Carrega o estado atual do arquivo
        cls.objetos = [obj for obj in cls.objetos if obj.id != id_obj]  # Recria a lista mantendo apenas quem NÃO tem o id informado
        cls.salvar()  # Persiste a lista já sem o objeto excluído

    # ------------------------------------------------------------
    # SALVAR: grava a lista de objetos em memória no arquivo JSON
    # ------------------------------------------------------------
    # Converte cada objeto do modelo (Livro, Autor, Usuario...) em
    # um dicionário usando o método to_dict() de cada classe (ver
    # diagrama de classes: todos os modelos implementam to_dict()),
    # e então serializa essa lista de dicionários como JSON.
    @classmethod
    def salvar(cls):
        caminho_arquivo = os.path.join("Jsons", cls.arquivo)  # Monta o caminho até o arquivo (ex.: Jsons/livros.json)
        with open(caminho_arquivo, mode="w", encoding="utf-8") as f:
            lista_dicts = [obj.to_dict() for obj in cls.objetos]  # Polimorfismo: cada obj sabe se converter para dict
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)  # Grava formatado e preservando acentuação (ensure_ascii=False)

    # ------------------------------------------------------------
    # ABRIR: lê o arquivo JSON e reconstrói os objetos em memória
    # ------------------------------------------------------------
    # É o método "espelho" do salvar(): em vez de transformar objetos
    # em dicionários, ele transforma dicionários de volta em objetos.
    @classmethod
    def abrir(cls):
        cls.objetos = []  # Zera a lista em memória antes de recarregar, evitando duplicar dados
        caminho_arquivo = os.path.join("Jsons", cls.arquivo)  # Caminho do arquivo correspondente à DAO filha
        if os.path.exists(caminho_arquivo):  # Só tenta ler se o arquivo já existir (evita erro na primeira execução)
            with open(caminho_arquivo, mode="r", encoding="utf-8") as f:
                texto = f.read()
                if texto.strip():  # Verifica se o arquivo não está vazio antes de tentar decodificar JSON
                    lista_dicts = json.loads(texto)
                    # Polimorfismo: reconstrói dinamicamente os objetos baseados na classe filha
                    # cls.classe_modelo é definido por cada DAO filha (ex.: LivroDAO -> Livro),
                    # e from_dict() é o método de cada modelo responsável por recriar a instância
                    # a partir do dicionário lido do JSON.
                    cls.objetos = [cls.classe_modelo.from_dict(d) for d in lista_dicts]