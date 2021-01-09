from Funciones import *


def test():
    print('--DATABASES--')
    print(createDatabase('db1', 'isam', 'utf8'))
    print(createDatabase('db2', 'isam', 'utf8'))
    print(createDatabase('db3', 'isam', 'utf8'))
    print(createDatabase('db4', 'isam', 'utf8'))
    print(createDatabase('db5', 'isam', 'utf8'))

    print()
    print()

    print('--SHOW DATABASES--')
    print(showDict(load('metadata')))

    print()
    print()

    print('--TABLES--')
    print(createTable('db1', 'Table1', 3))
    print(createTable('db1', 'Table2', 3))
    print(createTable('db1', 'Table3', 3))

    print(createTable('db2', 'Table1', 3))
    print(createTable('db2', 'Table2', 3))
    print(createTable('db2', 'Table3', 3))

    print(createTable('db3', 'Table1', 3))
    print(createTable('db3', 'Table2', 3))
    print(createTable('db3', 'Table3', 3))

    print(createTable('db4', 'Table1', 3))
    print(createTable('db4', 'Table2', 3))
    print(createTable('db4', 'Table3', 3))

    print(createTable('db5', 'Table1', 3))
    print(createTable('db5', 'Table2', 3))
    print(createTable('db5', 'Table3', 3))

    print()
    print()

    print('--SHOW TABLES--')
    print(showTables('db1'))
    print('----------------------')
    print(showTables('db2'))
    print('----------------------')
    print(showTables('db3'))
    print('----------------------')
    print(showTables('db4'))
    print('----------------------')
    print(showTables('db5'))

    print()
    print()

    print('--PK\'S--')
    print(alterAddPK('db1', 'Table1', [0]))
    print(alterAddPK('db1', 'Table2', [1]))
    print(alterAddPK('db1', 'Table3', [2]))

    print(alterAddPK('db2', 'Table1', [0]))
    print(alterAddPK('db2', 'Table2', [1]))
    print(alterAddPK('db2', 'Table3', [2]))

    print(alterAddPK('db3', 'Table1', [0]))
    print(alterAddPK('db3', 'Table2', [1]))
    print(alterAddPK('db3', 'Table3', [2]))

    print(alterAddPK('db4', 'Table1', [0]))
    print(alterAddPK('db4', 'Table2', [1]))
    print(alterAddPK('db4', 'Table3', [2]))

    print(alterAddPK('db5', 'Table1', [0]))
    print(alterAddPK('db5', 'Table2', [1]))
    print(alterAddPK('db5', 'Table3', [2]))

    print()
    print()

    print('--INSERTS--')
    print(insert('db1', 'Table1', ['A1', 'B1', 'C1']))
    print(insert('db1', 'Table1', ['A2', 'B2', 'C2']))
    print(insert('db1', 'Table1', ['A3', 'B3', 'C3']))
    print(extractTable('db1', 'Table1'))

    print('--------------------------------------')

    print(insert('db1', 'Table2', ['A1', 'B1', 'C1']))
    print(insert('db1', 'Table2', ['A2', 'B2', 'C2']))
    print(insert('db1', 'Table2', ['A3', 'B3', 'C3']))
    print(extractTable('db1', 'Table2'))

    print('--------------------------------------')

    print(insert('db1', 'Table3', ['A1', 'B1', 'C1']))
    print(insert('db1', 'Table3', ['A2', 'B2', 'C2']))
    print(insert('db1', 'Table3', ['A3', 'B3', 'C3']))
    print(extractTable('db1', 'Table3'))

    print('--------------------------------------')

    print(insert('db2', 'Table1', ['A1', 'B1', 'C1']))
    print(insert('db2', 'Table1', ['A2', 'B2', 'C2']))
    print(insert('db2', 'Table1', ['A3', 'B3', 'C3']))
    print(extractTable('db2', 'Table1'))

    print('--------------------------------------')

    print(insert('db2', 'Table2', ['A1', 'B1', 'C1']))
    print(insert('db2', 'Table2', ['A2', 'B2', 'C2']))
    print(insert('db2', 'Table2', ['A3', 'B3', 'C3']))
    print(extractTable('db2', 'Table2'))

    print('--------------------------------------')

    print(insert('db2', 'Table3', ['A1', 'B1', 'C1']))
    print(insert('db2', 'Table3', ['A2', 'B2', 'C2']))
    print(insert('db2', 'Table3', ['A3', 'B3', 'C3']))
    print(extractTable('db2', 'Table3'))

    print('--------------------------------------')

    print(insert('db3', 'Table1', ['A1', 'B1', 'C1']))
    print(insert('db3', 'Table1', ['A2', 'B2', 'C2']))
    print(insert('db3', 'Table1', ['A3', 'B3', 'C3']))
    print(extractTable('db3', 'Table1'))

    print('--------------------------------------')

    print(insert('db3', 'Table2', ['A1', 'B1', 'C1']))
    print(insert('db3', 'Table2', ['A2', 'B2', 'C2']))
    print(insert('db3', 'Table2', ['A3', 'B3', 'C3']))
    print(extractTable('db3', 'Table2'))

    print('--------------------------------------')

    print(insert('db3', 'Table3', ['A1', 'B1', 'C1']))
    print(insert('db3', 'Table3', ['A2', 'B2', 'C2']))
    print(insert('db3', 'Table3', ['A3', 'B3', 'C3']))
    print(extractTable('db3', 'Table3'))

    print('--------------------------------------')

    print(insert('db4', 'Table1', ['A1', 'B1', 'C1']))
    print(insert('db4', 'Table1', ['A2', 'B2', 'C2']))
    print(insert('db4', 'Table1', ['A3', 'B3', 'C3']))
    print(extractTable('db4', 'Table1'))

    print('--------------------------------------')

    print(insert('db4', 'Table2', ['A1', 'B1', 'C1']))
    print(insert('db4', 'Table2', ['A2', 'B2', 'C2']))
    print(insert('db4', 'Table2', ['A3', 'B3', 'C3']))
    print(extractTable('db4', 'Table2'))

    print('--------------------------------------')

    print(insert('db4', 'Table3', ['A1', 'B1', 'C1']))
    print(insert('db4', 'Table3', ['A2', 'B2', 'C2']))
    print(insert('db4', 'Table3', ['A3', 'B3', 'C3']))
    print(extractTable('db4', 'Table3'))

    print('--------------------------------------')

    print(insert('db5', 'Table1', ['A1', 'B1', 'C1']))
    print(insert('db5', 'Table1', ['A2', 'B2', 'C2']))
    print(insert('db5', 'Table1', ['A3', 'B3', 'C3']))
    print(extractTable('db5', 'Table1'))

    print('--------------------------------------')

    print(insert('db5', 'Table2', ['A1', 'B1', 'C1']))
    print(insert('db5', 'Table2', ['A2', 'B2', 'C2']))
    print(insert('db5', 'Table2', ['A3', 'B3', 'C3']))
    print(extractTable('db5', 'Table2'))

    print('--------------------------------------')

    print(insert('db5', 'Table3', ['A1', 'B1', 'C1']))
    print(insert('db5', 'Table3', ['A2', 'B2', 'C2']))
    print(insert('db5', 'Table3', ['A3', 'B3', 'C3']))
    print(extractTable('db5', 'Table3'))

    print()
    print()

    print('--ALTER DATABASE--')
    print(alterDatabase('db1', 'db1_Update'))
    print()
    print('--SHOW DATABASES--')
    print(showDict(load('metadata')))
    print()

    print('--EXTRACT TABLE--')
    print(extractTable('db1_Update', 'Table1'))
    print(extractTable('db1_Update', 'Table2'))
    print(extractTable('db1_Update', 'Table3'))
    print('----------------------------------')
    print(extractTable('db2', 'Table1'))
    print(extractTable('db2', 'Table2'))
    print(extractTable('db2', 'Table3'))
    print('----------------------------------')
    print(extractTable('db3', 'Table1'))
    print(extractTable('db3', 'Table2'))
    print(extractTable('db3', 'Table3'))
    print('----------------------------------')
    print(extractTable('db4', 'Table1'))
    print(extractTable('db4', 'Table2'))
    print(extractTable('db4', 'Table3'))
    print('----------------------------------')
    print(extractTable('db5', 'Table1'))
    print(extractTable('db5', 'Table2'))
    print(extractTable('db5', 'Table3'))

    print()
    print()

    print('--DROP PK--')
    print(alterDropPK('db2', 'Table3'))

    print()
    print()

    print('--ALTER TABLE--')
    print(alterTable('db3', 'Table1', 'Tabl1_Update'))
    print()
    print('--SHOW TABLES--')
    print(showTables('db3'))

    print()
    print()

    print('--ALTER ADD COLUMN--')
    print(alterAddColumn('db4', 'Table1', 0))
    print()
    print('--EXTRACT TABLE--')
    print(extractTable('db4', 'Table1'))

    print()
    print()

    print('--ALTER DROP COLUMN--')
    print(alterDropColumn('db4', 'Table2', 2))
    print()
    print('--EXTRACT TABLE--')
    print(extractTable('db4', 'Table2'))

    print()
    print()

    print('--DROP TABLE--')
    print(dropTable('db5', 'Table3'))
    print()
    print('--SHOW TABLES--')
    print(showTables('db5'))

    print()
    print()

    print('--EXTRACT ROW--')
    print(extractRow('db1', 'Table3', ['C3']))

    print()
    print()

    print('--UPDATE--')
    print(update('db5', 'Table2', {0: 'A2_Update', 2: 'C2_Update'}, ['B2']))
    print()
    print('--EXTRACT TABLE--')
    print(extractTable('db5', 'Table2'))

    print()
    print()

    print('--DELETE--')
    print(delete('db4', 'Table1', 'A3'))
    print()
    print('--EXTRACT TABLE--')
    print(extractTable('db4', 'Table1'))

    print()
    print()

    print('--TRUNCATE--')
    print(truncate('db5', 'Table3'))
    print()
    print('--EXTRACT TABLE--')
    print(extractTable('db5', 'Table3'))


test()
