from Node import Node
from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree

'''values = [5, 17, 14, 32, 47, 89, 50, 25]

bst = BinarySearchTree()
for v in values:
    bst.insert(v)

bst.inorder_traversal()

print('\n----------------------------')

# teste de busca
items = [5, 3, 17, 89, 1000]
for item in items: 
    r = bst.search(item)
    if r is None:
        print(item, "não encontrado")
    else:
        print(r.root.data, 'encontrado')
'''
values = [61, 89, 66, 43, 51, 16,11, 55, 79, 77, 82, 32, 100, 90]

bst = BinarySearchTree()

for v in values:
    bst.insert(v)
print('Árvore em Ordem')
bst.inorder_traversal()
print('\nÁrvore em Pós Ordem')
bst.postorder_traversal()
print('\n----------------------------')

# teste de busca
print('Teste de Busca') 
items = [11, 89, 17, 90, 1000]
for item in items: 
    r = bst.search(item)
    if r is None:
        print(item, "não encontrado")
    else:
        print(r.root.data, 'encontrado')

print('\n----------------------------')


#teste de remoção 
v = 11
bst.remove(v)
print(f'Após remover {v}')
bst.inorder_traversal()
print('\n----------------------------')
print('Pós ordem')
bst.postorder_traversal()
print('\n')
print('\n----------------------------')

v2 = 100
bst.remove(v2)
print(f'Após remover {v2}')
print('Ordem simétrica')
bst.inorder_traversal()
print('\n----------------------------')
print('Pós ordem')
bst.postorder_traversal()
print('\n')
print('\n----------------------------')

v3 = 79
bst.remove(v3)
print(f'Após remover {v3}')
bst.inorder_traversal()
print('\n----------------------------')
print('Pós ordem')
bst.postorder_traversal()
print('\n')


