from problem import Problem
import sys
import random
import string


class Problem2 (Problem):
    def __init__(self):
        lista_nr = list(range(3,15))

        nr_caractere = random.choice(lista_nr)
        def rand_string(lenght):
            caractere = string.ascii_letters
            data = random.sample(caractere, lenght)
            return data

        data = list(rand_string(nr_caractere))
        statement = "Aveti la dispozitie 2 cozi. Introduceti, in urmatoarea ordine, elementele:\n"
        statement+=str(data)

        statement+="\n obtinanad la final:\n"
        sir=[]
        sir=random.sample(data,len(data))
        statement+=str(sir)
        statement+="\n Spuneti ce operatii au fost folosite (operatiile permise sunt:\n'caracter' -> se introduce caracterul in prima coada\n1 -> se scoate din prima coada se introduce in a doua coada\n2 -> se scoate din a doua coada se introduce in prima coada\nI_1 -> se extrage un element din coada 1 si se afiseaza\nI_2 -> se extrage un element din coada 2 si se afiseaza\n)"
        data=data+sir
        super().__init__(statement, data)

    def solve(self):
        a = []
        b = []
        cod1 = []
        cod2 = []
        s = self.data
        s1=list()
        s2=list()
        n=int(len(s)/2)

        for i in range (0,n):
            s1.append(s[i])

        for i in range (n, len(s)):
            s2.append(s[i])

        for x in range(0, len(s1)):
            y = 0
            while s1[x] != s2[y]:
                y += 1
            a.append(y + 1)

        solution = ""

        q1 =[]
        q2 =[]
        n1 = 0
        n2 = 0
        j = 0

        solution += 'Coada q1 si coada q2 sunt goale.\n'
        for i in range(1, len(a) + 1):
            if n2 > 0:
                if q2[0] == i:
                    aux = q2[0]
                    q2.remove(aux)
                    n2 = n2 - 1
                    solution += 'Eliminam elementul '+ s2[aux - 1] + " "  'din coada q2 prin operatia: l_2\n'
                    aux=cod2[0]
                    cod2.remove(aux)
                    b.append('l_2')
                    solution += 'cod1' + str(cod1)
                    solution += '\n'
                    solution += 'cod2' + str(cod2)
                    solution += '\n'
                    continue
            while a[j] != i:
                if n2 > 0:
                    while q2[0] < a[j]:
                        aux = q2[0]
                        q2.remove(aux)
                        n2 = n2 - 1
                        q1.insert(n1, aux)
                        n1 = n1 + 1
                        solution += 'Eliminam  elementul ' + s2[aux - 1] + " "  ' din coada q2 si il adaugam in coada q1 prin operatia: 2\n'
                        b.append('2')
                        cod1.append(s2[aux - 1])
                        aux = cod2[0]
                        cod2.remove(aux)
                        solution += 'cod1' + str(cod1)
                        solution += '\n'
                        solution+= 'cod2' + str(cod2)
                        solution += '\n'
                        if n2 == 0:
                            break
                q1.insert(n1, a[j])
                n1 = n1 + 1
                j = j + 1
                solution += 'Inseram in coada q1 elementul:' + s1[j - 1] + " "
                solution += '\n'
                b.append(s1[j - 1])
                cod1.append(s1[j - 1])
                solution += 'cod1' + str(cod1)
                solution += '\n'
                solution += 'cod2' + str(cod2)
                solution += '\n'


                while n2 > 0:
                    aux = q2[0]
                    q2.remove(aux)
                    n2 = n2 - 1
                    q1.insert(n1, aux)
                    n1 = n1 + 1
                    solution += 'Eliminam elementul ' + s2[aux - 1] + " " ' din coada q2 si il adaugam in coada q1 prin operatia: 2\n'
                    b.append('2')
                    aux = cod2[0]
                    cod2.remove(aux)
                    cod1.append(s2[aux - 1])
                    

                    solution += 'cod1' + str(cod1)
                    solution += '\n'
                    solution += 'cod2' + str(cod2)
                    solution += '\n'
                while n1 > 0:
                    aux = q1[0]
                    q1.remove(aux)
                    n1 = n1 - 1
                    q2.insert(n2, aux)
                    n2 = n2 + 1
                    solution += 'Eliminam elementul ' + s2[aux - 1] + " "  ' din coada q1 si il adaugam in coada q2 prin operatia: 1\n'
                    b.append('1')

                    cod2.append(s2[aux - 1])
                    aux = cod1[0]
                    cod1.remove(aux)
                    solution += 'cod1' + str(cod1)
                    solution += '\n'
                    solution += 'cod2' + str(cod2)
                    solution += '\n'


            q1.insert(n1, a[j])
            n1 = n1 + 1
            j = j + 1
            solution +='Inseram in coada q1 elementul:' + s1[j - 1] + " "
            solution += '\n'
            b.append(s1[j -1])
            cod1.append(s1[j - 1])
            solution += 'cod1' + str(cod1)
            solution += '\n'
            solution += 'cod2' + str(cod2)
            solution += '\n'

            aux = q1[0]
            q1.remove(aux)
            n1 = n1 - 1
            solution += 'Eliminam elementul '+ s2[aux - 1] + " " ' din coada q1 prin operatia: l_1\n'
            aux = cod1[0]
            cod1.remove(aux)
            b.append('l_1')
            solution += 'cod1' + str(cod1)
            solution += '\n'
            solution += 'cod2' + str(cod2)
            solution += '\n'
        solution +=str(b)
        solution +='\n'

        return solution
