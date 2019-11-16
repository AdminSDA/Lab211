import random
from random import randint
from problem import Problem



class Problem11(Problem):
    def __init__(self):
        pivot=randint(1,99)
        v=[0]
        i=0
        while(i<8):
            j=randint(1,2)
            aux=i
            while(i<=aux+j):
                v.append(randint(pivot+1,100))
                i+=1
            aux=i
            while(i<=aux+j):
                v.append(randint(1,pivot-1))
                i+=1
        i=randint(0,8)
        v[i]=pivot

        statement = 'Partiționați următorul vector folosind pivotul '
        statement += str(pivot)
        statement += ' și partiționarea Lomuto: '
        statement += str(v)


        for i in range(0, 9):
            if v[i] == pivot and i != (len(v) - 1):
                aux = v[i]
                v[i] = v[len(v) - 1]
                v[len(v) - 1] = aux
                i = 10

        data = v
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        n = len(data)
        v = data
        solution='O partitionare a vectorului este:\n'
        solution+='inlocuieste-ma'+'\n'+'\n'+'\n'
        'string-ul de mai sus va fi inlocuit dupa partitionare cu vectorul sortat'
        piv = v[n-1]
        solution += 'Pivotul este : '
        solution += str(piv)
        solution += '\n'
        solution += 'Vrem ca pivotul sa se afle pe ultima pozitie in sir\n'
        solution += 'Daca nu se afla pe ultima pozitie atunci il interschimbam cu elementul aflat pe pozitia respectiva\n'
        solution += 'Dupa interschimbarea pivotului sirul devine : '
        solution += str(v) + '\n' +'\n';
        solution+='Vom calcula pozitia unde trebuie sa stea pivotul,crescand indicele si efectuand interschimbari a.i. elementele mai mici sau egale sa fie in stanga sa.\n'
        solution+='La sfarsit pivotul va fi mutat pe pozitia corespunzatoare.\n'
        solution+='Pozitia pivotului este initial -1 dar va deveni cel putin 0 pe parcursul algoritmului.\n'+'\n'
        pozpiv = -1
        j = 0
        while j < n:
            solution += 'Pasul ' + str(j + 1) + ' : '
            if v[j] <= piv:

                pozpiv = pozpiv + 1
                if(v[j]<piv): solution += 'Elementul ' + str(v[j]) + ' este mai mic decat pivotul'
                else: solution+='Elementul '+str(v[j])+' este egal cu pivotul'
                solution+=' ---> se interschimba ' + str(v[j]) + ' cu ' + str(v[pozpiv]) + ' iar pozitia pivotului devine '+str(pozpiv)+'\n'
                aux = v[pozpiv]
                v[pozpiv] = v[j]
                v[j] = aux
                j =j + 1
            else:
                solution += 'Elementul ' + str(v[j]) + ' este mai mare decat pivotul ---> vectorul si pozitia pivotului raman aceleasi\n'
                j = j + 1
            solution+='Vectorul la aces pas al algoritmului este : '+str(v)+'\n'+'\n'
        if pozpiv >= n:
            pozpiv += -1
        solution += '\n'
        solution=solution.replace('inlocuieste-ma',str(v),1)
        return solution


