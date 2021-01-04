from Funciones import *


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

    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', [0]))      # 0
    print(alterTableAddFK('db63', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', [0]))     # 2
    print(alterTableAddFK('db6', 'Table2', 'Rel1', [0, 1], 'Table1_DB6', [0]))          # 3
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1', [0]))          # 3
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [], 'Table1_DB6', [0]))          # 4
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', []))       # 4
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel1', [0, 1], 'Table1_DB6', [0]))      # 6
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel2', [0, 1], 'Table1_DB6', [0]))      # 0
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel3', [0, 1], 'Table1_DB6', [0]))      # 0
    print(alterTableAddFK('db6', 'Table2_DB6', 'Rel4', [0, 1], 'Table1_DB6', [0]))      # 0
    showFK(load('FK'))

    print(alterTableDropFK('db63', 'Table2_DB6', 'Rel1'))       # 2
    print(alterTableDropFK('db6', 'Table4', 'Rel3'))            # 3
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel3'))        # 4
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel1'))        # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel2'))        # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel3'))        # 0
    print(alterTableDropFK('db6', 'Table2_DB6', 'Rel4'))        # 0

    showFK(load('FK'))


test()
