from problem import Problem
import random
import math
import heapq

class graph:
    def __init__(self, nod1, nod2, cost):
        self.nod1 = nod1
        self.nod2 = nod2
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost   #functie de comparare pt heap

class Problem41(Problem):
    def __init__(self):
        a = random.randint(3, 8) #nr de noduri
        noduri = random.sample(range(1,a+1), a) #vector cu etichetele nodurilor de la 1 la a+1
        data = []
        data.append(graph(noduri[0],noduri[1],random.randint(1,50))) #vector care contine initial prima muchie cu nod1, nod2, cost
        for i in range(2,a):
            data.append(graph(noduri[random.randint(0,i-1)],noduri[i],random.randint(1,50))) #vectorul va contine a-1 muchii, reprezentand un arbore initial
        m = random.randint(0,math.floor(((a-1)*(a-2))/2)) #nr de muchii care mai pot fi adaugate in graf
        for i in range (0,m):
            while True:
                ok = False
                u = random.sample(range(1, a+1), random.randint(2, 2)) # genereaza 2 noduri
                muchie = graph(u[0],u[1], random.randint(1, 50)) # formeaza muchia din nodurile de mai sus
                for j in data:
                    if ((muchie.nod1 == j.nod1) and (muchie.nod2 == j.nod2) or (muchie.nod1 == j.nod2) and (muchie.nod2 == j.nod1)): #verifica daca muchia se afla in lista de muchii deja
                        ok = True
                        break
                if ok == False: #daca muchia nu se afla in lista de muchii deja se adauga
                    break
            data.append(graph(muchie.nod1,muchie.nod2,muchie.cost))

        statement = '   Primiti urmatorul graf ponderat: \n'

        for i in data:
            statement += str(i.nod1) + ' ' + str(i.nod2)  + ' -> ' + str(i.cost) + '\n'
        statement += '  Construiti arborele partial de cost minim (Prim folosind heap-uri).'
        data = [data, a, a-1+m]

        super().__init__(statement, data)

    def solve(self):
        solution = 'Arborele obtinut este: \n'
        v = self.data[0] #lista de muchii
        nr_n = self.data[1] #nr de noduri
        st = v[0].nod1 #nodul de start
        culoare = [] #vector de culoare
        hmin = []

        la = []
        for i in range(0,nr_n):
            w = []
            la.append(w)
            culoare.append(0)

        for i in v:   #lista de adiacenta
            la[i.nod1 - 1].append(i)
            la[i.nod2 - 1].append(i)

        for i in la[st - 1]:
            if i.nod1 != st: #verificare daca nodul de start nu este vecinul sau din lista de adiacenta
                heapq.heappush(hmin,i)
            if i.nod2 != st:
                heapq.heappush(hmin, i)
        for i in range(0,nr_n):
            while True:
                aux = heapq.heappop(hmin)
                if culoare[aux.nod1 - 1] == 0:  #verificare daca nodul este colorat
                    culoare[aux.nod1 - 1] = 1
                    if i != 0:   #afisare muchii din arborele partial de cost minim fara primul pas pt a nu se repeta prima muchie
                        solution += str(aux.nod1) + ' ' + str(aux.nod2) + ' -> ' + str(aux.cost) + '\n'
                    st = aux.nod1
                    break
                elif culoare[aux.nod2 - 1] == 0:
                    culoare[aux.nod2 - 1] = 1
                    if i != 0:
                        solution += str(aux.nod1) + ' ' + str(aux.nod2) + ' -> ' + str(aux.cost) + '\n'
                    st = aux.nod2
                    break
            for j in la[st-1]:
                if j.nod1 != st:
                    if culoare[j.nod1 - 1] ==0:
                        heapq.heappush(hmin, j) # adaugare in heap a vecinilor nodului de start care nu au fost colorati
                if j.nod2 != st:
                    if culoare[j.nod2 - 1] == 0:
                        heapq.heappush(hmin, j)

        return solution
