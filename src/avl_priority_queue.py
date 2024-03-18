class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


def get_height_for_root(root):
    if not root:
        return 0
    return root.height


def get_balance_for_root(root):
    if not root:
        return 0
    return get_height_for_root(root.left) - get_height_for_root(root.right)


def update_height_and_balance_for_root(root):
    root.height = 1 + max(
        get_height_for_root(root.left), get_height_for_root(root.right)
    )
    balance = get_balance_for_root(root)
    return root, balance

def restore_balance(root, balance):
    if balance > 1:
        if get_balance_for_root(root.left) >= 0:
            return right_rotation(root)
        else:
            root.left = left_rotation(root.left)
            return right_rotation(root)
    if balance < -1:
        if get_balance_for_root(root.right) <= 0:
            return left_rotation(root)
        else:
            root.right = right_rotation(root.right)
            return left_rotation(root)


def find_node_with_the_most_priority(root):
    node_with_the_most_priority = root
    while node_with_the_most_priority.right:
        node_with_the_most_priority = node_with_the_most_priority.right
    return node_with_the_most_priority


def insert_into_queue(root, value, priority):
    if not root:
        return Node(value, priority)
    elif priority <= root.priority:
        root.left = insert_into_queue(root.left, value, priority)
    else:
        root.right = insert_into_queue(root.right, value, priority)

    root, balance = update_height_and_balance_for_root(root)
    if abs(balance) > 1:
        return restore_balance(root, balance)
    return root


def delete_from_queue(root):
    if not root:
        return root
    if not root.right:
        return root.left
    root.right = delete_from_queue(root.right)
    root, balance = update_height_and_balance_for_root(root)
    if abs(balance) > 1:
        return restore_balance(root, balance)
    return find_node_with_the_most_priority(root)


def right_rotation(z):
    y = z.left
    y_right_child = y.right

    y.right = z
    z.left = y_right_child

    z.height = 1 + max(get_height_for_root(z.right), get_height_for_root(z.right))
    y.height = 1 + max(get_height_for_root(y.left), get_height_for_root(y.right))
    return y


def left_rotation(z):
    y = z.right
    y_left_child = y.left

    y.left = z
    z.right = y_left_child
    z.height = 1 + max(get_height_for_root(z.right), get_height_for_root(z.right))
    y.height = 1 + max(get_height_for_root(y.left), get_height_for_root(y.right))
    return y


def left_right_rotation(z):
    z.left = left_rotation(z.left)
    return right_rotation(z)


def right_left_rotation(z):
    z.right = left_rotation(z.right)
    return left_rotation(z)


def print_the_queue(root):
    if not root:
        return

    print_the_queue(root.right)
    print(root.value)
    print_the_queue(root.left)


if __name__ == "__main__":
    root = None
    root = insert_into_queue(root, 'root_node 1', 3)
    root = insert_into_queue(root, 'root_node 2', 1)
    root = insert_into_queue(root, 'root_node 3', 5)
    root = insert_into_queue(root, 'root_node 4', 3)  # Duplicate priority
    root = insert_into_queue(root, 'root_node 5', 3)  # Duplicate priority
    print(root.left.right.value)
    # self.assertEqual(root.value, 'root_node 3')  # Highest priority
    # self.assertEqual(root.left.value, 'root_node 1')
    # self.assertEqual(root.left.left.value, 'root_node 4')  # Among duplicates, inserted in order
    # root = None
    # root = insert_into_queue(root, 10, 6)
    # root = insert_into_queue(root, 20, 5)
    # root = insert_into_queue(root, 30, 3)
    # root = insert_into_queue(root, 40, 2)
    # root = insert_into_queue(root, 50, 1)
    # root = insert_into_queue(root, 25, 4)
    # print(delete_from_queue(root).value)
    # print_the_queue(root)
