from problem import Problem
import random
from collections import deque

class Problem1(Problem):
    def __init__(self):
        L = range(3)
        amount = 3
        v = [random.choice(L) for _ in range(amount)]
        VectorNume = ["George", "Alina", "Marius"]
        VectorActiune = ["vrea", "doreste" ,"are"]
        VectorObiect = ["masina", "banane", "vacanta"]
        data = [VectorNume[v[0]], VectorActiune[v[1]], VectorObiect[v[2]]]
        statement = 'Aveti la dispozitie 3 structuri de date: \n'
        statement += '  1 -> stiva \n'
        statement += '  2 -> coada \n'
        statement += '  3 -> stiva \n'
        statement += 'Operatii: \n'
        statement += '  caracter -> se introduce caracterul in prima stiva \n'
        statement += '  1 -> se scoate din structura 1 se introduce in structura 2 \n'
        statement += '  2 -> se scoate din structura 2 se introduce in structura 3 \n'
        statement += '  3 -> se scoate din structura 3 se introduce in structura 1 \n'
        statement += 'Scrieti un sir de operatii pentru a avea la sfarsit:\n'
        statement += '  1 -> '  +  VectorNume[v[0]]
        statement += '\n'
        statement += '  2 -> '  +  VectorActiune[v[1]]
        statement += '\n'
        statement += '  3 -> '  +  VectorObiect[v[2]]
        super().__init__(statement, data)

    def solve(self):
        solution = '\n    Creeam cele trei structuri de date in ordine: stiva coada stiva.\n'
        solution += 'Stiva1: |__________|\n'
        solution += 'Coada:  |__________|\n'
        solution += 'Stiva2: |__________|\n\n'

        stiva1 = []
        coada  = deque([])
        stiva2 = []


        for i in range(0, len(self.data[0])):
            stiva1.append(self.data[0][i])

        for i in range(0,len(self.data[2])):
            stiva1.append(self.data[2][i])
            aux = stiva1.pop()
            aux1 = '\u0336'  + aux
            stiva1.append(aux1)
            coada.append(aux)
            coada[i] = '\u0336' + aux
            stiva2.append(aux)


        for i in range (0,len(self.data[1])):
            stiva1.append(self.data[1][i])
            aux = stiva1.pop()
            aux1 = '\u0336'  + aux
            stiva1.append(aux1)
            coada.append(aux)


        solution += '   Efectuam sirul de operatii: \n'
        for i in range(0, len(self.data[0])):
            solution += self.data[0][i] + ' \u0332' + 'c '
        for i in range(0, len(self.data[2])):
            solution +=self.data[2][i]  + ' \u0332' + 'c ' + ' \u0332' + '1 ' + ' \u0332' + '2 '
        for i in range(0, len(self.data[1])):
            solution += self.data[1][i] + ' \u0332' + 'c '  + ' \u0332' + '1 '
        solution += '\n\n'

        solution += '   Obtinem: \n'

        solution += 'Stiva1: ' + " ".join(map(str, stiva1))
        solution +='\n'
        solution += 'Coada:  ' + " ".join(map(str, coada))
        solution +='\n'
        solution += 'Stiva2: ' + " ".join(map(str, stiva2))
        solution +="\n"
        return solution
