def additem(node, v):
    new_node = [v, [], []]
    if node:
        left_chld, right_chld = node[1:]
        if not left_chld:
            left_chld.extend(new_node)
        elif not right_chld:
            right_chld.extend(new_node)
        else:
            additem(left_chld, v)
    else:
        node.extend(new_node)

def binary_tree(new1):
    root = []
    for i in new1:
        additem(root, i)
    return root

def traverse(nod, order):
    if nod:
        v = nod[0]
        if order == 'preorder':
            yield v
        for left_chld in traverse(nod[1], order):
            yield left_chld
        if order == 'inorder':
            yield v
        for right_chld in traverse(nod[2], order):
            yield right_chld
        if order == 'postorder':
            yield v

k=binary_tree('a + b - c'.split())
print k

print "preorder is......",list(traverse(k,'preorder'))
print "inorder is....",list(traverse(k,'inorder'))
print "post order is...." ,list(traverse(k,'postorder'))
