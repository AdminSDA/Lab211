import binarytree
from binarytree import Node
from binarytree import build
from problem import Problem
import random
from random import sample


def insert(node, value):
    if node.value:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                insert(node.right, value)
    else:
        node.value = value

INT_MIN = -1000
INT_MAX = 1000


def BST_fromSDR_recursiv(sdr, postIndex,
                      key, min, max, size):

    if (postIndex[0] < 0):
        return None

    root = None

    # If current element of post[] is
    # in range, then only it is part
    # of current subtree
    if (key > min and key < max):

        # Allocate memory for root of this
        # subtree and decrement *postIndex
        root = Node(key)
        postIndex[0] = postIndex[0] - 1

        if (postIndex[0] >= 0):
            # All nodes which are in range key..
            # max will go in right subtree, and
            # first such node will be root of
            # right subtree.
            root.right = BST_fromSDR_recursiv(sdr, postIndex,
                                           sdr[postIndex[0]],
                                           key, max, size)

            # Contruct the subtree under root
            # All nodes which are in range min ..
            # key will go in left subtree, and
            # first such node will be root of
            # left subtree.
            root.left = BST_fromSDR_recursiv(sdr, postIndex,
                                          sdr[postIndex[0]],
                                          min, key, size)

    return root


def BST_fromSDR(sdr, nr_noduri):
    postIndex = [nr_noduri - 1]
    return BST_fromSDR_recursiv(sdr, postIndex,
                             sdr[postIndex[0]],
                             INT_MIN, INT_MAX, nr_noduri)


def postorder(node):
    res = []
    if node:
        res = postorder(node.left)
        res = res + postorder(node.right)
        res.append(node.value)
    return res

class Problem13(Problem):
    def __init__(self):
        statement = ""
        nr_noduri = 8
        v = sample(range(1, 20), nr_noduri)
        i = random.randint(0, 7)
        rad = v[i]
        root = Node(rad)

        for i in range(nr_noduri):
            insert(root, v[i])

        sdr = postorder(root)
        statement += "Se da urmatoarea parcurgere in postordine (SDR) a unui arbore binar de cautare: " + str(sdr)
        statement += "\nReconstruiti arborele."
        data = sdr
        super().__init__(statement, data)

    def solve(self):
        solution = ""
        sdr = self.data
        solution += "\n Parcurgerea in post-ordine este:" + str(sdr) + "\n"

        nr_noduri = len(sdr)
        bst_from_sdr = BST_fromSDR(sdr, nr_noduri)
        solution+= "\n - Constructia arborelui binar de cautare pornind de la SDR -"
        solution += "\n => Arborele binar de cautare reconstruit din parcurgerea post-ordine este: " + str(bst_from_sdr)

        return solution

