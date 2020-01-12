import random
from random import sample
from problem import Problem

COUNT = [10]
class Fifo():
    def __init__(self, val):
        self.val = val
        self.st = None
        self.dr = None
        self.h = 0


class Problem35(Problem):

    def __init__(self):
        self.statement = 'Inserati pe rand urmatoarele numere in AVL: '
        self.data = []
        n = random.randint(5, 15)
        v = random.sample(range(25), n)

        self.data = [n, v]
        self.statement += str(self.data[1])

        super().__init__(self.statement, self.data)

    def inserare(self, rad, nod):
        if rad.val < nod.val:
            if rad.dr is None:
                rad.dr = nod
            else:
                self.inserare(rad.dr, nod)
        else:
            if rad.st is None:
                rad.st = nod
            else:
                self.inserare(rad.st, nod)

    def preorder(self, rad, w):
        if rad:
            w.append(rad.val)
            self.preorder(rad.st, w)
            self.preorder(rad.dr, w)

    def fct(self, nod):
        if nod is None:
            return -1
        return nod.h


    def functie_h(self, nod):
        return max(self.fct(nod.st), self.fct(nod.dr)) + 1


    def factor_ec(self, nod):
        if nod is None:
            return 0
        return self.fct(nod.st) - self.fct(nod.dr)


    def SRL(self, nod):
        rightNode = nod.dr
        nod.dr = rightNode.st
        rightNode.st = nod

        nod.h = self.functie_h(nod)
        rightNode.h = self.functie_h(rightNode)
        return rightNode

    def SRR(self, nod):
        leftNode = nod.st
        nod.st = leftNode.dr
        leftNode.dr = nod

        nod.h = self.functie_h(nod)
        leftNode.h = self.functie_h(leftNode)
        return leftNode

    def DRL(self, nod):
        nod.dr = self.SRR(nod.dr)
        nod = self.SRL(nod)
        return nod

    def DRR(self, nod):
        nod.st = self.SRL(nod.st)
        nod = self.SRR(nod)
        return nod

    def print2DUtil(self, root, space, w):
        if (root == None):
            return

        space += COUNT[0]

        self.print2DUtil(root.dr, space, w)

        w.append('\n')
        for i in range(COUNT[0], space):
            w.append(' ')
        w.append(root.val)

        self.print2DUtil(root.st, space, w)

    def print2D(self, root, w):
        self.print2DUtil(root, 0, w)


    def inserare_avl(self, act, value):
        if act is None:
            return Fifo(value)
        elif value < act.val:
            act.st = self.inserare_avl(act.st, value)
        else:
            act.dr = self.inserare_avl(act.dr, value)

        act.h = self.functie_h(act)
        fe = self.factor_ec(act)

        if fe == -2:
            if value > act.dr.val:
                act = self.SRL(act)
            else:
                act = self.DRL(act)

        elif fe == 2:
            if value < act.st.val:
                act = self.SRR(act)
            else:
                act = self.DRR(act)

        return act

    def solve(self):
        solution = ''

        n = self.data[0]
        v = self.data[1]

        solution += '(Afisare folosind preordinea) \n'

        rad = None

        for i in range(0, n):
            rad = self.inserare_avl(rad, v[i])
            solution += 'AVL-ul dupa inserarea elementului ' + str(v[i]) + ' este: '
            w = []
            self.preorder(rad, w)
            for i in range(0, len(w)):
                solution += str(w[i])
                solution += ' '
            solution += '\n'

        s = []
        self.print2D(rad, s)
        for i in range(0, len(s)):
            solution += str(s[i])

        return solution

