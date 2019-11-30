from problem import Problem
import random
import math

class Problem29(Problem):
    def __init__(self):
        # Lungimea vectorului este intre 6-15 elemente (1-100)
        lungime = random.randint(6, 15)

        sir = random.sample(range(1, 100), lungime)
        # Adaugam 0 la final
        sir[lungime - 1] = 0
        # Alegem un random k (2 - 5)
        k = random.randint(2, 5)
        # Suprascriem 0 peste cateva numere din vector de la sir[k] la sir[ultim]
        zeroes = random.randint(1, math.floor((lungime - k) / 2 + 1))   # cand k = lungime ramane doar zeroul de la final.
                                                            # cand lungimea e mare si k e mic, avem mai multe zerouri,
                                                            # iar cand lungimea e mica si k e mare, avem mai putine.

        for i in range(0, zeroes):
            index = random.randint(k, lungime)
            if index < (lungime - 1):  # sir[lungime - 1] este deja 0 !
                if (sir[index + 1] != 0) and (sir[index - 1] != 0):  # Nu dorim sa avem doua zerouri alaturate
                    sir[index] = 0

        # Generam un vector x de k elemente in care copiem primele k elemente din vector.
        x = sir[0:k]
        # Sortam x
        x.sort()

        n = [lungime, k]

        data = [sir, x, n]
        # data = [v[v[0]], lungime[v[1]], x[v[2]], k[v[3]]]

        statement = 'Primiti numere naturale > 0 si atunci cand primiti 0, trebuie sa afisati cele mai mari k elemente.\n '
        statement += 'Se dau numerele: ' + ', '.join(map(str, sir)) + '.\n k = ' + str(k) + '\n'
        super().__init__(statement, data)


    def solve(self):

        solution = '\n'
        for i in range(self.data[2][1], self.data[2][0]):
            if self.data[0][i] == 0:
                # afisam x
                solution += ', '.join(map(str, self.data[1])) + '\n'
            elif self.data[0][i] < self.data[1][self.data[2][1] - 1]:
                self.data[1][self.data[2][1] - 1] = self.data[0][i]
                # ducem x[k - 1] pe pozitia potrivita si vectorul x va fi din nou sortat !
                for j in range(self.data[2][1] - 1, 0, -1):
                    if self.data[1][j] < self.data[1][j - 1]:
                        aux = self.data[1][j]
                        self.data[1][j] = self.data[1][j - 1]
                        self.data[1][j - 1] = aux
                    else:
                        break # x[j] e pe pozitia care trebuie ! Nu este necesar sa verificam restul elementelor, intrucat acestea au fost sortate anterior !

        return solution
