import random
from random import sample
from problem import Problem
import math


class Pheapho:
    def __init__(self, a, b, c, k):
        self.a = a
        self.b = b
        self.c = a + b * math.sqrt(k)


class Problem24(Problem):
    def __init__(self):
        self.statement = 'Gasiti un algoritm care va indica primele '
        self.data = []
        n = random.randint(5, 15)
        k = random.randint(2, 10)
        self.data = [n, k]
        self.statement += str(self.data[0])
        self.statement += ' numere de forma a + b * sqrt('
        self.statement += str(self.data[1])
        self.statement += '), cu a si b din N si exemplificati algoritmul. Radicalul a fost ales aleator.\n'
        #self.solution = ''
        super().__init__(self.statement, self.data)


        self.dictionar = {
        (0, 0): 1
        }

    def reechilibrare(self, li, index):  # reechilibrare pentru inserare
        if index == 0:
            return
        tata = (int)((index - 1) / 2)

        if (li[tata].c > li[index].c):
            aux = li[tata]
            li[tata] = li[index]
            li[index] = aux

        index = tata
        self.reechilibrare(li, index)

    def reechilibrare2(self, li, index):  # reechilibrare pentru stergere; apelam reechilibrare2(li, 0) mereu
        if (2 * index + 1 > len(li) - 1):
            return

        tata = index

        if (2 * index + 2 > len(li) - 1):
            fiu = 2 * index + 1
        else:
            if (li[2 * index + 1].c < li[2 * index + 2].c):
                fiu = 2 * index + 1
            else:
                fiu = 2 * index + 2

        if li[tata].c > li[fiu].c:
            aux = li[tata]
            li[tata] = li[fiu]
            li[fiu] = aux

        index = fiu
        self.reechilibrare2(li, index)

    def inserare(self, li, elem):
        # elem este de tip obiect
        li.append(elem)
        n = len(li)
        self.reechilibrare(li, n - 1)

    def stergere(self, li):
        length = len(li)
        li[0] = li[length - 1]
        li.pop(length - 1)
        self.reechilibrare2(li, 0)

    def solve(self):
        solution = ''
        li = []
        k = self.data[1]
        n = self.data[0]
        # inserare elem 0 in heap
        p = Pheapho(0, 0, 0, k)
        self.inserare(li, p)
        ok = 1

        solution += 'Idee de rezolvare: Cream un MIN_heap. Avem radacina a + b * sqrt(k) si inseram in heap numerele (a + 1) + b * sqrt(k) si a + (b + 1) * sqrt(k). \n'
        solution += 'Dupa fiecare inserare reechilibram heap-ul. Afisam radacina, decapitam heap-ul si il reechilibram.\n'

        while n >= 1:
            rad = li[0]
            indice1 = rad.a
            indice2 = rad.b

            # vecin jos
            vecin_jos = Pheapho(indice1 + 1, indice2, 0, k)
            pereche1 = (indice1 + 1, indice2)
            vizitat = 0
            if pereche1 in self.dictionar:
                vizitat = 1

            if vizitat == 0:
                self.inserare(li, vecin_jos)
                self.dictionar[pereche1] = 1

            # vecin dreapta
            vecin_dreapta = Pheapho(indice1, indice2 + 1, 0, k)
            pereche2 = (indice1, indice2 + 1)
            vizitat = 0
            if pereche2 in self.dictionar:
                vizitat = 1

            if vizitat == 0:
                self.inserare(li, vecin_dreapta)
                self.dictionar[pereche2] = 1

            # decapitare heap
            solution += '\nHeap: '
            #' ( ' + str(li[0].a) + ' , ' + str(li[0].b) + ' ) ' + ' .\n'
            length = len(li)
            for i in range(0, length - 1):
                solution +=  ' ( ' + str(li[i].a) + ' , ' + str(li[i].b) + ' ) , '
            solution += ' ( ' + str(li[length - 1].a) + ' , ' + str(li[length - 1].b) + ' ) '

            if ok == 1:
                solution += '\nPrimul element este: 0\n'
            else:
                solution += '\nAl ' + str(ok) + '-lea element este: '
                solution += str(li[0].a) + ' + ' + str(li[0].b) + ' * sqrt(' + str(k) + ')\n'

            self.stergere(li)
            ok = ok + 1

            # actualizam numar elemente de afisat
            n = n - 1
        return solution
