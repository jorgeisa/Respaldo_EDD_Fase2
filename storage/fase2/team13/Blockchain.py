import json
import hashlib
import os
import pickle
import re


class Block:
    def __init__(self, numberBlock, data, previousHash, idHash):
        self._idBlock = numberBlock
        self._data = data
        self._previousHash = previousHash
        self._idHash = idHash
        self._previousBlock = None
        self._checker = True

    def getIdBlock(self):
        return self._idBlock

    def getData(self):
        return self._data

    def getPreviousHash(self):
        return self._previousHash

    def getIdHash(self):
        return self._idHash

    def getPreviousBlock(self):
        return self._previousBlock

    def getChecker(self):
        return self._checker

    def setPreviousBlock(self, previousBlock):
        self._previousBlock = previousBlock

    def setIdHash(self, idHash):
        self._idHash = idHash

    def getBlock(self):
        return [self._idBlock, self._data, self._previousHash, self._idHash]

    def getInfoGraph(self):
        info = "Bloque: " + str(self._idBlock) + "\\nData: " + str(self._data) + "\\nHash Bloque: " + str(self._idHash) \
               + "\\nHash Ant.: " + str(self._previousHash)
        return info

    def verificarBloque(self):
        if self._previousBlock.getIdHash() == self._previousHash:
            return True
        self._checker = False
        return False


class Blockchain:
    def __init__(self):
        self.idChain = 1
        self.previous = 0
        self.blocks_list = []
        self.checkerChain = True

    def generate_hash(self, data):
        pattern = r'[0-9a-zA-Z]+'
        objectStr = pickle.dumps(data)
        while True:
            id_hash = hashlib.sha256(objectStr).hexdigest()
            if re.match(pattern, id_hash):
                return id_hash

    def insertBlock(self, tupla, nombreTabla):
        id_hash = self.generate_hash(tupla)
        newBlock = Block(self.idChain, tupla, self.previous, id_hash)
        self.idChain += 1
        self.blocks_list.append(newBlock)

        # Colocando todos los punteros al anterior bloque
        if len(self.blocks_list) != 1:
            for i in range(len(self.blocks_list)):
                if i == (len(self.blocks_list)-1):
                    self.blocks_list[i].setPreviousBlock(self.blocks_list[i-1])
                    print("Actual:", self.blocks_list[i].getIdBlock())
                    print("Anterior:", self.blocks_list[i].getPreviousBlock().getIdBlock())

        file = open(f"{nombreTabla}.json", "w+")
        file.write(json.dumps([j.getBlock() for j in self.blocks_list]))
        self.previous = id_hash


    def updateBlock(self, oldName, newName, table):

        # Cambiando valores de la lista y generando nuevo hash
        newHash = ""
        for tuple in table:
            if tuple.nombre == oldName:
                tuple.nombre = newName
                newHash = self.generate_hash(tuple)

        file = open("tabla1.json", "r")
        JSblock_list = json.loads(file.read())
        file.close()

        # Imprimiendo tuplas de personas
        for persona in table:
            print("\n", persona.nombre)
            print(persona.tupla)

        # Recorriendo JSON
        for blockJS in JSblock_list:
            if oldName == blockJS[1][0]:
                blockJS[1][0] = newName
                blockJS[3] = newHash

        # actualizando JSON
        for block in self.blocks_list:
            if oldName == block.getData()[0]:
                block.getData()[0] = newName
                block.setIdHash(newHash)

        file = open("tabla1.json", "w+")
        file.write(json.dumps(JSblock_list))
        file.close()

    def graphBlockchain(self):
        graph = 'digraph G{\n'
        graph += 'rankdir=LR;\n'
        graph += "node[shape = \"box\"]\n"
        graph += self.__graficar()
        graph += '}'
        file = open("BChain.dot", "w")
        file.write(graph)
        file.close()
        os.system('dot -Tpng BChain.dot -o BChain.png')

    def __graficar(self):
        graph = ""
        for i in range(len(self.blocks_list)):
            info = self.blocks_list[i].getInfoGraph()
            nodo = 'node' + str(self.blocks_list[i].getIdBlock())
            color = "green"

            if not (i == 0):
                brokeChain = self.blocks_list[i].verificarBloque()
                if not brokeChain:
                    color = "red"

            if not (i == (len(self.blocks_list)-1)):
                nextId = self.blocks_list[i+1].getIdBlock()
                nextNodo = 'node' + str(nextId)
                graph += nodo + f'[label="{info}", color="{color}", fixedsize="false", height="1", width="1"]\n'
                graph += nodo + '->' + nextNodo + '\n'
            else:
                graph += nodo + f'[label="{info}", color="{color}", fixedsize="false", height="1", width="1"]\n'

            if not (i == 0):
                nodoAnterior = "node" + str(self.blocks_list[i].getPreviousBlock().getIdBlock())
                graph += nodo + '->' + nodoAnterior + "\n"

        return graph
