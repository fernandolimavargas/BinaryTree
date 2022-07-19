from BinarySearchTree import *
from BinaryTree import *
tree = []

def menu(): 
    bst = BinarySearchTree() 
    while True: 
        print('''
        ===========================
                   MENU
        ===========================
        0 - Parar programa
        1 - Inserção 
        2 - Remoção 
        3 - Mostrar em Ordem
        4 - Mostrar em Pós Ordem
        5 - Buscar1
        ''')
        option = input('Escolha a opção: ') 

        if option == '0': break

        if option == "1":
            value = float(input('Digite o valor que queira inserir: '))
            if value in tree: 
                input('Este valor já foi inserido! [ENTER] Continuar')
            else: 
                bst.insert(value)
                print('Arvore Binária')
                tree.append(value)
                print(tree)
            
        if option == '2': 
            value = float(input("Escolha um elemento para remover: "))
            if value in tree:
                bst.remove(value)
                print(f'Após remover {value}')
                bst.inorder_traversal()
            else: 
                input('Valor não encontrado! [ENTER] Continuar.')

        if option == '3': 
            bst.inorder_traversal()

        if option == '4': 
            bst.postorder_traversal()

        if option == '5': 
            item = input('Digite o valor que queira buscar: ')
            if item in tree:
                r = bst.search(item)
                if r is None:
                    print(item, "não encontrado")
                else:
                    print(r.root.data, 'encontrado')

menu()  
