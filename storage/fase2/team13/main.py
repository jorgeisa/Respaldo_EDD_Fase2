# This is the test for the branch BlockchainFunction
from Funciones import *
import os


def testDict():
    dict = {"valor1": [1, 2, 3], "valor2": [4, 5, 6]}
    dict.update({"valor1": [0, 0, 0, 0, 0, 0, 0]})
    dict.get("valor2")[2] = 888
    print(dict)
    # print(os.getcwd() + "\\Data")
    # os.mkdir(os.getcwd() + "/Data")
    # os.mkdir(os.getcwd() + '/data/jsonBC')
    if os.path.isdir(os.getcwd() + "\\Data\\jsonBC"):
        print(True)
    else:
        os.makedirs(os.getcwd() + "\\Data\\JsonBC")
        # os.mkdir(os.getcwd() + "\\Data\\Json")
        print(False)


def test():
    print('#' * 10 + '  DATABASES  ')
    print(createDatabase('db6', 'b', 'utf8'), end='-')
    print(createDatabase('db6', 'bplus', 'ascii'), end='-')  # 2, exist db
    print(createDatabase('db1', 'avl', 'asci'), end='-')  # 4, encoding incorrect
    print(createDatabase('db2', 'avl', 'utf8'), end='-')
    print(createDatabase('db8', 'isam', 'utf8'), end='-')
    print(createDatabase('db4', 'jsona', 'utf8'), end='-')  # 3, mode incorrect
    print(createDatabase('db5', 'json', 'utf8'), end='-')
    print(createDatabase('db7', 'hash', 'ascii'))

    print('#' * 10 + '  TABLES  ')
    print(createTable('db6', 'Table1_DB6', 3), end='-')
    print(createTable('db6', 'Table2_DB6', 2), end='-')
    print(createTable('db6', 'Table3_DB6', 4), end='-')
    print(createTable('db7', 'Table1_DB7', 4), end='-')
    print(createTable('db7', 'Table2_DB7', 3))

    print('#' * 10 + '  REGISTERS  ')
    print('DB6 - TABLE1', end=': ')
    print(insert('db66', 'Table1', ['A1', 'B1', 'C1']), end='-')  # 2, database doesn't exist
    print(insert('db6', 'Table1', ['A2', 'B2', 'C2']), end='-')
    print(insert('db6', 'Table1', ['A3', 'B3', 'C3']))

    print('DB6 - TABLE2', end=': ')
    print(insert('db6', 'Table2', ['A12', 'B12', 'C12']), end='-')
    print(insert('db6', 'Table2', ['A22', 'B22', 'C22']), end='-')
    print(insert('db6', 'Table2', ['A32', 'B32', 'C32']))

    print('#' * 10 + '  ALTER_DATABASE_MODE')
    print('BEFORE')
    dictionary = load('metadata')
    showDict(dictionary)
    showMode('b')
    showMode('bplus')

    print('alterDatabaseMode: ', alterDatabaseMode('db6', 'bplus'))
    print('AFTER')
    dictionary = load('metadata')
    showDict(dictionary)
    showMode('b')
    showMode('bplus')

    j = checkMode('b')
    print('MODE B - DB6: ', j.showTables('db6'))

    j = checkMode('bplus')
    print('MODE BPLUS - DB6', j.showTables('db6'))

    print(showTables('db6'))

    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', [0]))  # 0
    print(alterTableAddFK('db63', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', [0]))  # 2
    print(alterTableAddFK('db6', 'Table2', 'Rel1', [0, 1], 'Table1_DB6', [0]))  # 3
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1', [0]))  # 3
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [], 'Table1_DB6', [0]))  # 4
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', []))  # 4
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', [0]))  # 6
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel2', [0, 1], 'Table1_DB6', [0]))  # 0
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel3', [0, 1], 'Table1_DB6', [0]))  # 0
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel4', [0, 1], 'Table1_DB6', [0]))  # 0
    showFK(load('FK'))

    print(alterTableDropFK('db63', 'Table2_DB6', 'Rel1'))  # 2
    print(alterTableDropFK('db6', 'Table4', 'Rel3'))  # 3
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel3'))  # 4
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel1'))  # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel2'))  # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel3'))  # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel4'))  # 0
    showFK(load('FK'))


