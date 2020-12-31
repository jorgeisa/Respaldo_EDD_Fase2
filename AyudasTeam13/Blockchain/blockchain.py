import json
import hashlib
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

    def getBlock(self):
        return [self._idBlock, self._data, self._previousHash, self._idHash]


class blockchain:
    def __init__(self):
        self.idChain = 1
        self.previous = 0
        self.blocks_list = []

    def generateHash(self, data):
        pattern = r'[0-9a-zA-Z]+'
        nonce = 0
        while True:
            id_hash = hashlib.sha256(data).hexdigest()
            nonce += 1
            if re.match(pattern, id_hash):
                print("Lo encontro, nonce:", nonce)
                return id_hash


B = blockchain()
persona1 = persona("P1", ["id", 34, 34.5])
print(B.generateHash(b""))
