from Node import Node

class BinaryTree: # vai servir para guardar a raiz e vai ser o ponto de partida para chamarmos os métodos de construção de nós 
    def __init__(self, data=None, node=None) -> None:
        if node:
            self.root = node
        elif data: 
            node = Node(data) #criação de um nó 
            self.root = node # a raiz da árvore é igual ao nó criado acima 
        else:
            self.root = None 


    def inorder_traversal(self, node=None): 
        if node is None: #se o nó for vazio 
            node = self.root  #o nó vai ser atribuido a raiz da árvore
        if node.left: 
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None): # self - própria arvore, node é o nó 
        if node is None:
            node = self.root 
        if node.left: # se existe a esquerda
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=' ')