from problem import Problem
import random
from random import sample
solution=''
class Problem10(Problem):
    def __init__(self):
        n=random.randint(6, 10)
        data = sample(range(1, 101), n)
        self.k1=random.randrange(1,4)
        self.k2=random.randrange(1,3)
        self.k3=random.randrange(1,4)
        statement = '10. Se da vectorul: ' + ', '.join(map(str, data)) + '. '
        statement += 'Gasiti numarul minim de elemente care pot fi sterse astfel incat sa se poata considera ca s-au facut \n'
        statement+= ' - ' + (str(self.k1))
        statement+=' pasi din algoritmul de sortare prin selectia maximului\n '
        statement += '- '+(str(self.k2))
        statement += ' pasi din algoritmul de sortare prin insertie directa\n '
        statement += '- '+(str(self.k3))
        statement += ' pasi din algoritmul de sortare prin selectia minimului. '
        super().__init__(statement,data)

    def solve(self):
        k1=self.k1
        k2=self.k2
        k3=self.k3
        vtest=self.data
        solution=''
        def sortMIN(vtest, k1):
            if k1 == 1:
                prim = vtest[0]
                for i in range(len(vtest)):
                    if vtest[i] < prim:
                        return 0
                return 1
            if k1 == len(vtest):
                nou = sorted(vtest)
                if nou == vtest:
                    return 1
                else:
                    return 0
            if k1 > len(vtest) - 1:
                return 0
            for i in range(0, k1 - 1):
                if vtest[i] > vtest[i + 1] or i + 1 > k1:
                    return 0
            c = vtest[k1 - 1]
            poz = k1
            for i in range(poz, len(vtest)):
                if vtest[i] < c:
                    return 0
            return 1
        def INSERTIONsort(vtest, k1):
            if k1 + 1 > len(vtest):
                return 0
            for i in range(0, k1):
                if vtest[i] > vtest[i + 1] and i + 1 <= k1:
                    return 0
            return 1
        def sortMAX(vtest, k1):
            if k1 == len(vtest):
                nou = sorted(vtest)
                if nou == vtest:
                    return 1
                else:
                    return 0
            if k1 == 1:
                ult = vtest[len(vtest) - 1]
                for i in range(len(vtest) - 1):
                    if vtest[i] > ult:
                        return 0
                return 1
            if k1 > len(vtest) - 1:
                return 0
            for i in range(len(vtest) - 1, len(vtest) - k1, -1):
                if vtest[i] < vtest[i - 1] or i - 1 < len(vtest) - k1:
                    return 0
            c = vtest[i - 1]
            poz = i - 2
            for i in range(poz, -1, -1):
                if vtest[i] > c:
                    return 0
            return 1
        def comb(vtest,nou,index,lung):
            for i in range(index,len(vtest)):
                nou.append(vtest[i])
                if len(nou) == lung:
                    yield nou
                for x in comb(vtest,nou,i+1,lung):
                    if len(x)==lung :
                        yield x
                nou.pop(-1)
        #from itertools import combinations
        v = tuple(vtest)
        cop = list(v)
        min1 = min2 = min3 = 0
        gata1 = gata2 = gata3 = 0
        x = sortMAX(vtest, k1)
        ok1 = 0
        solution+='\nGeneram toate combinarile posibile cu elementele vectorului,pana cand am rezolvat toate cerintele. Pentru fiecare combinare generata sterg din vector respectivele elemente si verific daca satisface vreuna din cerinte.\n '
      
        if x == 1:

            solution+='\n---Numarul minim de elemente care trebuiesc sterse pt ca vectorul sa fie rezultatul a '+ str(k1)+' pasi de sortare prin selectia maximului este '+str(min1)
            solution+='\n   Vectorul rezultat dupa stergeri este '+str(vtest)
            solution += '\n   CONDITIA INDEPLINITA: pe ultimele ' + str(k1) + ' pozitii se afla cele mai mari elemente din vector, sortate crescator'
            ok1 = 1
            gata1 = 1

        y = INSERTIONsort(vtest, k2)
        ok2 = 0
        
        if y == 1:
            solution += '\n---Numarul minim de elemente care trebuiesc sterse pt ca vectorul sa fie rezultatul a ' + str(k2) + ' pasi de sortare prin insertie directa este ' + str(min2)
            solution += '\n   Vectorul rezultat dupa stergeri este ' + str(vtest)
            solution += '\n   CONDITIA INDEPLINITA: primele ' + str(k2 + 1) + ' elemente din vector sunt sortate crescator'
            gata2 = 1
            ok2 = 1
        z= sortMIN(vtest, k3)
        ok3 = 0
        
        if z == 1:
            solution += '\n---Numarul minim de elemente care trebuiesc sterse pt ca vectorul sa fie rezultatul a ' + str(k3) + ' pasi de sortare prin selectia minimului este ' + str(min3)
            solution += '\n   Vectorul rezultat dupa stergeri este ' + str(vtest)
            solution += '\n   CONDITIA INDEPLINITA: pe primele ' + str(k3) + ' pozitii se afla cele mai mici elemente din vector, sortate crescator'
            gata3 = 1
            ok3 = 1

        if gata1==1 and gata2==1 and gata3==1:
            return solution
        while gata1==0 or gata2==0 or gata3==0:
           for k in range(1,len(vtest)+1):
                for j in comb(vtest,[],0,k):  # fiecare j reprezinta o comb
                # j este un vector
                    #solution+='\nIncerc sa sterg elementele ' +str(set(j))
                    cop = list(v)
                    q = list(j)
                    for a in range(len(q)):
                        cop.remove(q[a])
                        #copie = cop
                # de acum lucrez cu cop
                    min1 = min2 = min3 = len(q)
                    if gata1 == 0:
                        x = sortMAX(cop, k1)
                    if gata2 == 0:
                        y = INSERTIONsort(cop, k2)
                    if gata3 == 0:
                        z= sortMIN(cop, k3)
                    if x == 1 and gata1 == 0 and ok1 == 0 and len(cop) >= k1:
                        solution+='\n---Pentru a satisface '+str(k1)+' pasi de sortare prin selectia maximului, '
                        solution+="numarul minim de elemente care trebuiesc sterse este "+str(min1)+' ('+str(set(q))+')'
                        solution+='.\n   Vectorul rezultat dupa stergeri este '+str(cop)
                        solution+='\n   CONDITIA INDEPLINITA: pe ultimele '+str(k1)+' pozitii se afla cele mai mari elemente din vector, sortate crescator'
                        gata1 = 1
                        ok1 = 1
                    if len(cop) < k1 and ok1 == 0:
                        solution+="\n---NU SE POT STERGE ELEMENTE ASTFEL INCAT VECTORUL SA FIE REZULTATUL A "+str(k1)+' PASI DE SORTARE PRIN SELECTIA MAXIMULUI DEOARECE NU EXISTA '+str(k1)+" ELEMENTE SORTATE DESCRESCATOR IN VECTORUL INITIAL \n"
                        ok1 = 1
                        gata1=1
                    if y == 1 and gata2 == 0 and ok2 == 0 and len(cop) >= k2 + 1:
                        solution += '\n---Pentru a satisface ' + str(k2) + ' pasi de sortare prin insertie directa, '
                        solution += "numarul minim de elemente care trebuiesc sterse este " + str(min2)+' (' + str(set(q)) + ')'
                        solution += '.\n   Vectorul rezultat dupa stergeri este ' + str(cop)
                        solution+='\n   CONDITIA INDEPLINITA: primele '+str(k2+1)+' elemente din vector sunt sortate crescator'

                        gata2 = 1
                        ok2 = 1
                    if len(cop) < k2 + 1 and ok2 == 0:
                        solution+="\n---NU SE POT STERGE ELEMENTE ASTFEL INCAT VECTORUL SA FIE REZULTATUL A "+str(k2)+' PASI DE SORTARE PRIN INSERTIE DIRECTA DEOARECE NU EXISTA '+str(k2+1)+" ELEMENTE SORTATE CRESCATOR IN VECTORUL INITIAL \n"
                        ok2 = 1
                        gata2=1
                    if z == 1 and gata3 == 0 and ok3 == 0 and len(cop) >= k3:
                        solution += '\n---Pentru a satisface ' + str(k3) + ' pasi de sortare prin selectia minumului, '
                        solution += "numarul minim de elemente care trebuiesc sterse este " + str(min3)+' (' + str(set(q)) + ')'
                        solution += '.\n   Vectorul rezultat dupa stergeri este ' + str(cop)
                        solution+='\n   CONDITIA INDEPLINITA: pe primele '+str(k3)+' pozitii se afla cele mai mici elemente din vector, sortate crescator'

                        gata3 = 1
                        ok3 = 1
                    if len(cop) < k3 and ok3 == 0:
                        solution+="\n---NU SE POT STERGE ELEMENTE ASTFEL INCAT VECTORUL SA FIE REZULTATUL A "+str(k3)+" PASI DE SORTARE PRIN SELECTIA MINIMULUI DEOARECE NU EXISTA "+str(k3)+" ELEMENTE SORTATE CRESCATOR IN VECTORUL INITIAL .\n"
                        ok3 = 1
                        gata3=1
        return solution
