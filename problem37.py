import random
from problem import Problem


class Problem37(Problem):

    def __init__(self):
        self.statement = '\nAlgoritmul Huffman \n********\n '
        self.data = []

        dictionar = {'acs': ['acasa', 'casa', 'sac', 'cas', ], 'adenrt': ['ardenta', 'aderenta', 'datare', 'tandrete'],
                     'aerst': ['terasa', 'serata', 'trasee', 'stare'], 'art': ['rata', 'artar', 'arta', 'tatar']}
        d = random.choice(list(dictionar.keys()))
        v = random.randint(0, 3)
        self.statement += 'a)Construiti arborele avand ponderile date \n b)Codificati cuvantul '+str(dictionar[d][v])
        self.statement += '\n c)Decodificati daca este posibil \n d)Pentru alt exemplu mai rulati o data'

        self.data = [dictionar, d, v]

        super().__init__(self.statement, self.data)


    def combine(self, nodes, huffman_tree):
        pos = 0
        newnode = []
        if len(nodes) > 1:
            nodes.sort()
            nodes[pos].append(0)
            nodes[pos + 1].append(1)
            combined_node1 = (nodes[pos][0] + nodes[pos + 1][0])
            combined_node2 = (nodes[pos][1] + nodes[pos + 1][1])
            newnode.append(combined_node1)
            newnode.append(combined_node2)
            newnodes = []
            newnodes.append(newnode)
            newnodes = newnodes + nodes[2:]
            nodes = newnodes
            huffman_tree.append(nodes)
            self.combine(nodes, huffman_tree)
        return huffman_tree


    def solve(self):
        solution = ''
        dictionar = self.data[0]
        d = self.data[1]
        v = self.data[2]

        # print(d)
        #solution += str(d)
        #solution += '\n'

        # print(v)
        #solution += str(v)
        #solution += '\n'

        mesaj = dictionar[d][v]

        # print(dictionar[d][v])
        #solution += str(dictionar[d][v])
        #solution += '\n'

        litere = []
        doar_litere = []
        for litera in mesaj:
            if litera not in litere:
                frecventa = mesaj.count(litera)
                litere.append(frecventa)
                litere.append(litera)
                doar_litere.append(litera)

        nodes = []
        while len(litere) > 0:
            nodes.append(litere[0:2])
            litere = litere[2:]

        nodes.sort()
        solution += '\n******** \n'
        solution += 'Primim ponderile urmatoare: \n'

        #print(nodes)
        solution += str(nodes)

        huffman_tree = []
        huffman_tree.append(nodes)

        newnodes = self.combine(nodes, huffman_tree)
        huffman_tree.sort(reverse=True)
        solution += '\n******** \n'
        solution += '\nArborele Huffman corespunzator literelor este: \n'

        checklist = []
        for level in huffman_tree:
            for node in level:
                if node not in checklist:
                    checklist.append(node)
                else:
                    level.remove(node)
        count = 0
        for level in huffman_tree:
            #print("Nivel", count, ":", level)
            solution += 'Nivel ' + str(count) + ':' + str(level)
            solution += '\n'
            count += 1

        litera_bin = []
        if len(doar_litere) == 1:
            litera_cod = [doar_litere[0], "0"]
            litera_bin.append(litera_cod * len(mesaj))
        else:
            for litera in doar_litere:
                lit = ""
                for node in checklist:
                    if len(node) > 2 and litera in node[1]:
                        lit = lit + str(node[2])
                litera_cod = [litera, lit]
                litera_bin.append(litera_cod)

        solution += '\n******** \n'
        solution += '\nCodificarea literelor este:\n'
        for litera in litera_bin:
            #print(litera[0], litera[1])
            solution += str(litera[0]) + "\t"
            solution += str(litera[1]) + "\n"

        sir_bin = ""
        for caracter in mesaj:
            for item in litera_bin:
                if caracter in item:
                    sir_bin = sir_bin + item[1]
        solution += '\n******** \n'
        #print("Codificarea cuvantului " + mesaj + " este: " + sir_bin)
        solution += 'Codificarea cuvantului ' + str(mesaj) + ' este: ' + str(sir_bin)
        solution += '\n'
        # decodificare

        sir_bin = ""
        for i in range(0, random.randint(1, 5)):
            sir_bin = sir_bin + litera_bin[random.randint(0, 2)][1]

        sir_decod = ""
        code = ""
        for i in sir_bin:
            code = code + i
            pos = 0
            for litera in litera_bin:
                if code == litera[1]:
                    sir_decod = sir_decod + litera_bin[pos][0]
                    code = ""
                pos += 1
        solution += '\n******** \n'
        #print("Decodificarea sirului " + sir_bin + " este: " + sir_decod)
        solution += 'Decodificarea secventei ' + str(sir_bin) + ' este: ' + str(sir_decod)
        solution += '\n'
        #solution +=str(dictionar[d])
        k=0
        for i in  dictionar[d]:
            if i==sir_decod:
                solution +='Acesta reprezinta un cuvant'
                k=1

        if k==0:
            solution +='\n Acesta NU reprezinta un cuvant'

        return solution
