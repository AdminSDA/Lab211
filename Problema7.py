import queue
import random
from modules.Node import Nod
from problem import Problem

def sdr(root, v3):
    if root != None :
        sdr(root.left, v3)
        sdr(root.right, v3)
        v3.append(root.val)
    return v3
    # A function to do postorder tree traversal


def srd(root, v1):
    if root != None :
        srd(root.left,v1)
        v1.append(root.val)
        srd(root.right,v1)
    return v1

def rsd(root,v2):
    if root != None:
        v2.append(root.val)
        rsd(root.left,v2)
        rsd(root.right,v2)
    return v2

def afisare(root, nrNivele):
    space = " "
    coadaInitiala = queue.Queue(100)
    coadaFinala = queue.Queue(100)
    coadaInitiala.put(root)
    while not coadaInitiala.empty():
        x = coadaInitiala.get()
        if (x != " "):
            coadaFinala.put(x.val)
            if (x.left == None and x.right == None):
                coadaInitiala.put(" ")
                coadaInitiala.put(" ")
            else:
                if (x.left != None):
                    coadaInitiala.put(x.left)
                else:
                    coadaInitiala.put(" ")
                if (x.right != None):
                    coadaInitiala.put(x.right)
                else:
                    coadaInitiala.put(" ")
        else:
            coadaFinala.put(x)
    x = coadaFinala.get()
    if(x<10):
        print((4*4) * space + " ____ " + str(x) + "____")
    else:
        print((4*4) * space + " ____" + str(x) + "____")
    nivel = 2
    nivelMax = nrNivele
    weNeedSpaces = 0
    print((4*4) * space + "/" + 10 * space + '\\')
    while not coadaFinala.empty():
        v = []
        nrNoduriNivel = 2 ** (nivel - 1)
        x = coadaFinala.get()
        if (weNeedSpaces == 1):
            weNeedSpaces = 2
        if (x == " "):
            weNeedSpaces = 1
        if (weNeedSpaces == 2):
            print(16 * space + str(x), end='')
            weNeedSpaces = 0
        else:
            if(nivel==2):
                print((4*3) * space + "__" + str(x) + "__", end='')
            else:
                print(10 * space + str(x) + 2*space , end='')
        if (x == " "):
            v.append(0)
        else:
            v.append(1)
        nrNoduriNivel -= 1
        while (nrNoduriNivel > 0):
            x = coadaFinala.get()
            if (x == " "):
                v.append(0)
            else:
                v.append(1)
            if (nivel == 2):
                print(8 * space + "__" + str(x) + "__", end='')
            else:
                if (nivel == 3):
                    if (x != " "):
                        if (x < 10):
                            print(4*space + str(x), end='')
                        if (x > 10):
                            print(3*space + str(x), end='')
                    else:
                        print(2*space + 4 * space + str(x), end='')
                else:
                    if(x != " "):
                        print(4*space + str(x), end='')
                    else:
                        print(6*space + str(x), end='')
            nrNoduriNivel -= 1
        print()
        print((nrNivele - 1) * space + " ", end='')
        nrNivele -= 1
        if (nivel < nivelMax):
            spaceCount = 7
            spaceCount1 = 6
            spaceCount2 = 6
            for i in range(len(v)):
                if (v[i] == 0):
                    if(nivel == 2):
                        print(spaceCount * space + '/' + 5 * space + '\\  ', end='')
                        spaceCount = 4
                    if(nivel==3):
                        print(spaceCount1 * space + space + space, end='')
                        spaceCount1 = 3
                    else:
                        print( space + space, end='')
                else:
                    if (nivel == 2):
                        print(spaceCount*space + '/' + 5*space + '\\  ', end='')
                        spaceCount = 4;
                    else:
                        if(nivel == 3):
                            print(spaceCount2*space + '/' + '\\  ' , end='')
                            spaceCount2 = 4
                        else:
                            print(4*space + '/' + '\\', end='')
        else:
            if(nivel == nivelMax):
                return
        print()
        nivel += 1
    return

