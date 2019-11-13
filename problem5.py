from problem import Problem
from collections import defaultdict
import random
import string


class Problem5(Problem):
    def __init__(self):
        statement = "Inserati urmatoarele valori, pe rand, intr-un arbore binar de cautare: "
        data = random.sample(range(1,9),7)
        statement = statement + str(data) + ".\nScrieti nodurile care se pot sterge in doua moduri. Stergeti elementul "
        k = random.choice(data)
        statement = statement + str(k) + "."
        data = [data, k]

        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution="  "
        solution=solution+"\n"
        v=data[0] # in v retinem vectorul generat random
        nr=data[1] # in nr retinem valoarea nodului generata random care trebuie sters
        # cream structura nod: retinem fiul stang, pe cel drept si valoarea sa:
        class Nod:
            def __init__(self, val):
                self.fiu_stang = None
                self.fiu_drept = None
                self.val = val

        t=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # t=vectorul de tati
        v_niv=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # v_niv=vectorul de nivel

        # cream functia de inserare a fiecarui element din vector:
        def inserare(rad, nod):
            # daca valoarea nodului este mai mica decat valoarea radacinii
            if nod.val < rad.val:
                    # verifica daca radacina nu are fiu in stanga
                    if rad.fiu_stang is None:
                        rad.fiu_stang = nod # nodul devine fiul stang al radacinii curente
                        t[nod.val]=rad.val # tatal nodului este radacina curenta
                        v_niv[nod.val]=v_niv[rad.val]+1 # nivelul pe care se afla nodul in arbore este nivelul tatalui sau +1
                    # daca are fiu in stanga
                    else:
                        inserare(rad.fiu_stang, nod) # radacina devine radacina fiului stang si intra iar in inserare
            # daca valoarea nodului este mai mare decat valoarea radacinii
            else:
                # verifica daca radacina nu are fiu in dreapta
                if rad.fiu_drept is None:
                    rad.fiu_drept = nod # nodul devine fiul drept al radacinii curente
                    t[nod.val] = rad.val # tatal nodului este radacina curenta
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

        A = Nod(v[0]) # A=primul element din vector=radacina
        t[v[0]] = 0 # tatal radacinii este 0
        v_niv[v[0]]=0 # nivelul radacinii este 0

        # inserarea elementelor din vector:
        for i in range(1, len(v)):
            inserare(A, Nod(v[i]))

        print("\n")

        solution = solution + "\n"
        solution = solution + "Verificam in vectorul de tati ce noduri pot fi sterse in 2 moduri (cele care au 2 fii).\n"
        solution = solution + "Nodurile care se pot sterge in doua moduri sunt: "
        solution = solution + "\n"
        # verificam in vectorul de tati ce noduri pot fi sterse in 2 moduri (cele care au 2 fii)
        for i in range(1,9):
            k = 0 # in k numaram de cate ori apare nodul i in vectorul de tati
            for j in range(1,9):
                # daca i apare in vectorul de tati, creste k
                if i is t[j]:
                    k = k+1
            if k > 1: # daca k apare de minim 2 ori, retine i in statement pt. a fi afisat
                solution=solution + str(i) + " " + "deoarece are "+str(k) + " fii\n"

        solution = solution + "\n"
        solution=solution+"Vectorul de tati este:"
        solution = solution + str(t) +"\n"
        solution=solution+"Vectorul de nivel este:"
        solution = solution + str(v_niv)

        # stabilim cea mai mica valoare din arbore:
        def val_min(nod):
            crt = nod # crt=valoarea nodului
            # cautam cel mai din stanga fiu:
            while (crt.fiu_stang is not None):
                crt = crt.fiu_stang
            return crt

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

        solution = solution + "\n"

        # functie pentru afisare din consola:
        def afisare_arbore(rad,space):
            if rad is None: # daca am terminat de parcurs arborele, iese
                return
            space += "      " # creste numarul de spatii la fiecare iteratie
            afisare_arbore(rad.fiu_drept, space) # apeleaza functia pentru fiul drept
            print(space+str(rad.val)) # afiseaza in consola
            afisare_arbore(rad.fiu_stang, space) # apeleaza functia pentru fiul stang

        print("Rezolvare in consola:")
        print("Arborele initial este (inordine):")
        inordine(A)
        print()
        print("Arborele initial este:")
        afisare_arbore(A, " ")
        print()
        A=stergere(A,nr) # stergem nodul nr din arborele a carui radacina este A
        print("Arborele final este (inordine):")
        inordine(A)
        print()
        print("Arborele final este:")
        afisare_arbore(A, " ")
        return solution

