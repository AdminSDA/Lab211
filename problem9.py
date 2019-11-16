from problem import Problem
import random

class Problem9(Problem):

    lungime_maxima = 10
    valoare_maxima = 100
    lungime = random.randint(5, lungime_maxima)
    v = random.sample(range(valoare_maxima), lungime)
    # variabila banut controleaza probabilitatea ca raspunsul sa fie adevarat sau fals !
    banut = random.randint(0, 9)

    if banut > 1: # Avem 80% sansa sa aplicam 2 pasi din selection sort la vector
        # se aplica 2 pasi din Selection Sort (maxim)
        for i in range(lungime - 1, lungime - 3, -1):
            index = i
            for j in range(0, i):
                if v[j] > v[index]:
                    index = j

            q = v[i]
            v[i] = v[index]
            v[index] = q

    if lungime > 5:
        pasi_ss = random.randint(1, 4)
        pasi_is = random.randint(1, 4)
        pivot1 = random.sample(v[(lungime - 4):(lungime - 1)], 1)
        pivot = pivot1[0]
    else:
        pasi_ss = random.randint(1, lungime - 1)
        pasi_is = random.randint(1, lungime - 1)
        pivot1 = random.sample(v, 1)
        pivot = pivot1[0]

    def __init__(self, problem9_v, problem9_lungime, problem9_pasi_ss, problem9_pasi_is, problem9_pivot):
        self.v = problem9_v
        self.lungime = problem9_lungime
        self.pasi_ss = problem9_pasi_ss
        self.pasi_is = problem9_pasi_is
        self.pivot = problem9_pivot

    def __init__(self):

        statement = 'Se da vectorul ' + ', '.join(map(str, self.v)) + '. Raspundeti cu adevarat sau fals si explicati de ce:\n'
        statement += '- vectorul a rezultat in urma aplicarii a ' + str(self.pasi_ss) + ' pasi din Selection Sort - maxim\n'
        statement += '- vectorul a rezultat in urma aplicarii a ' + str(self.pasi_is) + ' pasi din Insertion Sort\n'
        statement += '- vectorul a rezultat in urma unei partitionari folosind pivotul ' + str(self.pivot) + '\n'
        statement += '- exemplificati sortarea sirului folosind Bubblesort si Selection Sort (Maxim)\n'

        super().__init__(statement, self.v)

    def bubblesort_explained(self, v, n, solution):
        # n = len(arr) se poate folosi in loc sa primeasca lungimea din apelare

        solution += 'Sirul este: ' + ', '.join(map(str, v)) + '\n'

        for i in range(1, n):
            inversari = False  # am folosit bool pentru inversari
            for j in range(0, n - i):
                if v[j] > v[j + 1]:
                    x = v[j]
                    v[j] = v[j + 1]
                    v[j + 1] = x
                    inversari = True

            solution += 'Dupa parcurgere sirul este: ' + ', '.join(map(str, v)) + '\n'

            if inversari == False:
                solution += 'La aceasta parcurgere nu se face nici o inversare !\n'
                break

        solution += 'Sirul este sortat !\n'

        return solution

    def selectionsort_explained(self, v, n, solution):
        for i in range(n - 1, 0, -1):
            index = i

            solution += 'Sirul este: ' + ', '.join(map(str, v)) + '\n'
            solution += 'Parcurgem sirul pana la elementul ' + str(v[index]) + ' '

            for j in range(0, i):

                if v[j] > v[index]:
                    index = j

            if v[i] != v[index]:
                solution += 'si interschimbam ' + str(v[i]) + ' cu ' + str(v[index]) + ' .\n'

                x = v[i]
                v[i] = v[index]
                v[index] = x

            else:
                solution += 'si nu se face nicio interschimbare . \n'

        solution += 'Sirul este sortat !\n'
        return solution

    def partitionare(self, v, n, pivot, solution):
        ok = False
        solution += 'Verificati daca vectorul a rezultat in urma unei partitionari folosind pivotul ' + str(pivot) + ' !\n'
        solution += 'Aflam pozitia pe care se afla pivotul: '

        for i in range(0, n):
            if v[i] == pivot:
                poz = i
                ok = True

        if ok == False:
            solution += '\nElementul ales ca pivot nu se gaseste in vector !\n'
            return solution

        solution += str(poz) + '\n'
        solution += 'Verificam daca elementele din stanga sunt mai mici decat pivotul, iar cele din dreapta, mai mari. \n'

        if poz != 0:
            for i in range(0, poz):
                if v[i] > pivot:
                    solution += 'Vectorul nu a rezultat in urma unei partitionari folosind pivotul ' + str(pivot) + '\n'
                    return solution

        if poz != n - 1:
            for i in range(poz + 1, n):
                if v[i] < pivot:
                    solution += 'Vectorul nu a rezultat in urma unei partitionari folosind pivotul ' + str(pivot) + '\n'
                    return solution

        solution += 'Da, vectorul a rezultat in urma unei partitionari folosind pivotul ' + str(pivot) + '\n'
        return solution

    def solve(self):

        # facem 2 copii ale vectorului v
        x = [None] * self.lungime
        y = [None] * self.lungime
        for i in range(0, self.lungime):
            x[i] = self.v[i]  # pentru a compara vectorul initial cu vectorul sortat
                         # apoi vom sorta x cu Bubblesort
            y[i] = self.v[i]  # pentru a sorta y cu Selection Sort (maxim)

        # sortam vectorul v pentru a-l putea compara cu copia sa x, nesortata
        self.v.sort()
        # afisam vectorul nesortat
        solution = 'nesortat = ' + ', '.join(map(str, x)) + '\n'
        # afisam vectorul sortat
        solution += 'sortat = ' + ', '.join(map(str, self.v)) + '\n'
        solution += '\n' # new line

        # Verificam daca vectorul a rezultat in urma aplicarii a ?? pasi din Selection Sort (maxim)

        solution += 'Vectorul a rezultat in urma aplicarii a ' + str(self.pasi_ss) + ' pasi din Selection Sort (maxim) ?\n'
        check = 0
        for i in range(1, self.pasi_ss + 1):
            if x[self.lungime - i] == self.v[self.lungime - i]:
                check = check + 1

        if (check == self.pasi_ss):

            solution += 'Adevarat, deoarece dupa aplicarea a ' + str(self.pasi_ss) + ' pasi din selection sort (maxim) cele mai mari ' + str(self.pasi_ss) + ' numere se vor afla la finalul vectorului\n'

        else:

            solution += 'Fals, deoarece dupa aplicarea a ' + str(self.pasi_ss) + ' pasi din selection sort (maxim) cele mai mari ' + str(self.pasi_ss) + ' numere s-ar fi aflat la finalul vectorului, insa nu s-a intamplat acest lucru\n'

        solution += '\n' # new line

        # Verifica daca vectorul a rezultat in urma aplicarii a ?? pasi din Insertion Sort

        solution += 'Vectorul a rezultat in urma aplicarii a ' + str(self.pasi_is) + ' pasi din Insertion Sort ?\n'

        t = False # valoare de adevar.
        check = 0

        for i in range(0, self.pasi_is):
            if x[i] < x[i + 1]:
                check = check + 1

        if check == self.pasi_is:
            check = 0
            for i in range(1, self.pasi_is + 1):
                if x[self.lungime - i] > x[self.lungime - i - 1]:
                    check = check + 1

            if (check == self.pasi_is):
                solution += 'Adevarat, indiferent daca partitia cu termeni sortati a fost aleasa la inceput sau la sfarsit\n'
                solution += 'deoarece atat primii cat si ultimii ' + str(self.pasi_is + 1) + ' termeni ai vectorului sunt sortati !\n'
                t = True

            else:
                solution += 'Adevarat, deoarece primii ' + str(self.pasi_is + 1) + ' termeni ai vectorului sunt sortati ! (termenii sortati la inceput)\n'
                t = True

        else:
            check = 0
            for i in range(1, self.pasi_is + 1):
                if x[self.lungime - i] > x[self.lungime - i - 1]:
                    check = check + 1

            if check == self.pasi_is:
                solution += 'Adevarat, deoarece ultimii ' + str(self.pasi_is + 1) + ' termeni ai vectorului sunt sortati ! (termenii sortati la sfarsit)\n'
                t = True

        if t == False:
            solution += 'Fals, deoarece nici primii si nici ultimii ' + str(self.pasi_is + 1) + ' termeni ai vectorului NU sunt sortati !\n'

        solution += '\n' # new line

        # Verificam daca vectorul a rezultat in urma unei partitionari folosind pivotul 19

        solution = self.partitionare(x, self.lungime, self.pivot, solution)
        solution += '\n' # new line

        # Exemplificati sortarea sirului folosind Bubblesort si Selection Sort (Maxim)

        solution += 'Sortare cu Bubble Sort:\n'
        solution = self.bubblesort_explained(x, self.lungime, solution)
        solution += 'v = ' + ', '.join(map(str, x)) + '\n'
        solution += '\n'  # new line

        solution += 'Sortare cu Selection Sort (maxim):\n'
        solution = self.selectionsort_explained(y, self.lungime, solution)
        solution += 'v = ' + ', '.join(map(str, y)) + '\n'
        solution += '\n'  # new line

        # v = self.v

        return solution
