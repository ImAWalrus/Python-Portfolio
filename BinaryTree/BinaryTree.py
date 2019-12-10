
from collections import deque

class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def __iter__(self):
        for i in self.data:
            yield i

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key),
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key),
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key),

    def bforder(self):
        Q = deque([])
        Q.append(self)
        while Q:
            p = Q.pop()
            yield p.key
            if p.leftChild:
                Q.appendleft(p.leftChild)
            if p.rightChild:
                Q.appendleft(p.rightChild)
      

    def build_tree(self, tree, pos, data):
        if pos*2 >= len(data):
           return ''

        tree.insertLeft(data[pos*2])
        tree.insertRight(data[pos*2+1])
        pos + 1
        tree.build_tree(tree.leftChild,pos*2,data)
        tree.build_tree(tree.rightChild,pos*2+1,data)



if __name__ == '__main__':
    data = [0]
    data.extend('guoidpy')  # --> [0, 'g', 'u', 'o', 'i', 'd', 'p', 'y']
    root = BinaryTree(data[1])
    root.build_tree(root, 1, data)

      #############################
      #            g              #
      #        ____|____          #
      #        u       o          #
      #      __|__   __|__        #
      #      i   d   p   y        #
      #############################

    print '\n Pre Order ==>\t ', # --> g u i d o p y
    root.preorder()
    print '\n  In Order ==>\t ', # --> i u d g p o y
    root.inorder()
    print '\nPost Order ==>\t ', # --> i d u p y o g
    root.postorder()
    print '\nBreadth First Order ==>\t ', # --> g u o i d p y
    root.bforder()
    for i in root.bforder():
        print i,
        
    print root.data
