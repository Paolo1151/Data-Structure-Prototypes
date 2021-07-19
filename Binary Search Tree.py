class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def is_leaf(self):
        return self.left is None and self.right is None

    def get_children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    def is_parent(self, val):
        children = self.get_children()
        for child in children:
            if child.val == val:
                return True
        else:
            return False 

    def get_val(self):
        return self.val

class BST:
    
    def __init__(self):
        self.root = None

    def insert(self, element):
        if self.root is None:
            self.root = Node(element)
        else:
            self.__insert_node(self.root, element)
    
    def __insert_node(self, current_node, element):
        if current_node is None:
            return Node(element)
        else:
            if element <= current_node.val:
                current_node.left = self.__insert_node(current_node.left, element)
            else:
                current_node.right = self.__insert_node(current_node.right, element)
            return current_node

    def search(self, element):
        if self.root is None or self.root is element:
            return self.root
        else:
            return self.__search_node(self.root, element) 

    def __search_node(self, current_node, element):
        if current_node is None:
            return current_node
        else:
            if element == current_node.val:
                return current_node
            if element < current_node.val:
                return self.__search_node(current_node.left, element)
            else:
                return self.__search_node(current_node.right, element)

    def delete(self, element):
        if self.root is element or self.root is None:
            self.root = None
        else:
            self.__delete_node(self.root, element)
    
    def __pop_min(self, subtree, parent=None):
        if subtree.is_leaf():
            parent.right = None
            return subtree
        else:
            prev_node = parent
            current_node = subtree
            while current_node.left is not None:
                prev_node = current_node
                current_node = current_node.left
            if current_node.right is not None:
                prev_node.left = current_node.right
            else:
                prev_node.left = None
            return current_node

    def __delete_node(self, current_node, element):
        if current_node is None:
            return current_node
        elif current_node.is_leaf():
            if current_node.val == element:
                return None
            else:
                return current_node
        else:
            if current_node.is_parent(element):
                if current_node.left is not None:
                    if current_node.left.val == element:
                        left_children = current_node.left.get_children()
                        if len(left_children) == 0:
                            current_node.left = None
                        elif len(left_children) == 1:
                            current_node.left = left_children[0]
                        else:
                            mini = self.__pop_min(current_node.left.right, current_node.left)
                            mini.left = current_node.left.left
                            mini.right = current_node.left.right
                            current_node.left = mini
                if current_node.right is not None:
                    if current_node.right.val == element:
                        right_children = current_node.right.get_children()
                        if len(right_children) == 0:
                            current_node.right = None
                        elif len(right_children) == 1:
                            current_node.right = right_children[0]
                        else:
                            mini = self.__pop_min(current_node.right.right, current_node.right)
                            mini.left = current_node.right.left
                            mini.right = current_node.right.right
                            current_node.right = mini
                return current_node
            else:
                if element <= current_node.val:
                    current_node.left = self.__delete_node(current_node.left, element)
                    
                else:
                    current_node.right = self.__delete_node(current_node.right, element)
                return current_node

    def print_tree(self):
        if self.root is None:
            print('The Tree is Empty')
        else:
            self.__preOT(self.root)

    def __preOT(self, current_node):
        if current_node is not None:
            print(current_node.val)
            self.__preOT(current_node.left)
            self.__preOT(current_node.right)
        else:
            print('NULL')