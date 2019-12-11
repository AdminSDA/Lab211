from problem import Problem
from collections import defaultdict
import random
import string
cnt = 10
v_niv=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # v_niv=vectorul de nivel
tata=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # tata=vectorul de tati
class Nod:
    def __init__(self, val):
        self.fiu_stang = None
        self.fiu_drept = None
        self.val = val
class Problem36(Problem):
    def __init__(self):
        statement = "Primiti urmatorul arbore binar de cautare: "
        boo=random.randint(0,1)
        if boo==1:
                a=[8,4,12,2,6,10,14]
                b=random.sample(range(1,16,2),3)
                a=a+b
                vector=a.copy()
                a.sort()
                for i in range(1,11):
                       for j in range(0,10):
                              if a[i-1]==vector[j]:
                                        vector[j]=i
        else:
                vector = random.sample(range(1,11),10)
        litere = random.sample(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V"],11)
        # cream functia de inserare a fiecarui element din vector:
        def inserare(rad, nod):
            # daca valoarea nodului este mai mica decat valoarea radacinii
            if nod.val < rad.val:
                # verifica daca radacina nu are fiu in stanga
                if rad.fiu_stang is None:
                    rad.fiu_stang = nod  # nodul devine fiul stang al radacinii curente

                # daca are fiu in stanga
                else:
                    inserare(rad.fiu_stang, nod)  # radacina devine radacina fiului stang si intra iar in inserare
            # daca valoarea nodului este mai mare decat valoarea radacinii
            else:
                # verifica daca radacina nu are fiu in dreapta
                if rad.fiu_drept is None:
                    rad.fiu_drept = nod  # nodul devine fiul drept al radacinii curente

                # daca are fiu in dreapta
                else:
                    inserare(rad.fiu_drept, nod)  # radacina devine radacina fiului drept si intra iar in inserare

        A = Nod(vector[0])  # A=primul element din vector=radacina

        # inserarea elementelor din vector:
        for i in range(1, len(vector)):
            inserare(A, Nod(vector[i]))

            # afisare nod:
        def afisare_imbunatatita(rad, space, sol=""):
            # primul caz
            if (rad == None):
                return ''
            space += cnt  # creste distanta dintre nivele
            sol += afisare_imbunatatita(rad.fiu_drept, space)  # parcurge intai fiii din dreapta
            # afisam nodul curent dupa spatiu:
            sol += '\n'  # trecem la linie noua
            sol += ' ' * (space - cnt)  # afisam suficiente spatii
            sol += str(litere[rad.val])  # afisam valoarea nodului curent
            sol += afisare_imbunatatita(rad.fiu_stang, space)  # parcurge fiii din stanga
            return sol

            # functie care returneaza sol-ul creat in functia anterioara
        def print_imbunatatit(rad):
            s = afisare_imbunatatita(rad, 0)  # punem in string ce returneaza
            return s
        statement = statement + str(print_imbunatatit(A))

        statement = statement + "\nRaspundeti la intrebarile de mai jos:\n"
        a = random.choice([1,2,3])
        b = a + random.choice([1,2,3])
        c = b + random.choice([1,2,3])
        A = litere[a]
        B = litere[b]
        C = litere[c]
        h = random.choice([5,6])
        j = h - random.choice([1,2,3,4])
        k = h + random.choice([2,3])
        H = litere[h]
        J = litere[j]
        K = litere[k]
        data = [vector,litere,[a,b,c,h,j,k]]
        statement = statement + "\n" + "1. Care este succesorul nodului "+str(A) +" ?"
        statement = statement + "\n" + "2. Care este succesorul nodului " + str(B) + " ?"
        statement = statement + "\n" + "3. Care este succesorul nodului " + str(C) + " ?"
        statement = statement + "\n" + "4. Care este inaltimea arborelui ?"
        statement = statement + "\n" + "5. Care este numarul maxim de noduri care pot fi adaugate astfel incat inaltimea sa nu se modifice ?"
        statement = statement + "\n" + "6. Este acest arbore AVL ?"
        statement = statement + "\n" + "7. Daca stergem nodul " + str(H) + ", rezultatul este AVL ?"
        statement = statement + "\n" + "8. Daca stergem nodul " + str(J) + ", rezultatul este AVL ?"
        statement = statement + "\n" + "9. Daca stergem nodul " + str(K) + ", rezultatul este AVL ?"
        super().__init__(statement, data)

    def solve(self):

        data = self.data
        solution="  "
        solution=solution+"\n"
        vector = data[0]
        litere = data[1]

        elemente = data[2]
        a = elemente[0]
        b = elemente[1]
        c = elemente[2]
        h = elemente[3]
        j = elemente[4]
        k = elemente[5]

        # cream functia de inserare a fiecarui element din vector:
        def inserare(rad, nod):
            # daca valoarea nodului este mai mica decat valoarea radacinii
            if nod.val < rad.val:
                    # verifica daca radacina nu are fiu in stanga
                    if rad.fiu_stang is None:
                        rad.fiu_stang = nod # nodul devine fiul stang al radacinii curente
                        tata[nod.val] = rad.val
                        v_niv[nod.val]=v_niv[rad.val]+1 # nivelul pe care se afla nodul in arbore este nivelul tatalui sau +1
                    # daca are fiu in stanga
                    else:
                        inserare(rad.fiu_stang, nod) # radacina devine radacina fiului stang si intra iar in inserare
            # daca valoarea nodului este mai mare decat valoarea radacinii
            else:
                # verifica daca radacina nu are fiu in dreapta
                if rad.fiu_drept is None:
                    rad.fiu_drept = nod # nodul devine fiul drept al radacinii curente
                    tata[nod.val]=rad.val
                    v_niv[nod.val] = v_niv[rad.val] + 1 # nivelul pe care se afla nodul in arbore este nivelul tatalui sau +1
                # daca are fiu in dreapta
                else:
                    inserare(rad.fiu_drept, nod) # radacina devine radacina fiului drept si intra iar in inserare

        # parcurgere in inordine (afiseaza de la cel mai mic la cel mai mare):
        def inordine(rad):
            # daca nu mai exista noduri de parcurs iese
            if not rad:
                return
            inordine(rad.fiu_stang) # parcurge fiii din stanga
            print(rad.val) # afiseaza nodurile
            inordine(rad.fiu_drept) # parcurge fiii din dreapta
            return rad

        A = Nod(vector[0]) # A=primul element din vector=radacina
        ind = vector[0]
        ind1 = int(ind)
        v_niv[ind1]=0 # nivelul radacinii este 0

        # inserarea elementelor din vector:
        for i in range(1, len(vector)):
            inserare(A, Nod(vector[i]))


        # afisare nod:
        def afisare_imbunatatita(rad, space, sol=""):
            # primul caz
            if (rad == None):
                return ''
            space += cnt  # creste distanta dintre nivele
            sol += afisare_imbunatatita(rad.fiu_drept, space)  # parcurge intai fiii din dreapta
            # afisam nodul curent dupa spatiu:
            sol += '\n'  # trecem la linie noua
            sol += ' ' * (space - cnt)  # afisam suficiente spatii
            sol += str(litere[rad.val])  # afisam valoarea nodului curent
            sol += afisare_imbunatatita(rad.fiu_stang, space)  # parcurge fiii din stanga
            return sol

        # functie care returneaza sol-ul creat in functia anterioara
        def print_imbunatatit(rad):
            s = afisare_imbunatatita(rad, 0)  # punem in string ce returneaza
            return s

        # stabilim cea mai mica valoare din arbore:
        def val_min(nod):
            crt = nod  # crt=valoarea nodului
            # cautam cel mai din stanga fiu:
            while crt.fiu_stang is not None:
                crt = crt.fiu_stang
            return crt



        solution = solution + "\nArborele este:\n\n"
        solution = solution + str(print_imbunatatit(A))

        solution = solution + "\n1. Succesorul nodului " + str(litere[a]) + " este: "
        if a==10:
            solution=solution + " nu are succesor"
        else:
            solution=solution + str(litere[a+1])



        solution = solution + "\n2. Succesorul nodului " + str(litere[b]) + " este: "
        if b==10:
            solution=solution + " nu are succesor"
        else:
            solution=solution + str(litere[b+1])

        solution = solution + "\n3. Succesorul nodului " + str(litere[c]) + " este: "
        if c==10:
            solution=solution + " nu are succesor"
        else:
            solution=solution + str(litere[c+1])

        solution = solution + "\n4. Inaltimea arborelui este: " + str(max(v_niv))
        solution = solution + ", deoarece vectorul de nivel este: "+str(v_niv[1:])
        solution = solution + "\n5. Numarul de noduri care pot fi adaugate este: "

        nr=max(v_niv)+1
        putere=1
        s=0
        while nr!=0:
            s = s + putere
            putere=putere*2
            nr=nr-1

        nr = s - len(vector)
        solution = solution +str(nr)


        # stergere nod:
        def stergere(rad, sters):
            # primul caz (daca nu exista radacina):
            if rad is None:
                return rad
             # daca nodul sters este mai mic decat radacina (atunci sters va fi in arborele din stanga):
            if sters < rad.val:
                rad.fiu_stang = stergere(rad.fiu_stang, sters) # se repeta algoritmul pentru fiul stang al radacinii curente
                # daca nodul sters este mai mare decat radacina (atunci sters va fi in arborele din dreapta):
            elif (sters > rad.val):
                rad.fiu_drept = stergere(rad.fiu_drept, sters) # se repeta algoritmul pentru fiul drept al radacinii curente
             # altfel, daca radacina este sters:
            else:
                # verificam daca nodul are un fiu sau niciunul:
                # daca nu are fii in stanga:
                if rad.fiu_stang is None:
                    x = rad.fiu_drept # x devine fiul drept al radacinii
                    rad = None # radacina devine 0
                    return x # returneaza x = noua radacina
                # daca nu are fii in dreapta
                elif rad.fiu_drept is None:
                    x = rad.fiu_stang # x devine fiul stang al radacinii
                    rad = None # radacina devine 0
                    return x # returneaza x = noua radacina
                # daca nodul sters are 2 fii (ia succesorul din inordine):
                x = val_min(rad.fiu_drept) # x devine cea mai mica valoare din subarborele din dreapta
                rad.val = x.val # introduce valoarea succesorului in nodul curent
                rad.fiu_drept = stergere(rad.fiu_drept, x.val) # se repeta algoritmul de stergere pentru succesor
            return rad # returneaza noua radacina
        def nivel(nod):
            if nod is None:
                return 0
            return max(nivel(nod.fiu_stang), nivel(nod.fiu_drept)) + 1
        def avl(rad):
            if rad is None:
                return True
            stg = nivel(rad.fiu_stang)
            dr = nivel(rad.fiu_drept)
            s=0
            if (abs(stg - dr) <= 1):
                s=1
                if avl(rad.fiu_stang) is True:
                    s=2
                    if avl(rad.fiu_drept) is True:
                        return True
            if s==0:
                return abs(stg-dr)
            if s==2:
                return -1
            if s==1:
                return 100

        solution = solution + "\n6. Arborele"
        if avl(A) is True:
            solution=solution + " este AVL."
        else:
            solution = solution + " nu este AVL"
            if avl(A)!=-1 and avl(A)!=100:
                    solution = solution + ", deoarece diferenta este de "+str(avl(A))+". (si trebuie sa fie <2)"

        solution = solution + "\n7. Dupa stergerea nodului "+ str(litere[h])+", arborele arata asa:\n"
        stergere(A,h)
        solution = solution + str(print_imbunatatit(A))
        if avl(A) is True:
            solution = solution +"\nsi este AVL."
        else:
            solution = solution + "\nsi nu este AVL."

        A = Nod(vector[0])  # A=primul element din vector=radacina
        ind = vector[0]
        ind1 = int(ind)
        v_niv[ind1] = 0  # nivelul radacinii este 0

        # inserarea elementelor din vector:
        for i in range(1, len(vector)):
            inserare(A, Nod(vector[i]))

        solution = solution + "\n8. Dupa stergerea nodului " + str(litere[j]) + ", arborele arata asa:\n"
        stergere(A, j)
        solution = solution + str(print_imbunatatit(A))
        if avl(A) is True:
            solution = solution + "\nsi este AVL."
        else:
            solution = solution + "\nsi nu este AVL."

        A = Nod(vector[0])  # A=primul element din vector=radacina
        ind = vector[0]
        ind1 = int(ind)
        v_niv[ind1] = 0  # nivelul radacinii este 0

        # inserarea elementelor din vector:
        for i in range(1, len(vector)):
            inserare(A, Nod(vector[i]))

        solution = solution + "\n9. Dupa stergerea nodului " + str(litere[k]) + ", arborele arata asa:\n"
        stergere(A, k)
        solution = solution + str(print_imbunatatit(A))
        if avl(A) is True:
            solution = solution + "\nsi este AVL."
        else:
            solution = solution + "\nsi nu este AVL."
        return solution
