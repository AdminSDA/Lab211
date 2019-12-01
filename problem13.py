from problem import Problem
import random
from random import sample

COUNT= 10

class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
        return res

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res

class Tree():

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True



class Problema13(Problem):
    def __init__(self):
        statement = ""
        nr_noduri = 7
        v = sample(range(1, 20), nr_noduri)
        rad=v[0]
        root = Node(rad)

        for i in range(len(v)):
            root.insert(v[i])

        sdr = root.postorder(root)
        srd = root.inorder(root)

        statement += "Se da urmatoarea parcurgere in postordine (SDR) a unui arbore binar de cautare: " + str(sdr)
        statement += "\nReconstruiti arborele."

        print(statement)
        data = [srd, rad,root]

        super().__init__(statement, data)

    def solve(self):

        srd = self.data[0]
        rad = self.data[1]
        root= self.data[2]
        solution = ""
        solution= "\nRadacina arborelui este " +str(rad)
        solution+= "\nParcurgerea in inordine (SRD) a arborelui este: " + str(srd) +"\n"

        def print2DUtil(root, space, pretty=""):
            if (root == None):
                return ''

            space += COUNT

            pretty += print2DUtil(root.right, space)

            pretty += '\n'
            pretty += ' ' * (space - COUNT)
            pretty += str(root.data)
            pretty += print2DUtil(root.left, space)
            return pretty

        def print2D(root):
            s = print2DUtil(root, 0)
            return s

        solution += "\nArborele reconstruit din SDR+SRD este: " +"\n"
        solution+= str(print2D(root))


        return solution
        

