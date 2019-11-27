from problem import Problem
from collections import defaultdict
import random
import string
pord=[]
radacini=[]
cnt=10
val_min = -2**31
val_max = 2**31
raspuns=[]
class Nod:
    def __init__(self, val):
        self.fiu_stang = None
        self.fiu_drept = None
        self.val = val

class Problem14(Problem):
    def __init__(self):
        statement = "Poate fi urmatorul vector o parcurgere in postordine a unui arbore binar de cautare:\n a="
        vect = random.sample(range(2,20),10)
        A=Nod(vect[0])

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

        def verif(v):
            if len(v) > 0:
                return v[-1]
            return None

        # parcurgere in postordine:
        def postordine(rad):
            # verificam daca exista radacina:
            if rad is None:
                return
            v = []
            while (True):
                while (rad):
                    if rad.fiu_drept is not None:
                        v.append(rad.fiu_drept) # punem fiii din dreapta al radacinii
                    v.append(rad) # punem radacina
                    rad = rad.fiu_stang # radacina devine fiul stang al radacinii
                rad = v.pop() # setam un element din v ca radacina
                # daca are fiu drept si acesta inca nu este pus in v:
                if rad.fiu_drept is not None and verif(v) == rad.fiu_drept:
                    v.pop()  # scoatem din v fiul drept
                    v.append(rad)  # punem radacina
                    rad = rad.fiu_drept  # radacina devine fiul drept ca sa fie procesata
                # altfel, punem radacina in v:
                else:
                    pord.append(rad.val)
                    rad = None # setam radacina ca None
                if len(v) <= 0:
                    break

        for i in range(1, len(vect)):
            inserare(A, Nod(vect[i]))

        postordine(A)
        data=pord+pord
        i = 0
        while pord[i] < pord[len(pord) - 1]:
            i += 1
        i -= 1
        if i > 4:
            j = random.randint(0, i - 1)
            data[10 + j] = max(pord) + 1
        else:
            j = random.randint(i + 2, len(pord) - 2)
            data[10 + j] = min(pord) - 1
        a = data[0:10]
        b = data[10:20]
        statement = statement + str(a) + ",\ndar acesta:\n b=" + str(b)

        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution="\n"
        a = data[0:10]
        b = data[10:20]

        def spl(p, s, d):  # p=vectorul, s=prima pozitie din stanga, d=pozitia radacinii curente
            # cazul pentru "DA": daca s si d au devenit aceeasi pozitie
            if d - s <= 0:
                return 0
            i = s  # i=pozitia primului element din subarborele stang
            # cat timp elementul de pe pozitia din stanga e mai mic decat radacina curenta
            while p[i] < p[d]:
                i += 1  # creste pozitia din stanga
            for j in range(i,d):  # j ia valori intre pozitia primului element din stanga mai mare decat radacina curenta
                if p[j] < p[d]:  # daca exista un element mai mic decat radacina curenta => "NU"
                    raspuns.append(p[j])
                    raspuns.append(p[d])
                    return False
            return spl(p, s, i - 1) & spl(p, i,d - 1)  # repeta algoritmul pentru subarborele stang(rad o sa fie pe poz i-1) si pentru cel drept(rad o sa fie pe pozitia d-1)

        # creare arbore:
        def creare_arbore(vect, ind,elem, min, max, size):
            if (ind[0] < 0):
                return None
            rad = None # initializam radacina
            # daca face parte din [min,max], atunci e parte din subarborele curent
            if (elem > min and elem < max):
                rad = Nod(elem) # declaram radacina de tip nod
                ind[0] = ind[0] - 1 # indexul scade
                if (ind[0] >= 0):
                    rad.fiu_drept = creare_arbore(vect, ind,vect[ind[0]],elem, max, size) # construim subarborele drept
                    rad.fiu_stang = creare_arbore(vect, ind,vect[ind[0]],min, elem, size) # contruim subarborele stang
            return rad

        def constructie_arbore(vect, size):

            ind = [size - 1]
            return creare_arbore(vect, ind,vect[ind[0]],val_min, val_max, size)

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
            sol += str(rad.val)  # afisam valoarea nodului curent
            sol += afisare_imbunatatita(rad.fiu_stang, space)  # parcurge fiii din stanga
            return sol

        # functie care returneaza sol-ul creat in functia anterioara
        def print_imbunatatit(rad):
            s = afisare_imbunatatita(rad, 0)  # punem in string ce returneaza
            return s

        solution=solution+"pentru a:" + str(a) + " afiseaza: "
        if spl(a, 0, len(a) - 1)==0:
            solution=solution+"DA\n"
            sizea=len(a)
            A=constructie_arbore(a,sizea)
            solution = solution + "\n"
            solution = solution + "Arborele este:\n\n"
            solution = solution + str(print_imbunatatit(A)) + "\n\n"
        else:
            solution=solution+"NU\n"

        solution = solution + "pentru b:" + str(b) + " afiseaza: "
        if spl(b, 0, len(b) - 1):
            solution = solution + "DA\n"
            sizeb=len(b)
            B=constructie_arbore(b,sizeb)
            solution = solution + "\n"
            solution = solution + "Arborele este:\n\n"
            solution = solution + str(print_imbunatatit(B)) + "\n\n"
        else:
            solution = solution + "NU, deoarece, "
            x=raspuns[0]
            y=raspuns[1]
            solution=solution + str(x)+" < "+str(y) + "."

        return solution