import random
import queue
from problem import Problem


class Node:
    def __init__(self, eticheta1):
        self.left = None
        self.right = None
        self.val = eticheta1
        self.weight = 0


inaltime = 0
root = Node(0)
maxHeight = 4
rand = random.sample(range(20, 100), 79)


def printPreorder(root, v):
    if root:
        v.append(root.val)
        printPreorder(root.left, v)
        printPreorder(root.right, v)
    return v


def printInorder(root, v):
    if root:
        printInorder(root.left, v)
        v.append(root.val),
        printInorder(root.right, v)
    return v

def sdr(root):
    global inaltime
    global maxHeight
    if root != None:
        sdr(root.left)
        sdr(root.right)
        if (root.left != None):
            inaltime = 1
            calculareInaltime(root.left)
            if (inaltime > maxHeight):
                inaltime = maxHeight
            inaltimeStanga = inaltime
        else:
            inaltimeStanga = 0
        if (root.right != None):
            inaltime = 1
            calculareInaltime(root.right)
            if (inaltime > maxHeight):
                inaltime = maxHeight
            inaltimeDreapta = inaltime
        else:
            inaltimeDreapta = 0
        root.weight = inaltimeDreapta - inaltimeStanga


def calculareInaltime(root):
    global inaltime
    if (root != None):
        if (root.left != None or root.right != None):
            inaltime += 1
        calculareInaltime(root.left)
        calculareInaltime(root.right)


def echilibrare(root):
    if root != None:
        echilibrare(root.left)
        # verificarile sunt scris e pe cazuri particulare de abori cu maxim 4 nivele si nu ar functiona pe cazuri mai mari,
        # se poate transforma intr - o solutie generala usor, pentru scopul nostru functioneaza bine si asa
        echilibrare(root.right)
        if (root.weight == - 2):
            insert(root, Node(root.val + 1))
            root.weight += 1
        if (root.weight == - 3):
            insert(root, Node(root.val + 1))
            root.weight += 1
            insert(root, Node(root.val + 2))
            root.weight += 1
        if (root.weight == - 4):
            insert(root, Node(root.val + 1))
            root.weight += 1
            insert(root, Node(root.val + 2))
            root.weight += 1
            insert(root, Node(root.val + 3))
            root.weight += 1
        if (root.weight == 2):
            insert(root, Node(root.val - 1))
            root.weight -= 1
        if (root.weight == 3):
            insert(root, Node(root.val - 1))
            root.weight -= 1
            insert(root, Node(root.val - 2))
            root.weight -= 1
        if (root.weight == 4):
            insert(root, Node(root.val - 1))
            root.weight -= 1
            insert(root, Node(root.val -2))
            root.weight -= 1
            insert(root, Node(root.val - 3))
            root.weight -= 1

def parcurgere(root,v):
    if (root):
        parcurgere(root.left,v)
        v.append(root.weight)
        parcurgere(root.right,v)
    return v


def insert(root, node):
    if root is None:
        root = node
    else:

        if root.val <= node.val:

            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.val >= node.val:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)

def afisareArbore(v):
    global solution
    AB = 100 *[]
    AB.append(v[0])
    for i in range(64):
        AB += [1000]
        "Aborele binar de cautare va fi retinut in felul urmator:"
        "Fiul stang al elementului de indice k e cel de indice  2*k+1 iar cel drept de indice 2*k+2"
        "Daca in loc de o valore in intervalul [1,50] e 1000 ,atunci locul e gol"
    solution += "\n"
    for x in v[1:len(v)]:
        poz = 0
        while (AB[poz] != 1000):
            if (x < AB[poz]):
                poz = 2 * poz + 1
            else:
                poz = 2 * poz + 2
        AB[poz] = x
    i = 1
    while i < 32:
        for k in range(0, int(64 / (2 * i))): solution += " "
        for j in range(i, i * 2):
            if (AB[j - 1] != 1000): solution += str(AB[j - 1])
            for k in range(0, int(64 / i)): solution += " "
        solution += '\n'
        i = i * 2
    solution += "\n"

