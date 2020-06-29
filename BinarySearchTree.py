class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.val)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val=val)
            return
        curr = self.root
        while curr:
            if curr.val > val:
                if not curr.left:
                    curr.left = Node(val=val)
                    return
                else:
                    curr = curr.left
            if curr.val < val:
                if not curr.right:
                    curr.right = Node(val=val)
                    return
                else:
                    curr = curr.right

    def find_successor(self, curr):
        temp = curr
        while temp.left:
            temp = temp.left
        return temp

    def delete(self, key, curr):
        if not self.root:
            return self.root
        if self.root.val == key and not self.root.left and not self.root.right:
            self.root = None
        if key < curr.val and curr.left:
            curr.left = self.delete(key, curr.left)
        elif key > curr.val and curr.right:
            curr.right = self.delete(key, curr.right)
        elif key == curr.val:
            # Deleting node with one or no child
            if not curr.left:
                temp = curr.right
                curr = None
                return temp
            elif not curr.right:
                temp = curr.left
                curr = None
                return temp
            # Deleting node with two child
            temp = self.find_successor(curr.right)
            curr.val = temp.val
            curr.right = self.delete(temp.val, curr.right)
        return curr

    def inorder(self, curr):
        ans = []
        if curr:
            ans = self.inorder(curr.left)
            ans.append(curr.val)
            ans = ans + self.inorder(curr.right)
        return ans

    def postorder(self, curr):
        ans = []
        if curr:
            ans = self.postorder(curr.left)
            ans = ans + self.postorder(curr.right)
            ans.append(curr.val)
        return ans

    def preorder(self, curr):
        ans = []
        if curr:
            ans.append(curr.val)
            ans = ans + self.preorder(curr.left)
            ans = ans + self.preorder(curr.right)
        return ans

    def search(self, key):
        if self.root.val == key:
            print(f'{key} found')
            return
        curr = self.root
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
                if curr:
                    if key == curr.val:
                        print(f'{key} found')
                        return
            if key > curr.val:
                curr = curr.right
                if curr:
                    if key == curr.val:
                        print(f'{key} found')
                        return
        print(f'{key} not in BST')


if __name__ == '__main__':
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(15)
    bst.insert(80)
    bst.insert(75)
    bst.insert(40)
    print(bst.inorder(bst.root))
    # print(bst.postorder(bst.root))
    # print(bst.preorder(bst.root))
    bst.search(75)
    bst.delete(15, bst.root)
    print(bst.inorder(bst.root))
    bst.delete(50, bst.root)
    print(bst.inorder(bst.root))
    bst.delete(45, bst.root)
    print(bst.inorder(bst.root))
