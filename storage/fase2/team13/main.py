from Funciones import *


def test():
    createDatabase('db6', 'b', 'utf8')
    createDatabase('db6', 'b', 'utf8')
    createDatabase('db3', 'bplus', 'ascii')
    createDatabase('db1', 'avl', 'ascii')
    createDatabase('db2', 'avl', 'utf8')
    #createDatabase('db8', 'dict', 'ascii')
    createDatabase('db9', 'isam', 'utf8')
    createDatabase('db4', 'json', 'utf8')
    createDatabase('db5', 'json', 'utf8')
    createDatabase('db7', 'hash', 'ascii')
    createDatabase('db9', 'hash', 'ascii')

    createTable('db6', 'Table1', 3, 'b')
    createTable('db6', 'Table2', 3, 'b')
    createTable('db3', 'Table1', 3, 'bplus')
    createTable('db3', 'Table2', 3, 'b')

    insert('db6', 'Table1', ['A1', 'B1', 'C1'], 'b')
    insert('db6', 'Table1', ['A2', 'B2', 'C2'], 'b')
    insert('db6', 'Table1', ['A3', 'B3', 'C3'], 'b')

    insert('db6', 'Table2', ['A12', 'B12', 'C12'], 'b')
    insert('db6', 'Table2', ['A22', 'B22', 'C22'], 'b')
    insert('db6', 'Table2', ['A32', 'B32', 'C32'], 'b')

test()