def generare_inserare(v, waiting_list, ABC):
    global solution
    for i in waiting_list:
        next_v = v.copy()
        next_v.append(i)
        next_waiting_list = waiting_list.copy()
        next_waiting_list.remove(i)
        if ABC[2 * i + 1] != 1000: next_waiting_list.append(2 * i + 1)
        if ABC[2 * i + 2] != 1000: next_waiting_list.append(2 * i + 2)
        if (len(next_waiting_list) > 0):
            generare_inserare(next_v, next_waiting_list, ABC)
        else:
            for i in next_v:
                solution += str(ABC[i]) + ','
            solution += '\n'


class Problem34(Problem):
    def __init__(self):
        v = random.sample(range(1, 20), 6)
        numberNodes = 6
        min1 = min(v)
        min2 = 1000
        for i in range(0, 6):
            if v[i] < min2 and v[i] > min1:
                min2 = v[i]
                j = i
        v[j] = v[0]
        v[0] = min2
        ABC = [v[0]]
        global root
        root = Node(v[0])
        for j in range(1, numberNodes):
            insert(root, Node(v[j]))
        statement = "Considerati urmatorul arbore binar de cautare: \n"
        for i in range(64):
            ABC += [1000]
            "Aborele binar de cautare va fi retinut in felul urmator:"
            "Fiul stang al elementului de indice k e cel de indice  2*k+1 iar cel drept de indice 2*k+2"
            "Daca in loc de o valore in intervalul [1,50] e 1000 ,atunci locul e gol"
        statement += str(v) + '\n'
        for x in v[1:6]:
            poz = 0
            while (ABC[poz] != 1000):
                if (x < ABC[poz]):
                    poz = 2 * poz + 1
                else:
                    poz = 2 * poz + 2
            ABC[poz] = x
        i = 1
        while i < 32:
            for k in range(0, int(64 / (2 * i))): statement += " "
            for j in range(i, i * 2):
                if (ABC[j - 1] != 1000): statement += str(ABC[j - 1])
                for k in range(0, int(64 / i)): statement += " "
            statement += '\n'
            i = i * 2
        statement += "\n"
        statement += "\n  • Scrieti toate modurile posibile de a insera acele elemente intr-un arbore binar de cautare, pentru ca ABC-ul sa aiba exact acea structura."
        statement += "\n  • Inserati un numar minim de noduri, astfel incat acel arbore sa poata fi considerat AVL."
        print(statement)
        data = ABC
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        v = []
        global solution
        solution = 'Putem insera elementele in urmatoarele moduri a.i. sa obtinem ABC-ul de mai sus: \n'
        generare_inserare([], [0], data)
        sdr(root)
        solution += "Pas1: Calculam ponderile pentru fiecare nod dupa formula: pondere = inaltimeArboreDrept - inaltimeArboreStang \n"
        solution += ("Ponderile inainte de echilibrare: ")
        v = parcurgere(root, v)
        solution += str(v)
        solution += ("\n")
        solution += ("Pas2: Pentru a obtine un arbore AVL trebuie sa adaugam noduri pana cand ponderea fiecarui nod este 1, 0 sau -1. \nDaca ponderea gasita este mai mica decat -1, nodurile vor fi adaugate in dreapta, daca este mai mare decat 1, le adaugam in stanga.\n")
        solution += ("Pas3: Repetam pasul 2 pana cand toate ponderile sunt 1,0 sau -1\n")
        solution += ("Observatie: Trebuie sa pastram structura de arbore binar, deci nodurile adaugate trebuie sa fie unice.\n")
        for j in range(5):
            echilibrare(root)
            sdr(root)
        solution += ("\nPonderi dupa echilibrare: \n")
        v = []
        parcurgere(root,v)
        solution += str(v)
        solution += ("\n")
        v = []
        v = printPreorder(root,v)
        solution += ("Parcurgerea RSD dupa echilibrare: ")
        solution += str(v)
        solution += "\n"
        v = []
        v = printInorder(root, v)
        solution += ("Parcurgerea SRD dupa echilibrare: ")
        solution += str(v)
        v = []
        coada = queue.Queue(100)
        coada.put(root)
        while(coada.empty() != 1):
            x = coada.get()
            v.append(x.val)
            if (x.left != None):
                coada.put(x.left)
            if (x.right != None):
                coada.put(x.right)
        afisareArbore(v)
        return solution
print(Problem34().solve())


