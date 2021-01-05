import os
import pickle
import shutil
import zlib

databases = {}  # LIST WITH DIFFERENT MODES
dict_encoding = {'ascii': 1, 'iso-8859-1': 2, 'utf8': 3}
dict_modes = {'avl': 1, 'b': 2, 'bplus': 3, 'dict': 4, 'isam': 5, 'json': 6, 'hash': 7}


# ---------------------------------------------------- FASE 2  ---------------------------------------------------------
# CREATE DATABASE
def createDatabase(database, mode, encoding):
    if dict_modes.get(mode) is None:
        return 3  # mode incorrect
    elif dict_encoding.get(encoding) is None:
        return 4  # encoding incorrect
    elif os.path.isfile(os.getcwd() + "\\Data\\metadata.bin"):
        dictionary = load('metadata')
        value_db = dictionary.get(database)

        if value_db:
            return 2  # Exist db
        else:
            j = checkMode(mode)
            value_return = j.createDatabase(database)
            if value_return == 1:
                return 1

            dictionary[database] = [mode, encoding, {}]
            save(dictionary, 'metadata')
            return 0
    else:
        j = checkMode(mode)
        value_return = j.createDatabase(database)
        if value_return == 1:
            return 1

        databases[database] = [mode, encoding, {}]
        save(databases, 'metadata')
        return 0


# ALTER DATABASEMODE
def alterDatabaseMode(database, mode):
    try:
        dictionary = load('metadata')
        value_db = dictionary.get(database)
        actual_mode = dictionary.get(database)[0]
        encoding = dictionary.get(database)[1]
        dict_tables = dictionary.get(database)[2]

        if value_db is None:
            return 2  # database doesn't exist
        elif dict_modes.get(mode) is None:
            return 4  # mode incorrect

        insertAgain(database, actual_mode, mode)
        dictionary.pop(database)
        dictionary[database] = [mode, encoding, dict_tables]
        save(dictionary, 'metadata')
        return 0
    except:
        return 1

# ALTER FOREIGN KEY
def alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef):
    try:
        if os.path.isfile(os.getcwd() + "\\Data\\FK.bin"):
            FK = load('FK')
        else:
            FK = {}
        db = load('metadata')
        if db.get(database) is not None:
            j = checkMode(db[database][0])
            tables = j.showTables(database)
            if (table in tables) and (tableRef in tables):
                if len(columns) != 0 and len(columnsRef) != 0:
                    if FK.get(indexName) is not None:
                        return 6
                    FK.update({indexName: [database, indexName, table, columns, tableRef, columnsRef]})
                    save(FK, 'FK')
                    return 0
                return 4
            return 3
        return 2
    except:
        return 1


# DROP FOREIGN KEY
def alterTableDropFK(database, table, indexName):
    try:
        if os.path.isfile(os.getcwd() + "\\Data\\FK.bin"):
            FK = load('FK')
            db = load('metadata')
            if db.get(database) is not None:
                j = checkMode(db[database][0])
                tables = j.showTables(database)
                if table in tables:
                    if FK.get(indexName) is not None:
                        FK.pop(indexName)
                        save(FK, 'FK')
                        return 0
                    return 4
                return 3
            return 2
        else:
            FK = {}
            save(FK, 'FK')
    except:
        return 1


# Compress Data
def alterTableCompress(database, table, level):
    try:
        newTable = []

        dictionary = load('metadata')
        value_db = dictionary.get(database)
        mode = dictionary.get(database)[0]

        if value_db:
            j = checkMode(mode)
            tableEx = j.extractTable(database, table)
            for tuple in tableEx:
                newTuple = []
                for register in tuple:
                    if isinstance(register, str):
                        # print("Tamaño sin comprimir %d" % len(register))
                        compressed = zlib.compress(register.encode(), level)
                        # print("Tamaño comprimido %d" % len(compressed))
                        newTuple.append(compressed)
                    else:
                        newTuple.append(register)

                newTable.append(newTuple)

            j.truncate(database, table)

            for tuple in newTable:
                j.insert(database, table, tuple)

            save(dictionary, 'metadata')
            return 0
            #print(newTable)

        else:
            return 2
    except:
        return 1

