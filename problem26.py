import random
import math
from problem import Problem

def creare(l):
    data = [0]
    data.append(random.randrange(30, 100))
    for i in range(2,l+1):
        tmp = random.randrange(1, 100)
        while tmp>data[math.trunc(i/2)]:
            tmp = random.randrange(1, 100)
        data.append(tmp)
        import random
import math
import heapq
from problem import Problem

def creare(l):
    data = [0]
    data.append(random.randrange(30, 100))
    for i in range(2,l+1):
        tmp = random.randrange(1, 100)
        while tmp>data[math.trunc(i/2)]:
            tmp = random.randrange(1, 100)
        data.append(tmp)
        
    return data

class Problem26(Problem):
    def __init__(self):
        lungime = random.randrange(5, 10)
        data = creare(lungime)
        #data = [0, 39, 28, 39, 10, 26, 30, 19, 7]
        #', '.join(map(str, data))
        self.k = random.randrange(2,len(data)-2)
        statement = '26. Gasiti un algoritm care va afiseaza cele mai mari '+ str(self.k) + ' elemente dintr-un max-heap cu n elemente. Complexitatea trebuie sa fie mai buna de O(k log n) sau O(n).\n'

        statement += 'Se da max-heapul ' + ' '.join(map(str,data[1:])) + ' si se cer cele mai mari ' + str(self.k) + ' valori din el.\n'
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        k = self.k
        s = []  #vectorul in care se va salva solutia
        q = []
        heapq.heappush(q, [data[1],1])
        #q = [1] #vector in  care se salveaza pozitiile celor mai mari valori
        solution = 'Adaugam in vectorul q valoarea si pozitia primului element (cel mai mare element) din ' + ' '.join(map(str,data[1:])) + ' , adica elementul de pe pozitia 1. Alegem elementul cu valoarea maxima salvat in q, afisam elementul, adaugam in q fii sai si apoi il stergem. Repetam acest pas de ' + str(k) +' ori.\n\n'
        #############################################################
        #       q[valoare, pozitie din data[]]
        for i in range(0, k):
            #gasim elementul maxim din coada
            #adaugam fii sai in coada
            #adaugam elementul in s(solutie)
            #stergem elementul din coada
            #solution += 'q = [ ' + ' '.join(map(str,q[:][:])) + ' ] alegem cel mai mare element din q'
            solution += 'q = [ '
            for i in range(0, len(q)):
                solution += str(q[i][0]) + ' '
            solution += ' ]. Alegem cel mai mare element din q'
            heapq._heapify_max(q)    
            solution += ', adica ' + str(q[0][0])    

            if 2*(q[0][1]) < len(data):    
                if 2*(q[0][1]) < len(data):
                    q.append([data[q[0][1]*2], q[0][1]*2])
                    solution += '\nAdaugam in q fii lui ' + str(q[0][0]) + ': ' + str(data[q[0][1]*2])

                if 2*(q[0][1])+1 < len(data):
                    q.append([data[q[0][1]*2+1],q[0][1]*2+1])
                    solution += ' ' + str(data[q[0][1]*2+1])
                solution+= ' . Afisam si stergem din q elementul ' + str(q[0][0]) + '\n'
            else:
                solution += '\nAfisam ' + str(q[0][0]) + ' si il stergem din q. \n'    

            s.append(data[q[0][1]])
            heapq.heappop(q)

        solution += '\n\tCele mai mari ' + str(k) + ' elemente din max-heapul ' + ' '.join(map(str,data[1:])) + ' sunt: ' + ' '.join(map(str,s)) + '\n'

        return solution
    return data

class Problem26(Problem):
    def __init__(self):
        lungime = random.randrange(5, 10)
        data = creare(lungime)
        #data = [0, 39, 28, 39, 10, 26, 30, 19, 7]
        #', '.join(map(str, data))
        self.k = random.randrange(2,len(data)-2)
        statement = '26. Gasiti un algoritm care va afiseaza cele mai mari '+ str(self.k) + ' elemente dintr-un max-heap cu n elemente. Complexitatea trebuie sa fie mai buna de O(k log n) sau O(n).\n'

        statement += 'Se da max-heapul ' + ' '.join(map(str,data[1:])) + ' si se cer cele mai mari ' + str(self.k) + ' valori din el.\n'
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        k = self.k
        s = []  #vectorul in care se va salva solutia
        q = [1] #vector in  care se salveaza pozitiile celor mai mari valori
        solution = 'Adaugam in vectorul q pozitia primului element (cel mai mare element) din ' + ' '.join(map(str,data[1:])) + ' , adica 1. Alegem elementul cu valoarea maxima de pe pozitiile salvate in q, afisam elementul, adaugam in q fii sai si ii stergem pozitia din q. Repetam acest pas de ' + str(k) +' ori.\n\n'
        #############################################################
        for i in range(0, k):
            max = 0
            #gasim elementul maxim din coada
            #adaugam fii sai in coada
            #adaugam elementul in s(solutie)
            #stergem elementul din coada
            solution += 'q = [ ' + ' '.join(map(str,q)) + ' ] deci alegem cel mai mare element dintre:  '

            for j in range(0, len(q)):
                solution += str(data[q[j]]) + ' '
                if data[q[j]] > data[q[max]]:
                    max = j
            solution += ', adica ' + str(data[q[max]])    

            if 2*(q[max]) < len(data):    
                if 2*(q[max]) < len(data):
                    q.append(q[max]*2)
                    solution += '\nAdaugam in q pozitiile fiilor lui ' + str(data[q[max]]) + ': ' + str(q[max]*2)

                if 2*(q[max])+1 < len(data):
                    q.append(q[max]*2+1)
                    solution += ' ' + str(q[max]*2+1)
                solution+= ' , il afisam si stergem din q pozitia ' + str(q[max]) + '\n'
            else:
                solution += '\nAfisam ' + str(data[q[max]]) + ' si stergem din q pozitia ' + str(q[max]) + '\n'    

            s.append(data[q[max]])
            q.remove(q[max])

        solution += '\n\tCele mai mari ' + str(k) + ' elemente din max-heapul ' + ' '.join(map(str,data[1:])) + ' sunt: ' + ' '.join(map(str,s)) + '\n'

        return solution
