from problem import Problem
import random
from random import sample
#from arbore import Node
#from arbore import Tree

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

    def inorder(self):
        if self.root is not None:
            return self.root.inorder(data)
        else:
            return False

class Problema13(Problem):
    def __init__(self):
        statement = ""
        nr_noduri = 7
        v = sample(range(1, 20), nr_noduri)
        i = random.randint(1,7)
        rad=v[i]
        root = Node(rad)
        statement += "Radacina este " + str(rad) + "\n"

        for i in range(len(v)):
            statement += "Inseram in ABC nodul " + str(v[i]) + "\n"
            root.insert(v[i])

        sdr = root.postorder(root)
        srd = root.inorder(root)

        statement += "Se da urmatoarea parcurgere in postordine (SDR) a unui arbore binar de cautare: " + str(sdr)
        statement += "\nReconstruiti arborele."

        statement += "\nParcurgerea in inordine (SRD) a arborelui este: " + str(srd)
        print(statement)
        data = [srd, rad]

        super().__init__(statement, data)

    def solve(self):
        srd = self.data[0]
        rad = self.data[1]
        solution = ""
        
        space = ' '
        v1 = []
        v2 = []
        rad = self.data[1]
        for i in range(7):
            if(srd[i] < rad):
                v1.append(srd[i])
            if(srd[i] > rad):
                v2.append(srd[i])
        
        solution += str(v1) + str(rad) + str(v2) + "\n"
        solution += 10*space + "______" + str(rad) + "______" + "\n"
        solution += 9*space + "/" + 14*space + "\\" + "\n"
        solution += 5*space + "___" + str(v1[1]) + "___" + 10*space + "___" + str(v2[1]) + "___" + "\n"

        i = 0

        while(i != len(v1)-1):
            if(v1[i] < v1[i-1]):
                solution += 4*space + "/" + 7*space + "\\" +"\n"
                solution += 3*space + str(v1[i])
                i = i + 1
                if(v1[i] > v1[i-1]):
                    solution += 8*space + str(v1[i])
                    i = i +1
            else: #(v1[i] > v1[i-1]):
                i = i + 1
        return solution
        