def alterTableDecompress(database, table):
    try:
        newTable = []

        os.path.isfile(os.getcwd() + "\\Data\\metadata.bin")
        dictionary = load('metadata')
        value_db = dictionary.get(database)
        mode = dictionary.get(database)[0]

        if value_db:
            j = checkMode(mode)
            tableEx = j.extractTable(database, table)
            for tuple in tableEx:
                newTuple = []
                for register in tuple:
                    if iscompressed(register):
                        # print("Tamaño sin comprimir %d" % len(register))
                        decompressed = zlib.decompress(register)
                        # print("Tamaño comprimido %d" % len(compressed))
                        newTuple.append(decompressed.decode("utf-8"))
                    else:
                        newTuple.append(register)

                newTable.append(newTuple)

            j.truncate(database, table)

            for tuple in newTable:
                j.insert(database, table, tuple)

            save(dictionary, 'metadata')
            return 0
            # print(newTable)

        else:
            return 2
    except:
        return 1

# ---------------------------------------------- AUXILIARY FUNCTIONS  --------------------------------------------------
#if is compressed
def iscompressed(data):
    result = True
    try:
        s = zlib.decompress(data)
    except:
        result = False
    return result

# SHOW DICTIONARY FK
def showFK(dictionary):
    print('--FOREIGN KEYS--')
    for key in dictionary:
        print(key, ':', dictionary[key])

# SHOW DICTIONARY
def showDict(dictionary):
    print('-- DATABASES --')
    for key in dictionary:
        print(key, ":", dictionary[key])


# SHOW MODE
def showMode(mode):
    j = checkMode(mode)
    print(mode, j.showDatabases())


# CHECK MODE
def checkMode(mode):
    if mode == 'avl':
        from storage.avl import avl_mode as j
        return j

    elif mode == 'b':
        from storage.b import b_mode as j
        return j

    elif mode == 'bplus':
        from storage.bplus import bplus_mode as j
        return j

    elif mode == 'dict':
        from storage.dict import dict_mode as j
        return j

    elif mode == 'isam':
        from storage.isam import isam_mode as j
        return j

    elif mode == 'json':
        from storage.json import json_mode as j
        return j

    elif mode == 'hash':
        from storage.hash import hash_mode as j
        return j


def insertAgain(database, mode, newMode):
    old_mode = checkMode(mode)
    new_mode = checkMode(newMode)
    new_mode.createDatabase(database)
    tables = old_mode.showTables(database)

    dictionary = load('metadata')
    dict_tables = dictionary.get(database)[2]

    if tables:
        for name_table in tables:
            register = old_mode.extractTable(database, name_table)  # [['A', '1'], ['B', '2'],  ['C', '3']]
            number_columns = dict_tables.get(name_table)[0]
            new_mode.createTable(database, name_table, number_columns)

            if register:  # There are registers
                for list_register in old_mode.extractTable(database, name_table):
                    new_mode.insert(database, name_table, list_register)

        old_mode.dropDatabase(database)

        
def grapList(list_):
    string = 'digraph G{\n'
    string += 'node[shape = \"record\"]\n'

    for i in range(0, len(list_)):
        string += f'node{hash(list_[i])*hash(list_[i])} [ label = "{list_[i]}"]\n'
        if i == len(list_)-1:
            pass
        else:
            string += f'node{hash(list_[i])*hash(list_[i])} -> node{hash(list_[i+1])*hash(list_[i+1])}\n'

    string += '}'
    file = open("List.circo", "w")
    file.write(string)
    file.close()
    os.system("circo -Tpng List.circo -o List.png")        

# ------------------------------------------------------ FASE 1 --------------------------------------------------------
# -------------------------------------------------- Data Base CRUD ----------------------------------------------------

# createDatabase was modified in this fase

def showDatabases(database):
    try:
        dictionary = load('metadata')
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.showDatabases()
        return value_return
    except:
        return []


def alterDatabase(databaseOld, databaseNew):
    try:
        dictionary = load('metadata')
        value_dbO = dictionary.get(str(databaseOld))
        value_dbN = dictionary.get(str(databaseNew))
        if not value_dbO:
            return 2
        if value_dbN:
            return 3
        mode = dictionary.get(str(databaseOld))[0]
        j = checkMode(mode)
        value_return = j.alterDatabase(databaseOld, databaseNew)
        if value_return == 0:
            info = dictionary[str(databaseOld)]
            dictionary.pop(str(databaseOld))
            dictionary[str(databaseNew)] = info
            save(dictionary, 'metadata')
        return value_return
    except:
        return 1


