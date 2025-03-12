class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        print("completed left subtree")
        print("elements: ", elements)
        elements.append(self.data)
        print("element itself: ", elements)
        if self.right:
            elements += self.right.in_order_traversal()
        print("elements in the right subtree: ", elements)
        return elements

    def delete(self, val):
        print("calling delete function for self:", self.data, "val: ",val)
        if val < self.data:
            print("inside val < self.data , val: ", val, "self.data: ",self.data)
            if self.left:
                print("self.left: ", self.left.data)
                self.left = self.left.delete(val)
                print("after recursive delete operation, self.left: ", self.left.data)
        elif val > self.data:
            print("inside val > self.data, val: ", val, "self.data: ",self.data)
            if self.right:
                print("self.right: ", self.right.data)
                self.right = self.right.delete(val)
                print("after recurseive delete operation, self.right: ", self.right.data)
        else:
            print("Enter into else part")
            if self.left is None and self.right is None:
                print("if self.left is None and self.right is None")
                return None
            elif self.left is None:
                print("into elif of else: self.left is None, self.left: ", self.left, " self.right: ", self.right)
                return self.right.data
            elif self.right is None:
                print("into elif of else: self.right is NOne, self.right: ", self.right, "self.left: ", self.left)
                return self.left

            min_val = self.right.find_min()
            print("min val: ", min_val)
            self.data = min_val
            print("self.data: ", self.data)
            self.right = self.right.delete(min_val)
            print("self.right: ", self.right)
        print("returning self.data", self.data)
        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("numbers_tree: ", type(numbers_tree))
    #print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    # numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.delete(9)
    # print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    # numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.delete(17)
    # print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]