def test2():
    print('#' * 20 + ' Create Database')
    print(createDatabase('db1', 'avl', 'utf8'), end='-')
    print(createDatabase('db2', 'b', 'utf8'), end='-')
    print(createDatabase('db3', 'bplus', 'utf8'))

    print('#' * 20 + ' Create Table')
    print(createTable('db1', 'Table1_DB1', 3), end='-')
    print(createTable('db2', 'Table1_DB2', 3))

    print('#' * 20 + ' Insert')
    print(insert('db1', 'Table1_DB1', ['A1', 'B1', 'C1']), end='-')
    print(insert('db1', 'Table1_DB1', ['A2', 'B2', 'C2']), end='-')
    print(insert('db1', 'Table1_DB1', ['A3', 'B3', 'C3']), end='-')
    print(insert('db2', 'Table1_DB2', ['A1_DB2', 'B1', 'C1']), end='-')
    print(insert('db2', 'Table1_DB2', ['A2_DB2', 'B2', 'C2']), end='-')
    print(insert('db2', 'Table1_DB2', ['A3_DB2', 'B3', 'C3']))

    print('#' * 20 + ' Extract Row')
    print(extractRow('db1', 'Table1_DB1', [1]))

    print('#' * 20 + ' Update')
    print(update('db1', 'Table1_DB1', {1: 'B1_Update'}, [1]))

    print('#' * 20 + ' Extract Row')
    print(extractRow('db1', 'Table1_DB1', [1]))

    print('#' * 20 + ' delete')
    print(delete('db2', 'Table1_DB2', [0]))
    print(delete('db2', 'Table1_DB2', [1]))

    print('#' * 20 + ' Extract Row')
    print(extractRow('db2', 'Table1_DB2', [2]))

    print('#' * 20 + ' Extract Row Before')
    print(extractRow('db2', 'Table1_DB2', [0]))
    print(extractRow('db2', 'Table1_DB2', [1]))
    print(extractRow('db2', 'Table1_DB2', [2]))

    print('#' * 20 + ' truncate')
    print(truncate('db2', 'Table1_DB2'))

    print('#' * 20 + ' Extract Row After')
    print(extractRow('db2', 'Table1_DB2', [0]))
    print(extractRow('db2', 'Table1_DB2', [1]))
    print(extractRow('db2', 'Table1_DB2', [2]))