def dropDatabase(database):
    try:
        nombreBase = str(database)
        dictionary = load('metadata')
        value_base = dictionary.get(nombreBase)
        if value_base:
            mode = dictionary.get(nombreBase)[0]
            j = checkMode(mode)
            j.dropDatabase(nombreBase)
            dictionary.pop(nombreBase)
            save(dictionary, 'metadata')
        return 2
    except:
        return 1


# -------------------------------------------------- Table CRUD --------------------------------------------------------

def createTable(database, table, numberColumns):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.createTable(database, table, numberColumns)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            dict_tables[table] = [numberColumns, False]
            save(dictionary, 'metadata')

        return value_return
    except:
        return 1


def showTables(database):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return None  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.showTables(database)
        return value_return
    except:
        return 1


def extractTable(database, table):
    try:
        database = str(database)
        table = str(table)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return None
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.extractTable(database, table)
        return value_return
    except:
        return None


def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        database = str(database)
        table = str(table)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return None
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.extractRangeTable(database, table, int(columnNumber), lower, upper)
        return value_return
    except:
        return None


def alterAddPK(database, table, columns):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterAddPK(database, table, columns)
        return value_return
    except:
        return 1


def alterDropPK(database, table):
    try:
        dictionary = load('metadata')

        value_base = dictionary.get(database)
        if not value_base:
            return 2

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterDropPK(database, table)
        return value_return
    except:
        return 2


def alterTable(database, tableOld, tableNew):
    try:
        database = str(database)
        tableOld = str(tableOld)
        tableNew = str(tableNew)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return 2
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterTable(database, tableOld, tableNew)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            infoTabla = dict_tables[tableOld]
            dict_tables.pop(tableOld)
            dict_tables[tableNew] = infoTabla
            save(dictionary, 'metadata')
        return value_return
    except:
        return 1


def alterAddColumn(database, table, default):
    try:
        database = str(database)
        table = str(table)
        dictionary = load('metadata')

        value_base = dictionary.get(database)
        if not value_base:
            return 2

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterDropColumn(database, table, default)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            number_columns = dict_tables.get(table)[0]
            dict_tables.get(table)[0] = number_columns + 1
            save(dictionary, 'metadata')

        return value_return
    except:
        return 1


def alterDropColumn(database, table, columnNumber):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterDropColumn(database, table, columnNumber)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            number_columns = dict_tables.get(table)[0]
            dict_tables.get(table)[0] = number_columns-1  # Updating number of columns

            save(dictionary, 'metadata')

        return value_return
    except:
        return 1


def dropTable(database, table) :
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.dropTable(database, table)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            dict_tables.pop(table)

            save(dictionary, 'metadata')
    except:
        return 1


# -------------------------------------------------- Tuples CRUD -------------------------------------------------------

def insert(database, table, register):    
    try:
        dictionary = load('metadata')
        
        if dictionary.get(database) is None:
            return 2  # database doesn't exist
        
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.insert(database, table, register)
        return value_return
    except:
        return 1


def loadCSV(file, database, table):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.loadCSV(file, database, table)
        return value_return
    except:
        return []


def extractRow(database, table, columns):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.extractRow(database, table, columns)
        return value_return
    except:
        return []


def update(database, table, register, columns):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.update(database, table, register, columns)
        return value_return
    except:
        return 1


def delete(database, table, columns):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.delete(database, table, columns)
        return value_return
    except:
        return 1


def truncate(database, table):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.truncate(database, table)
    except:
        return 1


# ------------------------------------------------------- FILES --------------------------------------------------------
def save(objeto, nombre):
    file = open(nombre + ".bin", "wb")
    file.write(pickle.dumps(objeto))
    file.close()
    if os.path.isfile(os.getcwd() + "\\Data\\" + nombre + ".bin"):
        os.remove(os.getcwd() + "\\Data\\" + nombre + ".bin")
    shutil.move(os.getcwd() + "\\" + nombre + ".bin", os.getcwd() + "\\Data")


def load(nombre):
    file = open(os.getcwd() + "\\Data\\" + nombre + ".bin", "rb")
    objeto = file.read()
    file.close()
    return pickle.loads(objeto)
