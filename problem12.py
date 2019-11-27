from problem import Problem
import random

class Problem12(Problem):
    def __init__(self):
        statement="Reconstruiti un arbore oarecare, primind o parcurgere continua in adancime a arborelui, pornind din radacina.\nParcurgerea DFS continua:\n"
        n = 10  # nr de noduri

        class date_nod:
            def __init__(self, valoare, children):
                self.valoare = valoare
                self.children = children
        lista1 = list(range(1, n))
        radacina = random.choice(lista1)
        lista = list(range(1, n + 1))
        lista.remove(radacina)
        lista_nrfii = list(range(1, 5))
        v = []
        fii = []
        cnt = 1
        nod = []
        v.append(radacina)
        j = 0
        contor = 0
        while cnt < n:
            nr_fii = random.choice(lista_nrfii)
            while nr_fii > n - cnt:
                nr_fii = random.choice(lista_nrfii)
            for i in range(0, nr_fii):
                fii.append(random.choice(lista))
                cnt += 1
                v.append(fii[i])
                lista.remove(fii[i])
            radacina = v[0]
            copii = []
            i = 0
            while i < len(fii):
                copii.append(fii[i])
                i += 1
            nod.append(date_nod(radacina, copii))
            contor += 1
            v.pop(0)
            fii.clear()
            j += 1
        # Listele de adiacenta
        #for i in range(0, j):
         #   print(nod[i].valoare, ':', nod[i].children)
        # DFS CONTINUA:
        stiva = []
        vizitat = []
        for i in range(0, n):
            vizitat.append(0)
        dfs = []
        dfs.append(nod[0].valoare)  # radacina
        stiva.append(nod[0].valoare)
        nr = 1
        tata = []
        for i in range(0, contor):
            tata.append(nod[i].valoare)

        while nr <= n and len(stiva) > 0:

            gasit_nod_neviz = 0
            ok = 0
            while ok == 0:
                val = stiva[len(stiva) - 1]
                for k in tata:
                    if k == val:
                        i = tata.index(val)
                        ok = 1
                if ok == 0:
                    stiva.pop()
                    dfs.append(stiva[len(stiva) - 1])

            for j in range(0, len(nod[i].children)):
                if vizitat[(nod[i].children)[j] - 1] == 0:
                    gasit_nod_neviz = 1
                    vizitat[(nod[i].children)[j] - 1] = 1
                    stiva.append((nod[i].children)[j])
                    dfs.append((nod[i].children)[j])
                    nr += 1
                    break
            if gasit_nod_neviz == 0:
                stiva.pop()
                if len(stiva) > 0:
                    dfs.append(stiva[len(stiva) - 1])
        data=dfs
        statement+=str(data)
        super().__init__(statement, data)

    def solve(self):
        solution = ""
        vect = self.data
        #solution+='\nparcurgerea este '+str(vect)
        solution+='Reconstruim arborele plecand de la parcurgerea data\n'
        vizitat = [0] * 10
        vizitat[vect[0] - 1] = 1
        tata = sptata = [0] * 10
        for i in range(1, len(vect)):
            if vizitat[vect[i] - 1] == 0:
                tata[vect[i] - 1] = vect[i - 1]
                vizitat[vect[i] - 1] = 1
        n = 0

        '''def funct(nod, tata, vect, n):
            nr = 0
            #vizitat[nod - 1] = 1
            for i in range(0, len(tata)):
                if tata[i] == nod:
                    nr = nr + 1
            if nod == vect[0]:
                print(str(nod))
            if nr == 0:
                return
            if nr != 0:
                for i in range(0, len(tata)):
                    cop = n
                    if tata[i] == nod:
                        print("          " * n + "|---------" + str(i + 1))
                        n = n + 1
                        vizitat[i] = 1
                        funct(i + 1, tata, vect, n)
                    n = cop

        funct(vect[0], tata, vect, n)'''
        solution+='Pentru fiecare nod voi afisa fiii lui,incepand de la radacina'
        vizitat = [0] * 10
        vizitat[vect[0] - 1] = 1
        tata = sptata = [0] * 10
        for i in range(1, len(vect)):
            if vizitat[vect[i] - 1] == 0:
                tata[vect[i] - 1] = vect[i - 1]
                vizitat[vect[i] - 1] = 1
        n = 0
        vizitat = [0] * 10

        def funct(nod, tata, vect, vizitat, n, sol=''):
            nr = 0
            for i in range(0, len(tata)):
                if tata[i] == nod:
                    nr = nr + 1
            if nr != 0:
                sol += '\n'
                sol += str(nod)
                sol += '\n'
                for i in range(0, len(tata)):
                    if tata[i] == nod:
                        sol += "\n          " * n + "|---------" + str(i + 1) + '\n'
                return sol
            else:
                return
        vizi = [0] * 10
        nou = [0] * 10
        k = 0
        for i in range(0, len(vect)):
            if vizi[vect[i] - 1] == 0:
                nou[k] = vect[i]
                k += 1
                vizi[vect[i] - 1] = 1
        sol=''
        for i in range(len(tata)):
            a = funct(nou[i], tata, vect, vizitat, n)
            # print("pentrul nodul "+str(nou[i])+":")
            if a == None:
                continue
            else:
                sol += a
        solution+=sol
        return solution
