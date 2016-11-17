class Tree:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val


    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is not None:
                    self.left.insert(val)
                else:
                    self.left = Tree(val)
            elif val > self.val:
                if self.right is not None:
                    self.right.insert(val)
                else:
                    self.right = Tree(val)
            else:
                return
        else:
            self.val = val
            print("new node added")

    def showTree(self):
        if self.left is not None:
            self.left.showTree()
        print self.val
        if self.right is not None:
            self.right.showTree()
	    print self.val	