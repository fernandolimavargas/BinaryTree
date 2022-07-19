from BinaryTree import BinaryTree
from Node import Node

ROOT = 'root'


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root #variavel para raiz
        while(x):
            parent = x
            if value < x.data: #se o valor for menor que o dado guardado na class Node, ele vai descer para esquerda
                x = x.left
            else: # se não, desce para direita 
                x = x.right
        if parent is None: 
            self.root = Node(value) #caso o pai é None, então, vai receber o valor da raiz
        elif value < parent.data: #valor é menor que o valor pai
            parent.left = Node(value) 
        else:
            parent.right = Node(value) #valor é maior que o valor pai

    def search(self, value, node=0):
        if node == 0: 
            node = self.root
        if node is None:
            return node
        elif node.data == value: # se o node for vazio ou o valor que está nele for igual ao valor que estou procurando 
            return BinarySearchTree(node)
        if value < node.data: 
            return self.search(value, node.left)
        return self.search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def remove(self, value, node = ROOT):
        if node == ROOT:
            node = self.root
        if node is None: 
            return node
        if value < node.data: # se o valor for menor que o nó que estou olhando
            node.left = self.remove(value, node.left) #vou descer a esquerda e substituir 
        elif value > node.data: 
            node.right = self.remove(value, node.right) 
        else: # se não possuir filha a esquerda e nem a direita
            if node.left is None: #caso onde não há filho a esquerda
                return node.right #retorna o ramo a direita 
            elif node.right is None: # caso não há filho a direita
                return node.left #retorna o ramo a direita 
            else: #se tiver filho a esquerda e a direita
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)

        return node 


