import sys

# ==========================================
# IMPORTAÇÕES EXCLUSIVAS DAS VIEWS (MURALHAS)
# ==========================================
from Modules.Categoria.CategoriaView import CategoriaView
from Modules.Autor.AutorView import AutorView
from Modules.Editora.EditoraView import EditoraView
from Modules.Livro.LivroView import LivroView
from Modules.Exemplar.ExemplarView import ExemplarView
from Modules.Usuario.UsuarioView import UsuarioView
from Modules.Emprestimo.EmprestimoView import EmprestimoView


# ==========================================
# MODULO 1: CADASTROS BÁSICOS (ADMIN)
# ==========================================
def menu_gerenciar_categorias():
    while True:
        print("\n=== GERENCIAR CATEGORIAS ===")
        print("1. Cadastrar Categoria")
        print("2. Listar Categorias")
        print("3. Atualizar Categoria")
        print("4. Deletar Categoria")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\n-- Nova Categoria --")
            try:
                nome = input("Nome da Categoria: ").strip()
                CategoriaView.cadastrar_categoria(nome)
                print("✅ Categoria cadastrada com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "2":
            print("\n-- Lista de Categorias --")
            try:
                categorias = CategoriaView.listar()
                if not categorias:
                    print("Nenhuma categoria cadastrada ainda.")
                else:
                    for cat in categorias:
                        print(f"ID: {cat.id} | Nome: {cat.nome}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "3":
            print("\n-- Atualizar Categoria --")
            try:
                id_cat = int(input("Digite o ID da categoria que deseja alterar: "))
                novo_nome = input("Digite o NOVO nome: ").strip()
                CategoriaView.atualizar_categoria(id_cat, novo_nome)
                print("✅ Categoria actualizada com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "4":
            print("\n-- Deletar Categoria --")
            try:
                id_cat = int(input("Digite o ID da categoria a ser excluída: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_cat}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    CategoriaView.deletar_categoria(id_cat)
                    print("✅ Categoria excluída com sucesso!")
                else:
                    print("Operação cancelada.")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


def menu_cadastros_basicos():
    while True:
        print("\n=== CADASTROS BÁSICOS ===")
        print("1. Gerenciar Categorias (CRUD Completo)")
        print("2. Cadastrar Autor")
        print("3. Cadastrar Editora")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            menu_gerenciar_categorias()
        elif opcao == "2":
            print("\n-- Novo Autor --")
            try:
                nome = input("Nome: ").strip()
                nacionalidade = input("Nacionalidade: ").strip()
                AutorView.cadastrar_autor(nome, nacionalidade)
                print("✅ Autor cadastrado com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "3":
            print("\n-- Nova Editora --")
            try:
                nome = input("Nome: ").strip()
                cidade = input("Cidade: ").strip()
                EditoraView.cadastrar_editora(nome, cidade)
                print("✅ Editora cadastrada com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


# ==========================================
# MODULO 2: GERENCIAR ACERVO
# ==========================================
def submenu_gestao_livros():
    while True:
        print("\n--- GESTÃO DE LIVROS ---")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\n-- Novo Livro --")
            try:
                titulo = input("Título: ").strip()
                id_categoria = int(input("ID da Categoria referente: "))
                id_autor = int(input("ID do Autor referente: "))
                id_editora = int(input("ID da Editora referente: "))
                LivroView.cadastrar_livro(titulo, id_categoria, id_autor, id_editora)
                print("✅ Livro cadastrado com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "2":
            print("\n-- Lista de Livros no Acervo --")
            try:
                livros = LivroView.listar()
                if not livros:
                    print("Nenhum livro cadastrado no momento.")
                else:
                    for livro in livros:
                        print(f"ID: {livro.id} | Título: {livro.titulo} | Categoria ID: {livro.id_categoria} | Autor ID: {livro.id_autor}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "3":
            print("\n-- Atualizar Livro --")
            try:
                id_livro = int(input("Digite o ID do livro que deseja atualizar: "))
                print("Preencha os novos dados:")
                novo_titulo = input("Novo Título: ").strip()
                novo_id_categoria = int(input("Novo ID da Categoria: "))
                novo_id_autor = int(input("Novo ID do Autor: "))
                novo_id_editora = int(input("Novo ID da Editora: "))
                LivroView.atualizar_livro(id_livro, novo_titulo, novo_id_categoria, novo_id_autor, novo_id_editora)
                print("✅ Livro atualizado com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "4":
            print("\n-- Deletar Livro --")
            try:
                id_livro = int(input("Digite o ID do livro a ser excluído: "))
                confirmacao = input(f"Confirma a exclusão do livro {id_livro}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    LivroView.deletar_livro(id_livro)
                    print("✅ Livro excluído com sucesso!")
                else:
                    print("Operação cancelada.")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


def submenu_gestao_exemplares():
    while True:
        print("\n--- GESTÃO DE EXEMPLARES ---")
        print("1. Cadastrar Exemplar (Cópia Física)")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\n-- Novo Exemplar --")
            try:
                id_livro = int(input("ID do Livro Referente: "))
                codigo = input("Código de Tombamento: ").strip()
                ExemplarView.cadastrar_exemplar(id_livro, codigo)
                print("✅ Exemplar adicionado ao acervo!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


def menu_acervo():
    while True:
        print("\n=== GERENCIAR ACERVO ===")
        print("1. Gestão de Livros")
        print("2. Gestão de Exemplares")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            submenu_gestao_livros()
        elif opcao == "2":
            submenu_gestao_exemplares()
        else:
            print("⚠️ Opção inválida!")


# ==========================================
# MODULO 3: OPERAÇÕES (ADMIN)
# ==========================================
def submenu_gestao_usuarios():
    while True:
        print("\n--- GESTÃO DE USUÁRIOS ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\n-- Novo Usuário --")
            try:
                nome = input("Nome: ").strip()
                email = input("E-mail: ").strip()
                senha = input("Senha: ").strip()
                perfil = input("Perfil (admin/leitor): ").strip()
                UsuarioView.cadastrar_usuario(nome, email, senha, perfil)
                print("✅ Usuário cadastrado com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "2":
            print("\n-- Lista de Usuários --")
            try:
                usuarios = UsuarioView.listar()
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                else:
                    for u in usuarios:
                        print(f"ID: {u.id} | Nome: {u.nome} | E-mail: {u.email} | Perfil: {u.perfil}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "3":
            print("\n-- Atualizar Usuário --")
            try:
                id_user = int(input("Digite o ID do usuário que deseja atualizar: "))
                print("Preencha os novos dados:")
                novo_nome = input("Novo Nome: ").strip()
                novo_email = input("Novo E-mail: ").strip()
                nova_senha = input("Nova Senha: ").strip()
                novo_perfil = input("Novo Perfil (admin/leitor): ").strip()
                UsuarioView.atualizar_usuario(id_user, novo_nome, novo_email, nova_senha, novo_perfil)
                print("✅ Usuário atualizado com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "4":
            print("\n-- Deletar Usuário --")
            try:
                id_user = int(input("Digite o ID do usuário a ser excluído: "))
                confirmacao = input(f"Confirma a exclusão do usuário {id_user}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    UsuarioView.deletar_usuario(id_user)
                    print("✅ Usuário excluído com sucesso!")
                else:
                    print("Operação cancelada.")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


def submenu_consultas_gerais():
    while True:
        print("\n--- CONSULTAS GERAIS ---")
        print("1. Histórico de Empréstimos e Devoluções")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\n-- Histórico de Empréstimos e Devoluções --")
            try:
                emprestimos = EmprestimoView.listar_emprestimos()
                if not emprestimos:
                    print("Nenhuma transação registrada no momento.")
                else:
                    for emp in emprestimos:
                        status = "🟡 ATIVO (Emprestado)" if getattr(emp, 'ativo', True) else "🟢 DEVOLVIDO"
                        print(f"ID Empréstimo: {emp.id} | ID Exemplar: {emp.id_exemplar} | ID Leitor: {emp.id_usuario} | Retirada: {getattr(emp, 'data_retirada', 'N/D')} | Status: {status}")
            except AttributeError as ae:
                print(f"❌ Erro de Atributo: Verifique os nomes das variáveis na sua classe Emprestimo. Detalhe: {ae}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


def submenu_transacoes():
    while True:
        print("\n--- TRANSAÇÕES ---")
        print("1. Solicitar Empréstimo")
        print("2. Registrar Devolução")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\n-- Novo Empréstimo --")
            try:
                print("\nListando exemplares cadastrados para consulta de IDs:")
                try:
                    exemplares = ExemplarView.listar()
                    if not exemplares:
                        print("⚠️ Atenção: Não existem exemplares cadastrados no acervo.")
                    else:
                        for ex in exemplares:
                            status = "🟢 DISPONÍVEL" if getattr(ex, 'disponivel', True) else "🔴 INDISPONÍVEL"
                            print(f"   👉 [ID Exemplar: {ex.id}] | Livro ID: {ex.id_livro} | Tombo: {getattr(ex, 'codigo_tombamento', getattr(ex, 'codigo_tombo', 'N/D'))} | Status: {status}")
                except Exception:
                    print("⚠️ Não foi possível listar os exemplares automaticamente.")
                
                print("-" * 50)
                id_exemplar = int(input("ID do Exemplar Desejado: "))
                id_user = int(input("ID do Usuário Leitor: "))
                data = input("Data de Retirada (DD/MM/AAAA): ").strip()
                EmprestimoView.solicitar_emprestimo(id_exemplar, id_user, data)
                print("✅ Empréstimo registrado com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        elif opcao == "2":
            print("\n-- Registrar Devolução --")
            try:
                print("\nListando transações registradas para consulta de IDs:")
                emprestimos = EmprestimoView.listar_emprestimos()
                if not emprestimos:
                    print("⚠️ Atenção: Não existem transações de empréstimo registradas no sistema.")
                else:
                    for emp in emprestimos:
                        status = "🟡 ATIVO (Emprestado)" if getattr(emp, 'ativo', True) else "🟢 DEVOLVIDO"
                        if getattr(emp, 'ativo', True):
                            print(f"   👉 [ID: {emp.id}] | Exemplar ID: {emp.id_exemplar} | Leitor ID: {emp.id_usuario} | Status: {status}")
                        else:
                            print(f"      [ID: {emp.id}] | Exemplar ID: {emp.id_exemplar} | Leitor ID: {emp.id_usuario} | Status: {status}")
                
                print("-" * 50)
                id_emp = int(input("Digite o ID do Empréstimo a ser devolvido (número): "))
                EmprestimoView.registrar_devolucao(id_emp)
                print("✅ Devolução registrada com sucesso!")
            except ValueError as e:
                print(f"⚠️ Erro: {e}")
            except Exception as e:
                print(f"❌ Erro Crítico: {e}")
        else:
            print("⚠️ Opção inválida!")


def menu_operacoes():
    while True:
        print("\n=== OPERAÇÕES DE BIBLIOTECA E CONSULTAS ===")
        print("1. Gestão de Usuários")
        print("2. Consultas Gerais")
        print("3. Transações")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
        elif opcao == "1":
            submenu_gestao_usuarios()
        elif opcao == "2":
            submenu_consultas_gerais()
        elif opcao == "3":
            submenu_transacoes()
        else:
            print("⚠️ Opção inválida!")


# ==========================================
# MENUS EXCLUSIVOS DO PERFIL: LEITOR
# ==========================================
def menu_leitor(usuario_logado):
    while True:
        print(f"\n=================================")
        print(f"    BIBLIOTECH - ESPAÇO LEITOR   ")
        print(f"    Bem-vindo(a), {usuario_logado.nome}! ")
        print(f"=================================")
        print("1. Consultar Livros no Acervo")
        print("2. Consultar Meu Histórico de Empréstimos")
        print("0. Logout / Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            print("\nEfetuando logout...")
            break
        elif opcao == "1":
            print("\n-- Livros Disponíveis no Acervo --")
            try:
                livros = LivroView.listar()
                if not livros:
                    print("Nenhum livro no acervo no momento.")
                else:
                    for livro in livros:
                        print(f"📖 Título: {livro.titulo} (ID: {livro.id})")
            except Exception as e:
                print(f"❌ Erro ao consultar acervo: {e}")
        elif opcao == "2":
            print("\n-- Meu Histórico de Empréstimos --")
            try:
                emprestimos = EmprestimoView.listar_emprestimos()
                if not emprestimos:
                    print("Nenhum empréstimo registrado no sistema.")
                else:
                    encontrou = False
                    for emp in emprestimos:
                        # ALTERAÇÃO: Filtra apenas as transações do ID do usuário que está logado
                        if int(emp.id_usuario) == int(usuario_logado.id):
                            status = "🟡 ATIVO (Emprestado)" if getattr(emp, 'ativo', True) else "🟢 DEVOLVIDO"
                            print(f"ID Empréstimo: {emp.id} | Código Exemplar: {emp.id_exemplar} | Status: {status}")
                            encontrou = True
                    
                    if not encontrou:
                        print("Você não possui nenhum empréstimo registrado no seu nome.")
            except Exception as e:
                print(f"❌ Erro ao buscar histórico: {e}")
        else:
            print("⚠️ Opção inválida!")


# ==========================================
# MENU DO PERFIL: ADMINISTRADOR
# ==========================================
def menu_administrador():
    while True:
        print("\n=================================")
        print("      SISTEMA BIBLIOTECH (ADMIN) ")
        print("=================================")
        print("1. Cadastros Básicos (Categoria, Autor, Editora)")
        print("2. Gerenciar Acervo (Livros e Exemplares)")
        print("3. Operações (Usuários, Empréstimos e Devoluções)")
        print("0. Logout / Sair")
        
        opcao = input("\nEscolha o módulo desejado: ")
        
        if opcao == "1":
            menu_cadastros_basicos()
        elif opcao == "2":
            menu_acervo()
        elif opcao == "3":
            menu_operacoes()
        elif opcao == "0":
            print("\nEfetuando logout administrativo...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")


# ==========================================
# TELA DE AUTENTICAÇÃO (SISTEMA DE LOGIN)
# ==========================================
def tela_login():
    while True:
        print("\n=================================")
        print("       BEM-VINDO AO BIBLIOTECH   ")
        print("=================================")
        print(" Por favor, realize o login para continuar.")
        print(" (Digite 'sair' no usuário para fechar o sistema)")
        print("-" * 33)
        
        usuario = input("Usuário: ").strip()
        if usuario.lower() == "sair":
            print("\nEncerrando o BiblioTech. Até mais!")
            sys.exit()
            
        senha = input("Senha: ").strip()
        
        # 1. Validação do Perfil Administrador Hardcoded
        if usuario == "admin" and senha == "admin":
            print("\n🔓 Login realizado com SUCESSO! Perfil: ADMINISTRADOR")
            menu_administrador()
            continue
            
        # 2. Validação dinâmica dos Leitores salvos no JSON
        try:
            lista_usuarios = UsuarioView.listar()
            usuario_autenticado = None
            
            for u in lista_usuarios:
                if u.nome == usuario and u.senha == senha and u.perfil.lower() == "leitor":
                    usuario_autenticado = u
                    break
            
            if usuario_autenticado:
                print(f"\n🔓 Login realizado com SUCESSO! Perfil: LEITOR")
                # Passa o objeto do usuário inteiro para gerenciar a sessão individual
                menu_leitor(usuario_autenticado)
            else:
                print("\n❌ ERRO: Usuário ou senha incorretos (ou perfil inválido).")
                
        except Exception as e:
            print(f"\n❌ Erro ao acessar a base de dados de usuários: {e}")


if __name__ == "__main__":
    tela_login()