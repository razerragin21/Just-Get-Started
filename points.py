def add_points():
    points = 0
    points += 1
    

add_points()

def insert(self, val):
    if not self.val:
        self.val = val
        return

    if self.val == val:
        return

    if val < self.val:
        if self.left:
            self.left.insert(val)
            return
        self.left = BSTNode(val)
        return

    if self.right:
        self.right.insert(val)
        return
    self.right = BSTNode(val)


#feynman 
#1. pick a topic
#2. explain to 12 year old
#3. review, simplify, repeat