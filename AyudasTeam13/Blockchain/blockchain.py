import json
import hashlib
import pickle
import re


class persona:
    def __init__(self, nombre, tupla):
        self.nombre = nombre
        self.tupla = tupla


class block:
    def __init__(self, numberBlock, data, previousHash, idHash):
        self._idBlock = numberBlock
        self._data = data
        self._previousHash = previousHash
        self._idHash = idHash
        self._checker = True

    def getBlock(self):
        return [self._idBlock, self._data, self._previousHash, self._idHash]


class blockchain:
    def __init__(self):
        self.idChain = 1
        self.previous = 0
        self.blocks_list = []
        self.checkerChain = True

    def generateHash(self, data):
        pattern = r'[0-9a-zA-Z]+'
        objectStr = pickle.dumps(data)
        while True:
            id_hash = hashlib.sha256(objectStr).hexdigest()
            if re.match(pattern, id_hash):
                return id_hash

    def insertBlock(self, tupla):
        id_hash = self.generateHash(tupla)
        newBlock = block(self.idChain, [tupla.nombre, tupla.tupla], self.previous, id_hash)
        self.idChain += 1
        self.blocks_list.append(newBlock)
        file = open("tabla1.json", "w+")
        file.write(json.dumps([j.getBlock() for j in self.blocks_list]))
        self.previous = id_hash

    def updateBlock(self, oldName, newName, tabla):
        file = open("tabla1.json", "r")
        block_list = json.loads(file.read())
        file.close()

        for block in block_list:
            if oldName == block[1][0]:
                block[1][0] = newName
                # print(self.generateHash(block[0]))

        file = open("tabla1.json", "w+")
        file.write(json.dumps(block_list))
        file.close()


B = blockchain()
persona1 = persona("P1", ["id1", 34, 34.5])
persona2 = persona("P2", ["id2", 34, 34.5])
persona3 = persona("P3", ["id3", 34, 34.5])
persona4 = persona("P4", ["id4", 34, 34.5])
persona5 = persona("P5", ["id5", 34, 34.5])
persona6 = persona("P6", ["id6", 34, 34.5])
print(B.generateHash(persona1))
print(B.generateHash(persona2))
print(B.generateHash(persona3))
print(B.generateHash(persona4))
print(B.generateHash(persona5))
print(B.generateHash(persona6))
# Aqui aun no los he convertido a bytes
tabla1 = [persona1, persona2, persona3, persona4, persona5, persona6]

for i in tabla1:
    B.insertBlock(i)

B.updateBlock("P2", "nuevoNombre", tabla1)



