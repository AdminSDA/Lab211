import random
import math
from problem import Problem

def fmax(v):
    max = 0
    for i in range(0, len(v)):
        if max < v[i]:
            max = v[i]
    return max

def creare(lungime):
    v = [0]
    chck = [0]  #vect frecventa
    for i in range(1, lungime+1):
        v.append(0)
        chck.append(0)

    v[1] = random.randrange(1, 5)

    stk = []
    stk.append(1)
    #max = v[1]
    max = fmax(v)
    while stk:
        if stk[len(stk)-1] * 2 <= lungime and chck[stk[len(stk)-1]*2] < 2:
            chck[stk[len(stk)-1]*2] += 1
            stk.append(stk[len(stk)-1] * 2)
            if v[stk[len(stk)-1]] == 0:
                v[stk[len(stk)-1]] = random.randrange(max+1, max+10)
        elif stk[len(stk)-1] * 2 + 1 <= lungime and chck[stk[len(stk)-1] * 2+1]<2:
            chck[stk[len(stk)-1]*2+1] += 1
            stk.append(stk[len(stk)-1] * 2+1)
            if v[stk[len(stk)-1]] == 0:
                v[stk[len(stk)-1]] = random.randrange(max+1, max+10)
        else:
            stk.pop()
        max = fmax(v)
    return v


class Problem32(Problem):
    def __init__(self):
        self.lungime = random.randrange(3, 10)
        data = creare(self.lungime)
        #self.k = random.randint(1, 10)
        self.k = random.randint(1, fmax(data))
        statement = '32. Un Prim-Min ABC este un arbore cu urmatoarele proprietati:'
        statement += '\n\t• radacina are valoarea minima din arbore;'
        statement += '\n\t• fiecare valoare din sub-arborele st. are o valoare mai mica decat orice valoare din subarborele dr;'
        statement += '\n\t• sub-arborele stang si sub-arborele drept sunt Prim-Min ABC.'
        statement += '\nPrimind un Prim-Min ABC, ' + str(data[1:]) + ' si un numar ' + str(self.k) + ', decideti daca ' + str(self.k) + ' apare in acest arbore.\n'



        super().__init__(statement, data)

    def solve(self):
        solution = ''
        ok = False

        poz = 1
        solution += "Radacina: " + str(self.data[poz]) + "\n" 
        while poz <= len(self.data)-1:
            if self.data[poz] == self.k:
                ok = True
                solution += str(self.data[poz]) + ' = ' + str(self.k) + '\n'
                break
            elif self.data[poz] > self.k or self.data[poz] == 0:
                solution += "Nu are rost sa mai verificam in continuare (numerele sunt din ce in ce mai mari, iar k este mai mic decat ele).\n"
                break
            else:
                if poz*2+1 <= len(self.data)-1:
                    if self.data[poz*2+1] <= self.k:
                        poz = poz*2+1
                        solution += 'Fiul drept este mai mic decat k: ' + str(self.data[poz]) + ' <= ' + str(self.k) + '\n'
                    else:
                        poz = poz*2
                        solution += 'Fiul drept este mai mare decat k, iar cel stang este mai mic: ' + str(self.data[poz]) + ' <= ' + str(self.k) + '\n'
                elif poz*2 <=len(self.data)-1:
                    poz = poz*2
                else:
                    solution += str(self.data[poz]) + " nu mai are fii\n"
                    break

        if ok:
            solution += 'Deci, ' + str(self.k) + ' se afla in ' + str(self.data[1:])
        else:
            solution += 'Deci, ' + str(self.k) + ' NU se afla in ' + str(self.data[1:])
        #solution += str(ok) + '\n'
        #solution += str(self.data[1:])


        return solution