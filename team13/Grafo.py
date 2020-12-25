import os

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.lista_adyacentes = []

    def get_valor(self):
        return self.valor

    def set_numero(self, valor):
        self.valor = valor

    def get_lista_adyacentes(self):
        return self.lista_adyacentes

    def set_lista_adyacentes(self, lista):
        self.lista_adyacentes = lista


class Grafo:
    def __init__(self):
        self.lista_vertices = []

    def existe_vertice(self, valor):
        for vertice in self.lista_vertices:
            if vertice.get_valor() == valor:
                return vertice
        return None

    def agregar_vertice(self, valor):
        vertice = self.existe_vertice(valor)
        if vertice is None:
            self.lista_vertices.append(Vertice(valor))
        else:
            print('Ya existe')

    def enlazar(self, origen_, destino_):
        origen = self.existe_vertice(origen_)
        destino = self.existe_vertice(destino_)

        if (origen is None) or (destino is None):
            print('No es posible enlazar')
        else:
            origen.get_lista_adyacentes().append(destino)

    def graficar(self):
        cadena = 'digraph G{\n'
        cadena += "node[shape = \"record\"]\n"

        aux = []
        for i in range(0, len(self.lista_vertices)):
            temp = self.lista_vertices[i]
            if aux.__contains__(temp) is False:
                aux.append(temp)
                cadena += f'node{hash(temp)} [label="{temp.get_valor()}" ]\n'
            for j in range(0, len(temp.get_lista_adyacentes())):
                cadena += f'node{hash(temp)} -> node{hash(temp.get_lista_adyacentes()[j])}\n'

        cadena += '}'
        file = open("Grafo.circo", "w")
        file.write(cadena)
        file.close()
        os.system('circo -Tpng Grafo.circo -o Grafo.png')



    def buscar(self, valor):
        for i in range(0, len(self.lista_vertices)):
            if self.lista_vertices[i].get_valor() == valor:
                return self.lista_vertices[i]
        return None

    def anchura(self, inicio):
        visitados = []
        cola = []
        origen = self.buscar(inicio)
        cola.append(origen)

        while cola:
            actual = cola.pop(0)

            if actual not in visitados:
                print(actual.get_valor(), end=' -')
                visitados.append(actual)

            # Si los vertices adyacentes no han sido visitados, agregar a la cola
            for i in actual.get_lista_adyacentes():
                if i not in visitados:
                    cola.append(i)


g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_vertice('H')
g.agregar_vertice('T')
g.agregar_vertice('R')

g.enlazar('B', 'H')
g.enlazar('C', 'R')
g.enlazar('D', 'B')
g.enlazar('D', 'C')
g.enlazar('H', 'A')
g.enlazar('H', 'T')
g.enlazar('H', 'D')
g.enlazar('R', 'H')

print('RECORRIDO POR ANCHURA')
g.anchura('D')
print()
g.graficar()
