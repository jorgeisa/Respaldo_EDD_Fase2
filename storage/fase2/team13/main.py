from Funciones import *
import Funciones as j

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

    print(alterTableDropFK('db63', 'Table2_DB6', 'Rel1'))  # 2
    print(alterTableDropFK('db6', 'Table4', 'Rel3'))  # 3
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel3'))  # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel1'))  # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel2'))  # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel3'))  # 4
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

    print(alterDatabaseEncoding('db1', 'iso-8859-1'))
    print(extractTable('db1', 'Table1_DB1'))
    print(checksumDatabase('db1', 'MD5'))
    print(checksumDatabase('db1', 'MD5'))
    print(insert('db1', 'Table1_DB1', ['A4', 'B4', 'C4']))
    print(checksumDatabase('db1', 'MD5'))
    print('----------------------------------------------')
    print(checksumTable('db2', 'Table1_DB2', 'SHA256'))
    print(checksumTable('db2', 'Table1_DB2', 'SHA256'))
    print(insert('db2', 'Table1_DB2', ['A4_DB2', 'B4', 'C4']))
    print(checksumTable('db2', 'Table1_DB2', 'SHA256'))
    print(showChecksums(load('checksum')))
    print('----------------------------------------------')
    print(alterTableCompress('db1', 'Table1_DB1', 8))
    print(extractTable('db1', 'Table1_DB1'))
    print(alterTableDecompress('db1', 'Table1_DB1', ))
    print(extractTable('db1', 'Table1_DB1'))

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

    print('#' * 20 + ' Insert')
    print(insert('db1', 'Table1_DB1', ['A1', 'B1', 'C1']), end='-')
    print(insert('db1', 'Table2_DB1', ['A2', 'B2', 'C2']), end='-')
    print(insert('db1', 'Table3_DB1', ['A3', 'B3', 'C3']), end='-')

    print(insert('db2', 'Table1_DB2', ['A', 'B', 'C']), end='-')
    print(insert('db2', 'Table1_DB2', ['AA', 'BB', 'CC']), end='-')
    print(insert('db2', 'Table1_DB2', ['AAA', 'BBB', 'CCC']), end='-')
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

    print()
    print('#' * 20 + ' EXTRACTROW ' + '#' * 20)
    print(extractRow('db1', 'Table1_DB1', [2]))

    print('#' * 20 + ' Show Tables')
    print(showTables('db1'))
    print(showTables('db2'))
    print(showTables('db3'))
    print(showTables('db4'))
    print(showTables('db5'))
    print(showTables('db6'))

    print()
    print('#' * 20 + ' Security Mode ' + '#' * 20)
    print(safeModeOn('db1', 'Table1_DB1'))
    print(insert('db1', 'Table1_DB1', ['A11', 'B12', 'C13']), end='-')
    print(insert('db1', 'Table1_DB1', ['A21', 'B22', 'C23']), end='-')
    print(insert('db1', 'Table1_DB1', ['A31', 'B32', 'C33']), end='-')
    print(insert('db1', 'Table1_DB1', ['41', 'B42', 'C43']))
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

    print('#' * 20 + ' Alter Add PK')
    print(alterAddPK('db1', 'Table1_DB1', [1]))
    print(alterAddPK('db2', 'Table1_DB2', [1]))
    print(alterAddPK('db3', 'Table1_DB3', [1]))
    print(alterAddPK('db4', 'Table1_DB4', [1]))
    print(alterAddPK('db5', 'Table1_DB5', [1]))
    print(alterAddPK('db6', 'Table1_DB6', [1]))

    print('#' * 20 + ' UPDATE' + '#' * 20)
    print(update('db1', 'Table1_DB1', {0: 'JORGE8'}, ['B32']))
    # print(safeModeOff('db1', 'Table1_DB1'))

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
    print(createDatabase('db2', 'avl', 'utf8'))

    print(createTable('db1', 'Table1_DB1', 3))
    print(createTable('db1', 'Table2_DB1', 3))
    print(createTable('db1', 'Table3_DB1', 3))
    print(createTable('db2', 'Table1_DB2', 3))

    print(insert('db1', 'Table1_DB1', ['Ya valines todos', 'F con el proyecto xdxd', 123]))
    print(insert('db1', 'Table1_DB1', ['ABC', 'DEF', 'GHI']))
    print(insert('db1', 'Table2_DB1', ['A ver si funciona esto xd', 'F en el chat', 'Si sale el lab']))
    print(insert('db1', 'Table3_DB1', ['ya super F', 'Isaac es mal coordinador', 'Son bromas es un papucho']))
    print(insert('db2', 'Table1_DB2',
                 ['Test de compresion de las bases de datos xdxd', 'Ya no se que mas poner en estas tuplas jsjsjs',
                  'F en el chat']))

    print('#' * 10 + ' Before')
    print(extractTable('db1', 'Table1_DB1'))
    print(extractTable('db1', 'Table2_DB1'))
    print(extractTable('db1', 'Table3_DB1'))
    print(extractTable('db2', 'Table1_DB2'))

    print(alterDatabaseCompress('db2', 6))

    print('#' * 10 + ' After')
    print(extractTable('db1', 'Table1_DB1'))
    print(extractTable('db1', 'Table2_DB1'))
    print(extractTable('db1', 'Table3_DB1'))
    print(extractTable('db2', 'Table1_DB2'))

    print(alterDatabaseDecompress('db2'))

    print('#' * 10 + ' After')
    print(extractTable('db1', 'Table1_DB1'))
    print(extractTable('db1', 'Table2_DB1'))
    print(extractTable('db1', 'Table3_DB1'))
    print(extractTable('db2', 'Table1_DB2'))

    # print(alterTableCompress('db1', 'Table1_DB1', 6))
    # # table = extractTable('db1', 'Table1_DB1')
    # # print('Prueba')
    # # for tuple in table[0]:
    # #     print("Tamaño Real %d" % len(tuple))
    # print('#' * 10 + ' After')
    # print(extractTable('db1', 'Table1_DB1'))
    #
    # print(alterTableDecompress('db1', 'Table1_DB1'))
    # print('#' * 10 + ' Decompress')
    # print(extractTable('db1', 'Table1_DB1'))


