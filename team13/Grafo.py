
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
            print('Nuevo vertice: ', valor)
        else:
            print('Ya existe')

    def enlazar(self, origen_, destino_):
        origen = self.existe_vertice(origen_)
        destino = self.existe_vertice(destino_)

        if (origen is None) or (destino is None):
            print('No es posible enlazar')
        else:
            origen.get_lista_adyacentes().append(destino)

    def recorrido_anchura(self):
        lista_aux = []
        for a in self.lista_vertices:
            if lista_aux.__contains__(a) is False:
                lista_aux.append(a)
            # Recorriendo nodos adyacentes y que no estén en la lista
            for b in a.get_lista_adyacentes():
                if lista_aux.__contains__(b):
                    pass
                else:
                    lista_aux.append(b)

        print('RECORRIDO ANCHURA')
        if lista_aux is not None:
            for i in lista_aux:
                print(i.get_valor())

    def graficar(self):
        aux = []
        cadena = ''
        cadena += 'Digraph G {\n'

        for i in range(0, len(self.lista_vertices)):
            temp= self.lista_vertices[i]
            if aux.__contains__(temp) is False:
                aux.append(temp)
                cadena += f'node{hash(temp)} [label="{temp.get_valor()}" ]\n'
            for j in range(0, len(temp.get_lista_adyacentes())):
                cadena += f'node{hash(temp)} -> node{hash(temp.get_lista_adyacentes()[j])}\n'

        cadena += '}'
        print(cadena)


g = Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_vertice(4)
g.agregar_vertice(5)

g.enlazar(1, 2)
g.enlazar(1, 3)
g.enlazar(2, 3)
g.enlazar(2, 4)
g.enlazar(3, 5)

g.recorrido_anchura()
g.graficar()
