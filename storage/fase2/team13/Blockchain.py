import json
import hashlib
import os
import pickle
import re
import shutil

class Block:
    def __init__(self, numberBlock, data, previousHash, idHash):
        self._idBlock = numberBlock
        self._data = data
        self._previousHash = previousHash
        self._idHash = idHash
        self._checker = True

    def getIdBlock(self):
        return self._idBlock

    def getData(self):
        return self._data

    def getPreviousHash(self):
        return self._previousHash

    def getIdHash(self):
        return self._idHash

    def getChecker(self):
        return self._checker

    def setIdHash(self, idHash):
        self._idHash = idHash

    def getBlock(self):
        return [self._idBlock, self._data, self._previousHash, self._idHash]

    def getInfoGraph(self):
        info = "Bloque: " + str(self._idBlock) + "\\nData: " + str(self._data) + "\\nHash Bloque: " + str(self._idHash)\
               + "\\nHash Ant.: " + str(self._previousHash)
        return info

    def verificarBloque(self, hashAnterior):
        if hashAnterior == self._previousHash:
            return True
        self._checker = False
        return False


class Blockchain:
    def __init__(self):
        self.idChain = 1
        self.previous = 0
        self.blocks_list = []
        self.firstHash = ""
        self.checkerChain = True

    def generate_hash(self, data):
        pattern = r'[0-9a-zA-Z]+'
        objectStr = pickle.dumps(data)
        while True:
            id_hash = hashlib.sha256(objectStr).hexdigest()
            if re.match(pattern, id_hash):
                return id_hash

    def insertBlock(self, tupla, nameJson):
        id_hash = self.generate_hash(tupla)
        newBlock = Block(self.idChain, tupla, self.previous, id_hash)
        self.blocks_list.append(newBlock)

        file = self.load_json(nameJson)
        file.write(json.dumps([j.getBlock() for j in self.blocks_list]))
        file.close()

        # only for the first
        if self.idChain == 1:
            self.firstHash = id_hash

        self.idChain += 1
        self.previous = id_hash

    def updateBlock(self, oldTuple, newTuple, nameDatabase, nameTable):
        # Cambiando valores de la lista y generando nuevo hash
        newHash = self.generate_hash(newTuple)
        nameJson = str(nameDatabase) + '_' + str(nameTable)
        file = open(os.getcwd() + "\\DataJsonBC\\" + nameJson + ".json", "r")
        JSblock_list = json.loads(file.read())
        file.close()

        # Recorriendo JSON
        for blockJS in JSblock_list:
            if oldTuple == blockJS[1][0]:
                blockJS[1][0] = newTuple
                blockJS[3] = newHash

        # actualizando JSON
        for block in self.blocks_list:
            if oldTuple == block.getData()[0]:
                block.getData()[0] = newTuple
                block.setIdHash(newHash)

        file = open("tabla1.json", "w+")
        file.write(json.dumps(JSblock_list))
        file.close()

    def graphBlockchain(self, nombreImagen):
        graph = 'digraph G{\n'
        graph += 'rankdir=LR;\n'
        graph += "node[shape = \"box\"]\n"
        graph += self.__graficar()
        graph += '}'
        file = open(f"{nombreImagen}.dot", "w")
        file.write(graph)
        file.close()
        os.system(f'dot -Tpng {nombreImagen}.dot -o {nombreImagen}.png')

    def __graficar(self):
        graph = ""
        for i in range(len(self.blocks_list)):
            info = self.blocks_list[i].getInfoGraph()
            nodo = 'node' + str(self.blocks_list[i].getIdBlock())
            color = "green"
            hashAnterior = self.blocks_list[i].getPreviousHash()

            if not (i == 0):
                brokeChain = self.blocks_list[i].verificarBloque(str(hashAnterior))
                if not brokeChain:
                    color = "red"

            if not (i == (len(self.blocks_list) - 1)):
                nextId = self.blocks_list[i + 1].getIdBlock()
                nextNodo = 'node' + str(nextId)
                graph += nodo + f'[label="{info}", color="{color}"]\n'
                graph += nodo + '->' + nextNodo + '\n'
            else:
                graph += nodo + f'[label="{info}", color="{color}"]\n'

            if not (i == 0):
                nodoAnterior = "node" + str(self.blocks_list[i-1].getIdBlock())
                graph += nodo + '->' + nodoAnterior + "\n"

        return graph


    # ------------------------------------------------------- FILES ----------------------------------------------------
    def load_json(self, nombre):
        if os.path.isdir(os.getcwd() + "\\DataJsonBC"):
            file = open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json", "+w")
            return file
        os.makedirs(os.getcwd() + "\\DataJsonBC")
        file = open(os.getcwd() + "\\DataJsonBC\\" + nombre + ".json", "+w")
        return file
