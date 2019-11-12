import random
from random import sample
from problem import Problem



class Problem11(Problem):
    def __init__(self):
        v = sample(range(1, 100), 10)
        statement = 'Partiționați următorul vector folosind pivotul '
        pivot = random.choice(v)
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

            solution+='Vectorul la acest pas al algoritmului este : '+str(v)+'\n'+'\n'

        solution += '\n'
        solution=solution.replace('inlocuieste-ma',str(v),1)
        return solution