def test3():
    print('#' * 20 + ' Create Database')
    print(createDatabase('db1', 'avl', 'utf8'), end='-')
    print(createDatabase('db2', 'b', 'utf8'), end='-')
    print(createDatabase('db3', 'bplus', 'utf8'), end='-')
    print(createDatabase('db4', 'isam', 'utf8'), end='-')
    print(createDatabase('db5', 'json', 'utf8'), end='-')
    print(createDatabase('db6', 'hash', 'utf8'))

    print('#' * 20 + ' Create Table')
    print(createTable('db1', 'Table1_DB1', 3), end='-')
    print(createTable('db1', 'Table2_DB1', 3), end='-')
    print(createTable('db1', 'Table3_DB1', 3), end='-')
    print(createTable('db1', 'Table4_DB1', 3), end='-')

    print(createTable('db2', 'Table1_DB2', 3), end='-')
    print(createTable('db2', 'Table2_DB2', 3), end='-')
    print(createTable('db2', 'Table3_DB2', 3), end='-')
    print(createTable('db2', 'Table4_DB2', 3), end='-')

    print(createTable('db3', 'Table1_DB3', 3), end='-')
    print(createTable('db3', 'Table2_DB3', 3), end='-')
    print(createTable('db3', 'Table3_DB3', 3), end='-')
    print(createTable('db3', 'Table4_DB3', 3), end='-')

    print(createTable('db4', 'Table1_DB4', 3), end='-')
    print(createTable('db4', 'Table2_DB4', 3), end='-')
    print(createTable('db4', 'Table3_DB4', 3), end='-')
    print(createTable('db4', 'Table4_DB4', 3), end='-')

    print(createTable('db5', 'Table1_DB5', 3), end='-')
    print(createTable('db5', 'Table2_DB5', 3), end='-')
    print(createTable('db5', 'Table3_DB5', 3), end='-')
    print(createTable('db5', 'Table4_DB5', 3), end='-')

    print(createTable('db6', 'Table1_DB6', 3), end='-')
    print(createTable('db6', 'Table2_DB6', 3), end='-')
    print(createTable('db6', 'Table3_DB6', 3), end='-')
    print(createTable('db6', 'Table4_DB6', 3))

    print()
    print('#' * 20 + ' Security Mode ' + '#' * 20)
    print(safeModeOn('db1', 'Table1_DB1'))

    print('#' * 20 + ' Insert')
    print(insert('db1', 'Table1_DB1', ['A1', 'B1', 'C1']), end='-')
    print(insert('db1', 'Table1_DB1', ['A11', 'B12', 'C13']), end='-')
    print(insert('db1', 'Table1_DB1', ['A21', 'B22', 'C23']), end='-')
    print(insert('db1', 'Table1_DB1', ['31', 'B32', 'C33']), end='-')
    print(insert('db1', 'Table2_DB1', ['A2', 'B2', 'C2']), end='-')
    print(insert('db1', 'Table3_DB1', ['A3', 'B3', 'C3']), end='-')

    print(insert('db2', 'Table1_DB2', ['A1', 'B1', 'C1']), end='-')
    print(insert('db2', 'Table2_DB2', ['A2', 'B2', 'C2']), end='-')
    print(insert('db2', 'Table3_DB2', ['A3', 'B3', 'C3']), end='-')

    print(insert('db3', 'Table1_DB3', ['A1', 'B1', 'C1']), end='-')
    print(insert('db3', 'Table2_DB3', ['A2', 'B2', 'C2']), end='-')
    print(insert('db3', 'Table3_DB3', ['A3', 'B3', 'C3']), end='-')

    print(insert('db4', 'Table1_DB4', ['A1', 'B1', 'C1']), end='-')
    print(insert('db4', 'Table2_DB4', ['A2', 'B2', 'C2']), end='-')
    print(insert('db4', 'Table3_DB4', ['A3', 'B3', 'C3']), end='-')

    print(insert('db5', 'Table1_DB5', ['A1', 'B1', 'C1']), end='-')
    print(insert('db5', 'Table2_DB5', ['A2', 'B2', 'C2']), end='-')
    print(insert('db5', 'Table3_DB5', ['A3', 'B3', 'C3']), end='-')

    print(insert('db6', 'Table1_DB6', ['A1', 'B1', 'C1']), end='-')
    print(insert('db6', 'Table2_DB6', ['A2', 'B2', 'C2']), end='-')
    print(insert('db6', 'Table3_DB6', ['A3', 'B3', 'C3']))


    print('#' * 20 + ' Show Tables')
    print(showTables('db1'))
    print(showTables('db2'))
    print(showTables('db3'))
    print(showTables('db4'))
    print(showTables('db5'))
    print(showTables('db6'))

    print()
    print('#' * 20 + ' Security Mode ' + '#' * 20)
    print(safeModeOff('db1', 'Table1_DB1'))
    print(safeModeOn('db1', 'Table1_DB1'))

    dictionary = load('metadata')
    showDict(dictionary)

    print('#' * 20 + ' Extract Table')
    print(extractTable('db1', 'Table1_DB1'))
    print(extractTable('db2', 'Table1_DB2'))
    print(extractTable('db3', 'Table1_DB3'))
    print(extractTable('db4', 'Table1_DB4'))
    print(extractTable('db5', 'Table1_DB5'))
    print(extractTable('db6', 'Table1_DB6'))

    print('#' * 20 + ' Extract Range Table')
    print(extractRangeTable('db1', 'Table1_DB1', 0, 'A1', 'C1'))
    print(extractRangeTable('db2', 'Table1_DB2', 0, 'A1', 'C1'))
    print(extractRangeTable('db3', 'Table1_DB3', 0, 'A1', 'C1'))
    print(extractRangeTable('db4', 'Table1_DB4', 0, 'A1', 'C1'))
    print(extractRangeTable('db5', 'Table1_DB5', 0, 'A1', 'C1'))
    print(extractRangeTable('db6', 'Table1_DB6', 0, 'A1', 'C1'))

    print('#' * 20 + ' UPDATE' + '#' * 20)
    print(update('db3', 'Table1_DB3', {1: 'JORGE'}, [1]))
    print(extractTable('db3', 'Table1_DB3'))

    print('#' * 20 + ' Alter Add PK')
    print(alterAddPK('db1', 'Table1_DB1', [1]))
    print(alterAddPK('db2', 'Table1_DB2', [1]))
    print(alterAddPK('db3', 'Table1_DB3', [2]))
    print(alterAddPK('db4', 'Table1_DB4', [1]))
    print(alterAddPK('db5', 'Table1_DB5', [1]))
    print(alterAddPK('db6', 'Table1_DB6', [1]))

    print('#' * 20 + ' UPDATE' + '#' * 20)
    print(update('db3', 'Table1_DB3', {1: 'JORGE8'}, ['C1']))
    print(extractTable('db3', 'Table1_DB3'))

    print('#' * 20 + ' Alter Drop PK')
    print(alterDropPK('db1', 'Table1_DB1'))
    print(alterDropPK('db2', 'Table1_DB2'))
    print(alterDropPK('db3', 'Table1_DB3'))
    print(alterDropPK('db4', 'Table1_DB4'))
    print(alterDropPK('db5', 'Table1_DB5'))
    print(alterDropPK('db6', 'Table1_DB6'))

    print('#' * 20 + ' Alter Table')
    print(alterTable('db1', 'Table1_DB1', 'Table1New_DB1'))
    print(alterTable('db2', 'Table1_DB2', 'Table1New_DB2'))
    print(alterTable('db3', 'Table1_DB3', 'Table1New_DB3'))
    print(alterTable('db4', 'Table1_DB4', 'Table1New_DB4'))
    print(alterTable('db5', 'Table1_DB5', 'Table1New_DB5'))
    print(alterTable('db6', 'Table1_DB6', 'Table1New_DB6'))

    dictionary = load('metadata')
    showDict(dictionary)

    print('#' * 20 + ' Alter drop Column')
    print(alterDropColumn('db1', 'Table2_DB1', 1))
    print(alterDropColumn('db2', 'Table2_DB2', 1))
    print(alterDropColumn('db3', 'Table2_DB3', 1))
    print(alterDropColumn('db4', 'Table2_DB4', 1))
    print(alterDropColumn('db5', 'Table2_DB5', 1))
    print(alterDropColumn('db6', 'Table2_DB6', 1))

    print('#' * 20 + ' drop Table')
    print(dropTable('db1', 'Table3_DB1'))
    print(dropTable('db2', 'Table3_DB2'))
    print(dropTable('db3', 'Table3_DB3'))
    print(dropTable('db4', 'Table3_DB4'))
    print(dropTable('db5', 'Table3_DB5'))
    print(dropTable('db6', 'Table3_DB6'))

    dictionary = load('metadata')
    showDict(dictionary)


def testCompress():
    print(createDatabase('db1', 'b', 'utf8'))
    print(createTable('db1', 'Table1_DB1', 3))
    print(insert('db1', 'Table1_DB1', ['Ya valines todos', 'F con el proyecto xdxd', 123]))
    print(insert('db1', 'Table1_DB1', ['ABC', 'DEF', 'GHI']))

    print('#' * 10 + ' Before')
    print(extractTable('db1', 'Table1_DB1'))

    print(alterTableCompress('db1', 'Table1_DB1', 2))
    # table = extractTable('db1', 'Table1_DB1')
    # print('Prueba')
    # for tuple in table[0]:
    #     print("Tamaño Real %d" % len(tuple))
    print('#' * 10 + ' After')
    print(extractTable('db1', 'Table1_DB1'))

    print(alterTableDecompress('db1', 'Table1_DB1'))
    print('#' * 10 + ' Decompress')
    print(extractTable('db1', 'Table1_DB1'))


test3()
# testCompress()
# test()
# testDict()
