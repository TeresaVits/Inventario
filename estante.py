import csv

livros = []  # Lista para armazenar os livros

# Peguei o salvar e carregar da internt, o resto fiz tah.

#Um arquivo CSV é um formato de arquivo que armazena dados tabulares (como uma planilha) 
# em formato de texto simples. Os dados em um arquivo CSV são organizados em linhas, em que cada linha representa 
# um registro e os campos são separados por um caractere delimitador, geralmente uma vírgula 
def salvar_dados():
    with open("livros.csv", "w", newline="") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["livro", "local"])  # Escreve o cabeçalho no arquivo
        for livro in livros:
            writer.writerow([livro["livro"], livro["local"]])  # Escreve os dados de cada livro

# Função para carregar os dados dos livros a partir do arquivo CSV
def carregar_dados():
    try:
        with open("livros.csv", "r", newline="") as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            next(reader)  # Ignora a primeira linha (cabeçalho)
            for linha in reader:
                livro = {
                    "livro": linha[0],
                    "local": int(linha[1])
                }
                livros.append(livro)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Iniciando com estante vazia.")

#um menu básico com as opcoes
def menu():
    print("================")
    print("Estante")
    print("================")
    print("(1) Adicionar livro")
    print("(2) Remover livro")
    print("(3) Atualizar estante")
    print("(4) Buscar livro")
    print("(5) Mostrar informações")
    print("(0) Sair")
    opcao = int(input("Digite a opção: "))
    selecionar(opcao)

def selecionar(opcao):
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        remover()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        buscar()
    elif opcao == 5:
        mostrar()
    elif opcao == 0:
        salvar_dados()  # Salva os dados antes de sair do programa
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu()


#na variavel local abaixo, eu resolvi dividir a estante em secoes. a minha estante tem 5 linhas e 2 colunas
# entao se o local for 1, vai ser a primeira secao, de cima, esquerda para direita.

def adicionar():
    print("Adicionando livro")
    print("================")
    livro = input("Nome do livro: ")
    local = int(input("Número da seção estante: "))
    novo_livro = {
        "livro": livro,
        "local": local
    }
    livros.append(novo_livro)
    # a funcao append adiciona um novo livro a lista de livros, lá em cima. sem ela, não conseguiria fazer as outras operacoes.
    salvar_dados()  # Salva os dados após adicionar o livro
    print("Livro adicionado com sucesso!")
    opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    if opcao == 1:
        menu()
    else:
        salvar_dados()  # Salva os dados antes de sair do programa
        exit()

def remover():
    print("Removendo livro")
    print("================")
    livro = input("Nome do livro: ")

    livro_removido = None  #é iniciazado como none, indicando que nenhum liv foi encontrado
    for l in livros: #loop para percorrer a lista de livros. 
        if l["livro"] == livro: #se o livro digitado estiver na lista
            livro_removido = l #ele é removido
            break

    if livro_removido: #se for removido
        livros.remove(livro_removido)

        salvar_dados()  # Salva os dados após remover o livro
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado na estante.")

    opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    if opcao == 1:
        menu()
    else:
        salvar_dados()  # Salva os dados antes de sair do programa
        exit()

def atualizar():
    print("Atualizando estante")
    print("================")
    livro = input("Nome do livro: ")
    novo_local = int(input("Novo número da seção estante: "))

    livro_atualizado = None
    for l in livros:
        if l["livro"] == livro:
            livro_atualizado = l
            break

    if livro_atualizado:
        livro_atualizado["local"] = novo_local
        salvar_dados()  # Salva os dados após atualizar a estante
        print("Estante atualizada com sucesso!")
    else:
        print("Livro não encontrado na estante.")

    opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    if opcao == 1:
        menu()
    else:
        salvar_dados()  # Salva os dados antes de sair do programa
        exit()

def buscar():
    print("Buscando livro")
    print("================")
    livro = input("Nome do livro: ")

    livro_encontrado = None
    for l in livros:
        if l["livro"] == livro:
            livro_encontrado = l
            break

    if livro_encontrado:
        print("Livro encontrado na seção:", livro_encontrado["local"])
    else:
        print("Livro não encontrado na estante.")

    opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    if opcao == 1:
        menu()
    else:
        salvar_dados()  # Salva os dados antes de sair do programa
        exit()

def mostrar():
    print("Mostrando informações")
    print("================")

    for livro in livros:
        print("Livro:", livro["livro"])
        print("Seção:", livro["local"])
        print("================")

    opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    if opcao == 1:
        menu()
    else:
        salvar_dados()  # Salva os dados antes de sair do programa
        exit()

carregar_dados()  # Carrega os dados ao iniciar o programa

menu()
