import random
from modules.node import Node
from modules.Urcare import urca
from modules.Coborare import coboara
from problem import Problem




class Problem25(Problem):
    def __init__(self):
        statement = ""
        statement += "Introduceti elementele "
        v = random.sample(range(1, 30), 8)
        statement += str(v)
        ordonat = 1
        for i in range(7):
            if(v[i]<v[i+1]):
                ordonat = 0
        if(ordonat == 1):
            random.shuffle(v)
        statement += " intr-un max heap ternal si decapitati heap-ul"
        print(statement)
        data = v
        super().__init__(statement, data)
    def solve(self):
        v = self.data
        Heap=[v[0]]
        solution ='Heap-ul este alcatuit initial doar din '+str(v[0])+'\n'+'\n'
        for i in range(1,8):
            Heap=list(urca(Heap,v[i]))
            solution+='L-am inserat pe '+str(v[i])+' in heap.Heap-ul devine: \n'
            solution+=str(Heap)
            solution+='\n'+'\n'
        Heap[0]=Heap[7]
        del Heap[7]
        solution+='Am inteschimbat elementul aflat in capul heap-ului cu cel aflat pe  ultima frunza si am scos ultima frunza \n'
        solution+='Fostul heap are acuma forma \n'+str(Heap)
        solution+='\n'+'\n'
        solution+='Coboram elementul aflat la radacina in arbore pentru a se reface structura de heap \n'
        solution+="Verificam daca " + str(Heap[0]) + " este mai mic decat maximul dintre " + str(Heap[1]) + " " + \
                  str(Heap[2]) + " " + str(Heap[3]) + ". \n"
        if Heap[0]>max(Heap[1], Heap[2], Heap[3]):
            solution += "Nu este.Deci heap-ul a pastrat structura de max \n"
        else:
            solution += "Este.Trebuie sa interschimbam " + str(Heap[0]) + " cu " + str(max(Heap[1],Heap[2],Heap[3]))+ \
                        " pentru a se pastra structura de max heap \n"
            if max(Heap[1],Heap[2],Heap[3])==Heap[2]:
                solution +="["+str(Heap[2])+ " "+str(Heap[1])+ " "+str(Heap[0])+ " "+str(Heap[3])+ " "+str(Heap[4])+ \
                            " "+str(Heap[5])+ " "+str(Heap[6])+ " ]"
                solution += "\n"
            if max(Heap[1], Heap[2], Heap[3]) == Heap[3]:
                    solution +="["+ str(Heap[3]) + " " + str(Heap[1]) + " " + str(Heap[2]) + " " + str(Heap[0]) + " " + \
                                str(Heap[4]) + " " + str(Heap[5]) + " " + str(Heap[6]) + " ]\n"
            solution += "\n"
            if max(Heap[1],Heap[2],Heap[3]) == Heap[1]:
                solution +="["+str(Heap[1]) + " " + str(Heap[0]) + " " + str(Heap[2]) + " " + str(Heap[3]) + " " + \
                            str(Heap[4]) + " " + str(Heap[5]) + " " + str(Heap[6]) + " ]\n"
                solution += "\nMai trebuie sa verificam daca " + str(Heap[0]) + " este mai mic decat maximul dintre  "+ \
                            str(Heap[4]) + " " + str(Heap[5]) + " " + str(Heap[6]) + ".\n"
                if Heap[0] > max(Heap[4], Heap[5], Heap[6]):
                    solution += "Nu este.Deci heap-ul a pastrat structura de max \n"
                else:
                    solution += "Este.Trebuie sa interschimbam " + str(Heap[0]) + " cu " \
                                + str(max(Heap[4], Heap[5], Heap[6])) + " pentru a se pastra structura de max heap \n"
                    if max(Heap[4], Heap[5], Heap[6]) == Heap[4]:
                        solution +="["+str(Heap[1]) + " " + str(Heap[4]) + " " + str(Heap[2]) + " " + \
                                    str(Heap[3]) + " " + str(Heap[0]) + \
                                    " " + str(Heap[5]) + " " + str(Heap[6]) + " ]"
                        solution += "\n"
                    if max(Heap[4], Heap[5], Heap[6]) == Heap[5]:
                        solution +="["+ str(Heap[1]) + " " + str(Heap[5]) + " " + str(Heap[2]) + " " + str(Heap[3]) + \
                                       " " + str(Heap[4]) + " " + str(Heap[0]) + " " + str(Heap[6]) + " "
                    solution += "\n"
                    if max(Heap[4], Heap[5], Heap[6]) == Heap[6]:
                        solution += "["+str(Heap[1]) + " " + str(Heap[6]) + " " + str(Heap[2]) + " " + str(Heap[3]) + \
                                    " " + str(Heap[4]) + " " + str(Heap[5]) + " " + str(Heap[0]) + " ]"
                        solution += "\n"




        Heap=list(coboara(Heap))
        solution+="Dupa 'decapitare' si operatiile necesare heap-ul devine \n"
        solution += str(Heap) + '\n' + '\n'
        solution+="   --------"
        solution+=str(Heap[0])
        if (Heap[0] < 10):
            solution+='   ----------------\n'
        else:
            solution+="--------\n"

        solution+="   |       |        |\n"
        solution+="---"
        solution += str(Heap[1])
        if (Heap[1] < 10):
            solution+="---   "
        else:
            solution+="---   "
        solution+=str(Heap[2])
        if (Heap[2] < 10):
            solution+="        "
        else:
            solution+="       "
        solution+=str(Heap[3])
        solution+="\n"
        solution+="|  |   |"
        solution +="\n"
        solution+=str(Heap[4])
        if (Heap[4] < 10):
            solution+="  "
        else:
            solution+=" "
        solution+=str(Heap[5])
        if (Heap[5] < 10):
            solution+="   "
        else:
            solution+="  "
        solution +=str(Heap[6])
        if (Heap[6] < 10):
            solution+="   "
        return solution
