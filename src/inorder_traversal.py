#     10
#
#   5    15
#
# 3   7    20
#
#         12

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_next(node: BinaryTree) -> BinaryTree:
    if node.right:
        return most_left_child(node.right)
    else:
        return find_unchecked_parent(node)


def find_bigger_next_value(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    next_node = find_next(node)
    while next_node.value <= node.value:
        next_node = find_next(next_node)
    print(next_node)
    return next_node.value


def most_left_child(node):
    current = node
    while current.left:
        current = current.left
    return current


def find_unchecked_parent(node):
    current_node = node
    while current_node.parent and current_node.parent.right == current_node:
        current_node = current_node.parent
    return current_node.parent


root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.parent = root
root.right.parent = root
root.right.right = BinaryTree(20)
root.right.right.parent = root.right
root.right.right.left = BinaryTree(12)

root.right.right.left.parent = root.right.right
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(7)


root.left.left.parent = root.left
root.left.right.parent = root.left


print(find_bigger_next_value(root, root.left))


# def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