class Problem7 (Problem):
    def __init__(self):
        statement = ""
        num_nod = random.randrange(4,13,1)
        v = random.sample(range(1, 30), num_nod)

        v1 = []
        v2 = []
        root = Nod(v[0])

        for i in range(0, num_nod):
            ok = 1
            if(root.val != v[i]):
                check_node = root
                while ok != 0:
                    if check_node.val > v[i]:
                        if check_node.left == None:
                            check_node.left = Nod(v[i])
                            ok = 0
                        else:
                            check_node = check_node.left
                    else:
                        if check_node.right == None:
                            check_node.right = Nod(v[i])
                            ok = 0
                        else:
                            check_node = check_node.right

        RSD = rsd(root, v2)
        SRD = srd(root, v1)
        index_position = list(zip(RSD, SRD))
        random.shuffle(index_position)
        RSD, SRD = zip(*index_position)
        statement += "Construiti arborele care are parcurgerile SRD:  " + str(SRD) + " si RSD: " + str(RSD) + ".\n"
        statement += "Afisati si parcurgerea SDR"
        print(statement)
        data = RSD + SRD
        super().__init__(statement, data)

    def solve(self):
        solution = "Idee de rezolvare:Ne folosim de parcurgerea RSD (primul element e radacina) si il cautam in SRD, construind arborele. \n "
        solution += "Rezolvare:Luam primul element din RSD si il cautam in SRD.Impartim SRD in doua parti si luam primul nod din RSD(dupa impartire)si il cautam in partea stanga a SRD \n "
        vector = self.data
        v3 = []
        n = len(vector)//2
        RSD = list(vector[0:n])
        SRD = list(vector[n:len(vector)])
        tata = [None] * 100
        nrNiveleStanga = 0
        nrNiveleDreapta = 0
        root = Nod(RSD[0])
        nodArboreStang = root   #copie a radacinii
        nodArboreDrept = root
        radAnte = root.val
        solution += "Prima radacina este: " + str(radAnte) + "\n"
        solution += " Cautam " + str(radAnte) + " in SRD.\n "
        for i in range(n):
            if(SRD[i]==RSD[0]):
                pozRad = i
                pozitie = i
                break
        for i in range(1, n):
            rad = RSD[i]
            solution += "Noua radacina va fi: " + str(RSD[i]) +".\n "
            for j in range(pozitie):
                if(SRD[j] == rad):
                    solution += "Cautam noua radacina in SRD. \n "
                    solution +=  str(rad)+ " se afla pe pozitia " + str(j) + " si verificam daca se afla in stanga sau in dreapta nodului anterior " + str(radAnte) + ".\n "
                    if (j<pozRad):
                        nodArboreStang.left = Nod(SRD[j])
                        SRD[j] = 0;
                        solution +=  str(rad) + " se afla in stanga, deci il adaugam in stanga nodului anterior. \n "
                        tata[nodArboreStang.left.val] = nodArboreStang
                        nodArboreStang = nodArboreStang.left

                        solution += "Verificam daca nodul " + str(rad) + " mai are noduri in stanga sau in dreapta in SRD. \n "
                        if(j != 0):
                            if (SRD[j-1] == 0 and SRD[j + 1] == radAnte):
                                solution += "Nodul " + str(rad) + " nu mai are noduri in stanga sau in dreapta, deci ne intoarcem la nodul " + str(radAnte) + ".\n "
                                nodArboreStang = tata[nodArboreStang.val]
                                nrNiveleStanga -= 1
                            else:
                                solution += "Nodul " + str(rad) + " mai are noduri in  stanga sau in dreapta, deci ramanem la acelasi nod. \n "
                                pass
                        else:
                            if (SRD[j + 1] == 0):
                                solution += "Nodul " + str(rad) + " nu mai are noduri in stanga sau in dreapta, deci ne intoarcem la nodul " + str(radAnte) + ".\n "
                                nodArboreStang = tata[nodArboreStang.val]
                                nrNiveleStanga -= 1
                            else:
                                solution += "Nodul " + str(rad) + " mai are noduri in  stanga sau in dreapta, deci ramanem la acelasi nod. \n "
                                pass
                    else:
                        nodArboreStang.right = Nod(SRD[j])
                        SRD[j] = 0;
                        solution += str(rad) + " se afla in dreapta, deci il adaugam in dreapta nodului anterior. \n "
                        tata[nodArboreStang.right.val] = nodArboreStang
                        nodArboreStang = nodArboreStang.right
                        solution += "Verificam daca nodul " + str(rad) + " mai are noduri in stanga sau in dreapta in SRD. \n "
                        if (SRD[j-1] == 0 and SRD[j + 1] == 0):
                            solution += "Nodul " + str(rad) + " nu mai are noduri in stanga sau in dreapta, deci ne intoarcem la nodul " + str(radAnte) +".\n"
                            nodArboreStang = tata[nodArboreStang.val]
                            nrNiveleStanga -= 1
                        else:
                            solution += "Nodul " + str(rad) + " mai are noduri in  stanga sau in dreapta, deci ramanem la acelasi nod. \n "
                            pass
                    radAnte = rad
                    nrNiveleStanga += 1
                    pozRad = j
                    break
            for j in range(pozitie, n):
                if(SRD[j] == rad):
                    solution += "Cautam noua radacina in SRD.\n "
                    solution +=  str(rad)+ " se afla pe pozitia " + str(j) + " si verificam daca se afla in stanga sau in dreapta nodului anterior " + str(radAnte) +".\n "
                    if (j<pozRad):
                         nodArboreDrept.left = Nod(SRD[j])
                         SRD[j] = 0;
                         solution +=   str(rad) + " se afla in stanga, deci il adaugam in stanga nodului anterior. \n "
                         tata[nodArboreDrept.left.val] = nodArboreDrept
                         nodArboreDrept = nodArboreDrept.left
                         solution += "Verificam daca nodul " + str(rad) + " mai are noduri in stanga sau in dreapta in SRD. \n "
                         if (SRD[j+1] == 0 and SRD[j - 1] == 0):
                            solution += "Nodul " + str(rad) + " nu mai are noduri in stanga sau in dreapta, deci ne intoarcem la nodul " + str(radAnte) + ".\n"
                            nodArboreDrept = tata[nodArboreDrept.val]
                            nrNiveleDreapta -= 1
                         else:
                            solution += "Nodul " + str(rad) + " mai are noduri in  stanga sau in dreapta, deci ramanem la acelasi nod. \n "
                            pass
                    else:
                        nodArboreDrept.right = Nod(SRD[j])
                        SRD[j] = 0
                        solution +=   str(rad) + " se afla in dreapta, deci il adaugam in dreapta nodului anterior. \n "
                        tata[nodArboreDrept.right.val] = nodArboreDrept
                        nodArboreDrept = nodArboreDrept.right
                        solution += "Verificam daca nodul " + str(rad) + " mai are noduri in stanga sau in dreapta in SRD. \n "
                        if (j != n - 1):
                            if(SRD[j+1] == 0 and SRD[j - 1] == 0):
                                solution += "Nodul " + str(rad) + " nu mai are noduri in stanga sau in dreapta, deci ne intoarcem la nodul " + str(radAnte) + ".\n"
                                nodArboreDrept = tata[nodArboreDrept.val]
                                nrNiveleDreapta -= 1
                            else:
                                solution += "Nodul " + str(rad) + " mai are noduri in  stanga sau in dreapta, deci ramanem la acelasi nod. \n "
                                pass
                        else:
                            if (SRD[j - 1] == 0):
                                solution += "Nodul " + str(rad) + " nu mai are noduri in stanga sau in dreapta, deci ne intoarcem la nodul " + str(radAnte) + ".\n"
                                nodArboreDrept = tata[nodArboreDrept.val]
                                nrNiveleDreapta -= 1
                            else:
                                solution += "Nodul " + str(rad) + " mai are noduri in  stanga sau in dreapta, deci ramanem la acelasi nod. \n "
                                pass
                    radAnte = rad
                    pozRad = j
                    nrNiveleDreapta += 1
                    break
        solution+= "Am terminat de parcurs RSD.\n"
        solution+= " Parcurgerea SDR pentru arborele dat este :"
        sd = sdr(root, v3)
        solution+= str(sd)
        if(nrNiveleStanga >= nrNiveleDreapta):
            nrNivele = nrNiveleStanga + 1
        else:
            nrNivele = nrNiveleDreapta + 1
        afisare(root, nrNivele)
        return solution

print(Problem7().solve())




