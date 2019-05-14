from Agenda import No
from Agenda import Insere
from Agenda import Busca
from Agenda import Sucessor
from Agenda import Predecessor
from Agenda import PreOrder
from Agenda import InOrder
from Agenda import PosOrder
from Agenda import Remove
from Agenda import Profundidade
from Agenda import Calcula_fb
from Agenda import Atribui_fb
from Agenda import BuscaDesbalanceados

arvore = None

# arvore = Insere(arvore, No('Maria', '4343','maria@hotmail'))
# arvore = Insere(arvore, No('Pablo', '32323', 'pablo@hotmail.com'))
# arvore = Insere(arvore, No('Bianca', '3243', 'caramba@hotmail.com'))
# arvore = Insere(arvore, No('Cecilia', '42433', 'cecilia@hotmail.com'))
# arvore = Insere(arvore, No('Amanda', '43355', 'Duda@hotmail.com'))
# arvore = Insere(arvore, No('Pereira', '43355', 'Duda@hotmail.com'))
# arvore = Insere(arvore, No('Duda', '43355', 'Duda@hotmail.com'))
# arvore = Insere(arvore, No('Eduarda', '43355', 'Duda@hotmail.com'))


# arvore = Insere(arvore, No('Maria', 1, 'a'))
# arvore = Insere(arvore, No('Caramba', 1, 'a'))#No desbalanceado
# arvore = Insere(arvore, No('Cecilia', 1, 'a'))
# arvore = Insere(arvore, No('Duda', 1, 'a'))
# arvore = Insere(arvore, No('Pablo', 1, 'a'))
# arvore = Insere(arvore, No('Paolla', 1, 'a'))

# arvore = Insere(arvore, No('Maria', 1, 'a'))#No desbalanceado
# arvore = Insere(arvore, No('Caramba', 1, 'a'))
# arvore = Insere(arvore, No('Bianca', 1, 'a'))
# arvore = Insere(arvore, No('Fernanda', 1, 'a'))
# arvore = Insere(arvore, No('Fernando', 1, 'a'))
# arvore = Insere(arvore, No('Paolla', 1, 'a'))


# arvore = Insere(arvore, No('Maria', 1, 'a'))
# arvore = Insere(arvore, No('Cecilia', 1, 'a'))
# arvore = Insere(arvore, No('Caramba', 1, 'a'))
# arvore = Insere(arvore, No('Paolla', 1, 'a'))#No desbalanceado
# arvore = Insere(arvore, No('Pablo', 1, 'a'))
# arvore = Insere(arvore, No('Olga', 1, 'a'))





# arvore = Insere(arvore, No('Maria', 1, 'a'))
# arvore = Insere(arvore, No('Bianca', 1, 'a'))
# arvore = Insere(arvore, No('Amanda', 1, 'a'))
# arvore = Insere(arvore, No('Caio', 1, 'a'))
# arvore = Insere(arvore, No('Vitoria', 1, 'a'))
# arvore = Insere(arvore, No('Sabrina', 1, 'a'))
# arvore = Insere(arvore, No('Rogerio', 1, 'a'))
# arvore = Insere(arvore, No('Paolla', 1, 'a'))
# arvore = Insere(arvore, No('Pereira', 1, 'a'))



opcao = 0
print("Projeto árvore")
print("Agenda telefônica")
while opcao != 6:
    print("\nDigite 1 para inserir contato.")
    print("Digite 2 para buscar contato.")
    print("Digite 3 para remover contato.")
    print("Digite 4 para listar todos os contatos.")
    print("Digite 5 para altura da arvore.")
    print("Digite 6 para sair do programa")
    opcao = int(input("Digite sua opcao: "))
    if opcao == 6:
        # print("\nPreOrder: ")
        # PreOrder(arvore)
        # print("\nInOrder: ")
        # InOrder(arvore)
        # print("\nPosOrder: ")
        # PosOrder(arvore)
        print("\nObrigado pela preferência.")
    while opcao < 1 and opcao > 6:
        opcao = int(input("Opção inválida! Digite uma opção entre 1 e 6."))

    if opcao == 1:
        print("\nINSERIR")
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        arvore = Insere(arvore, No(nome, telefone, email))

    if opcao == 2: #incrementar buscar pelo email
        print("\nBUSCAR")
        nome = input("Digite o nome: ")
        aux = Busca(arvore, nome)
        if aux != None:
            print('Nome: ',aux.nome,'\nTelefone: ',aux.telefone,'\nEmail: ', aux.email,'\nFB:',aux.fb)
        else:
            print('Contato inexistente!')

    if opcao == 3:
        print("\nREMOVER")
        nome = input("Digite o nome: ")
        arvore = Remove(arvore, nome)

    if opcao == 4:
        if arvore == None:
            print('Árvore vazia')
        else:
            InOrder(arvore)

    if opcao == 5:
        print(Profundidade(arvore)-1)
