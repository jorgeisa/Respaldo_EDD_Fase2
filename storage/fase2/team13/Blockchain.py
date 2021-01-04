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
        newBlock = Block(self.idChain, [tupla.nombre, tupla.tupla], self.previous, id_hash)
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