def final_test():

    # def createDatabase(database: str, mode: string, encoding: string) -> int:
    # mode: 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'
    # encoding: 'ascii', 'iso-8859-1', 'utf8'
    # {0: success, 1: error, 2: db exist, 3: incorrect mode, 4: incorrect encoding
    print('#' * 20 + ' Create Database' + '#' * 20)
    print(j.createDatabase('db1', 'avl', 'ascii'), end='-')
    print(j.createDatabase('db2', 'avl', 'ascii'), end='-')
    print(j.createDatabase('db3', 'avl', 'ascii'), end='-')
    print(j.createDatabase('db4', 'b', 'ascii'), end='-')
    print(j.createDatabase('db5', 'b', 'ascii'), end='-')
    print(j.createDatabase('db6', 'b', 'ascii'), end='-')
    print(j.createDatabase('db7', 'bplus', 'ascii'), end='-')
    print(j.createDatabase('db8', 'bplus', 'iso-8859-1'), end='-')
    print(j.createDatabase('db9', 'bplus', 'iso-8859-1'), end='-')
    print(j.createDatabase('db10', 'dict', 'iso-8859-1'), end='-')
    print(j.createDatabase('db11', 'dict', 'iso-8859-1'), end='-')
    print(j.createDatabase('db12', 'dict', 'iso-8859-1'), end='-')
    print(j.createDatabase('db13', 'isam', 'iso-8859-1'), end='-')
    print(j.createDatabase('db14', 'isam', 'iso-8859-1'), end='-')
    print(j.createDatabase('db15', 'isam', 'utf8'), end='-')
    print(j.createDatabase('db16', 'json', 'utf8'), end='-')
    print(j.createDatabase('db17', 'json', 'utf8'), end='-')
    print(j.createDatabase('db18', 'json', 'utf8'), end='-')
    print(j.createDatabase('db19', 'hash', 'utf8'), end='-')
    print(j.createDatabase('db20', 'hash', 'utf8'), end='-')
    print(j.createDatabase('db21', 'hash', 'utf8'))

    print()
    print('#' * 20 + ' Show Databases ' + '#' * 20)
    print(j.showDatabases())

    # def createTable(database: str, table: str, numberColumns: int) -> int:
    # {0: success, 1: error, 2: db not exist, 3: table exist
    print()
    print('#' * 20 + ' Create Table ' + '#' * 20)
    print(j.createTable('db1', 'T1DB1', 1), end='-')
    print(j.createTable('db1', 'T2DB1', 1), end='-')
    print(j.createTable('db1', 'T3DB1', 1))

    print(j.createTable('db4', 'T1DB4', 2), end='-')
    print(j.createTable('db4', 'T2DB4', 2), end='-')
    print(j.createTable('db4', 'T3DB4', 2))

    print(j.createTable('db7', 'T1DB7', 3), end='-')
    print(j.createTable('db7', 'T2DB7', 3), end='-')
    print(j.createTable('db7', 'T3DB7', 3))

    print(j.createTable('db8', 'T1DB8', 4), end='-')
    print(j.createTable('db8', 'T2DB8', 4), end='-')
    print(j.createTable('db8', 'T3DB8', 4))

    print(j.createTable('db9', 'T1DB9', 5), end='-')
    print(j.createTable('db9', 'T2DB9', 5), end='-')
    print(j.createTable('db9', 'T3DB9', 5))

    print(j.createTable('db10', 'T1DB10', 3), end='-')
    print(j.createTable('db10', 'T2DB10', 3), end='-')
    print(j.createTable('db10', 'T3DB10', 3))

    print(j.createTable('db13', 'T1DB13', 3), end='-')
    print(j.createTable('db13', 'T2DB13', 3), end='-')
    print(j.createTable('db13', 'T3DB13', 3))

    print(j.createTable('db16', 'T1DB16', 3), end='-')
    print(j.createTable('db16', 'T2DB16', 3), end='-')
    print(j.createTable('db16', 'T3DB16', 3))

    print(j.createTable('db19', 'T1DB19', 3), end='-')
    print(j.createTable('db19', 'T2DB19', 3), end='-')
    print(j.createTable('db19', 'T3DB19', 3))

    # def insert(database: str, table: str, register: list) -> int:
    # {0: success, 1: error, 2: db not exist, 3: table not exist, 4: PK duplicated, 5: out limit
    print('#' * 20 + ' Insert ' + '#' * 20)
    print(j.insert('db1', 'T1DB1', ['A1']), end='-')
    print(j.insert('db1', 'T2DB1', ['B1']), end='-')
    print(j.insert('db1', 'T3DB1', ['C1']))

    print(j.insert('db4', 'T1DB4', ['A1', 'A2']), end='-')
    print(j.insert('db4', 'T2DB4', ['B1', 'B2']), end='-')
    print(j.insert('db4', 'T3DB4', ['C1', 'C2']))

    print(j.insert('db7', 'T1DB7', ['A1', 'A2', 'A3']), end='-')
    print(j.insert('db7', 'T2DB7', ['B1', 'B2', 'B3']), end='-')
    print(j.insert('db7', 'T3DB7', ['C1', 'C2', 'C3']))

    print(j.insert('db10', 'T1DB10', ['A1', 'A2', 'A3']), end='-')
    print(j.insert('db10', 'T2DB10', ['B1', 'B2', 'B3']), end='-')
    print(j.insert('db10', 'T3DB10', ['C1', 'C2', 'C3']))

    print(j.insert('db13', 'T1DB13', ['A1', 'A2', 'A3']), end='-')
    print(j.insert('db13', 'T2DB13', ['B1', 'B2', 'B3']), end='-')
    print(j.insert('db13', 'T3DB13', ['C1', 'C2', 'C3']))

    print(j.insert('db16', 'T1DB16', ['A1', 'A2', 'A3']), end='-')
    print(j.insert('db16', 'T2DB16', ['B1', 'B2', 'B3']), end='-')
    print(j.insert('db16', 'T3DB16', ['C1', 'C2', 'C3']))

    print(j.insert('db19', 'T1DB19', ['A1', 'A2', 'A3']), end='-')
    print(j.insert('db19', 'T2DB19', ['B1', 'B2', 'B3']), end='-')
    print(j.insert('db19', 'T3DB19', ['C1', 'C2', 'C3']))

    # def showDatabases() -> list:
    # {[]: error, not db }
    # dictionary = load('metadata')
    # showDict(dictionary)
    print()
    print('#' * 20 + ' showDatabases ' + '#' * 20)
    print(j.showDatabases())

    print()
    print('#' * 20 + ' extract Table Prueba1: sin cambiar nombre ' + '#' * 20)
    print(j.extractTable("db1", "T1DB1"))
    print(j.extractTable("db4", "T1DB4"))
    print(j.extractTable("db7", "T1DB7"))
    print(j.extractTable("db10", "T1DB10"))
    print(j.extractTable("db13", "T1DB13"))
    print(j.extractTable("db16", "T1DB16"))
    print(j.extractTable("db19", "T1DB19"))

    print()
    print('#' * 20 + ' Show Tables y exctract Table ISAM ' + '#' * 20)
    print(j.showTables("db13"))
    print(j.extractTable("db13", "T3DB13"))  # isam mode

    # def alterDatabase(databaseOld, databaseNew) -> int:
    # {0: success, 1: error, 2: dbOld not exist, 3: dbNew exist}
    print()
    print('#' * 20 + ' alterdatabase ' + '#' * 20)
    print(j.alterDatabase("db1", "db101"))
    print(j.alterDatabase("db4", "db104"))
    print(j.alterDatabase("db7", "db107"))
    print(j.alterDatabase("db10", "db110"))
    print(j.alterDatabase("db13", "db113"))
    print(j.alterDatabase("db16", "db116"))
    print(j.alterDatabase("db19", "db119"))

    print()
    print('#' * 20 + ' Show Databases ' + '#' * 20)
    print(j.showDatabases())

    print()
    print('#' * 20 + ' drop database ' + '#' * 20)
    # def dropDatabase(database: str) -> int:
    # {0: success, 1: error, 2: db not exist}
    print(j.dropDatabase("db2"))
    print(j.dropDatabase("db3"))
    print(j.dropDatabase("db5"))
    print(j.dropDatabase("db6"))
    print(j.dropDatabase("db8"))
    print(j.dropDatabase("db9"))
    print(j.dropDatabase("db11"))

    print()
    print('#' * 20 + ' Show Databases ' + '#' * 20)
    print(j.showDatabases())

    print()
    # def showDatabases() -> list:
    # {[]: error, not tables, None: not db }
    print('#' * 20 + ' showTables ' + '#' * 20)
    print(j.showTables("db101"))
    print(j.showTables("db104"))
    print(j.showTables("db107"))
    print(j.showTables("db110"))
    print(j.showTables("db113"))
    print(j.showTables("db116"))
    print(j.showTables("db119"))

    print()
    # def extractTable(database: str, table: str) -> list:
    # {[]: , []: not registers, None: error}
    print('#' * 20 + ' extract Table ' + '#' * 20)
    print(j.extractTable("db101", "T1DB1"))
    print(j.extractTable("db104", "T1DB4"))
    print(j.extractTable("db107", "T1DB7"))
    print(j.extractTable("db110", "T1DB10"))
    print(j.extractTable("db113", "T3DB13"))
    print(j.extractTable("db116", "T1DB16"))
    print(j.extractTable("db119", "T1DB19"))

    print()
    print('#' * 20 + ' extract Range Table ' + '#' * 20)
    # def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    # {[]: not registers, None: not db, not table, error}
    print(j.extractRangeTable("db1", "T1DB1", 1, "A", "A"))

    print('#' * 20 + ' alter Drop PK ' + '#' * 20)
    print(j.alterDropPK('db101', 'T1DB1'))
    print(j.alterDropPK('db104', 'T1DB4'))
    print(j.alterDropPK('db107', 'T1DB7'))
    print(j.alterDropPK('db110', 'T1DB10'))
    print(j.alterDropPK('db113', 'T1DB13'))
    print(j.alterDropPK('db116', 'T1DB16'))
    print(j.alterDropPK('db119', 'T1DB19'))

    print()
    # def alterAddPK(database: str, table: str, columns: list) -> int:
    # {0: success, 1: error, 2: db not exist, 3: table not exist, 4: PK exist}
    print('#' * 20 + ' alter Add PK ' + '#' * 20)
    print(j.alterAddPK('db101', 'T1DB1', [0]))
    print(j.alterAddPK('db104', 'T1DB4', [0]))
    print(j.alterAddPK('db107', 'T1DB7', [0]))
    print(j.alterAddPK('db110', 'T1DB10', [0]))
    print(j.alterAddPK('db113', 'T1DB13', [0]))
    print(j.alterAddPK('db116', 'T1DB16', [0]))
    print(j.alterAddPK('db119', 'T1DB19', [0]))

    print()
    # def alterDropPK(database: str, table: str) -> int:
    # {0: success, 1: error, 2: db not exist, 3: table not exist, 4: PK not exist}
    print('#' * 20 + ' alter Drop PK ' + '#' * 20)
    print(j.alterDropPK('db101', 'T1DB1'))
    print(j.alterDropPK('db104', 'T1DB4'))
    print(j.alterDropPK('db107', 'T1DB7'))
    print(j.alterDropPK('db110', 'T1DB10'))
    print(j.alterDropPK('db113', 'T1DB13'))
    print(j.alterDropPK('db116', 'T1DB16'))
    print(j.alterDropPK('db119', 'T1DB19'))

    print()
    # def alterAddPK(database: str, table: str, columns: list) -> int:
    # {0: success, 1: error, 2: db not exist, 3: table not exist, 4: PK exist}
    print('#' * 20 + ' alter Add PK ' + '#' * 20)
    print(j.alterAddPK('db101', 'T1DB1', [0]))
    print(j.alterAddPK('db104', 'T1DB4', [0]))
    print(j.alterAddPK('db107', 'T1DB7', [0]))
    print(j.alterAddPK('db110', 'T1DB10', [0]))
    print(j.alterAddPK('db113', 'T1DB13', [0]))
    print(j.alterAddPK('db116', 'T1DB16', [0]))
    print(j.alterAddPK('db119', 'T1DB19', [0]))

    print()
    # def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    # {0: success, 1: error, 2: db not exist, 3:tableOld not exist, 4: tableNew exist}
    print(j.alterTable('db101', 'T1DB1', 'T1DB101'))
    print(j.alterTable('db104', 'T1DB4', 'T1DB104'))
    print(j.alterTable('db107', 'T1DB7', 'T1DB107'))
    print(j.alterTable('db110', 'T1DB10', 'T1DB110'))
    print(j.alterTable('db113', 'T1DB13', 'T1DB113'))
    print(j.alterTable('db116', 'T1DB16', 'T1DB116'))
    print(j.alterTable('db119', 'T1DB19', 'T1DB119'))

    print()
    # def showDatabases() -> list:
    # {[]: error, not tables, None: not db }
    print('#' * 20 + ' showTables ' + '#' * 20)
    print(j.showTables("db101"))
    print(j.showTables("db104"))
    print(j.showTables("db107"))
    print(j.showTables("db110"))
    print(j.showTables("db113"))
    print(j.showTables("db116"))
    print(j.showTables("db119"))

    print()
    print('#' * 20 + ' alter Add Column ' + '#' * 20)
    # def alterAddColumn(database: str, table: str, default: any) -> int:
    # {0: success, 1: error, 2: db not exist, 3: table not exist}
    print(j.alterAddColumn('db101', 'T1DB101', 'NuevaColumna101'))
    print(j.alterAddColumn('db104', 'T1DB104', 'NuevaColumna104'))
    print(j.alterAddColumn('db107', 'T1DB107', 'NuevaColumna107'))
    print(j.alterAddColumn('db110', 'T1DB110', 'NuevaColumna110'))
    print(j.alterAddColumn('db113', 'T1DB113', 'NuevaColumna113'))
    print(j.alterAddColumn('db116', 'T1DB116', 'NuevaColumna116'))
    print(j.alterAddColumn('db119', 'T1DB119', 'NuevaColumna119'))

    print()
    # def extractTable(database: str, table: str) -> list:
    # {[]: , []: not registers, None: error}
    print('#' * 20 + ' extract Table ' + '#' * 20)
    print(j.extractTable("db101", "T1DB101"))
    print(j.extractTable("db104", "T1DB104"))
    print(j.extractTable("db107", "T1DB107"))
    print(j.extractTable("db110", "T1DB110"))
    print(j.extractTable("db113", "T1DB113"))
    print(j.extractTable("db116", "T1DB116"))
    print(j.extractTable("db119", "T1DB119"))

# mode: 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'
final_test()
# test()
# testCompress()
