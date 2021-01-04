import os
import pickle
import shutil


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
        save(databases,  'metadata')
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


# ---------------------------------------------- AUXILIARY FUNCTIONS  --------------------------------------------------
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


# ------------------------------------------------------ FASE 1 --------------------------------------------------------
def createTable(database, table, numberColumns):
    dictionary = load('metadata')
    try:
        dict_tables = dictionary.get(database)[2]
        dict_tables[table] = [numberColumns]
        save(dictionary, 'metadata')

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.createTable(database, table, numberColumns)
        return value_return
    except:
        return 2  # database doesn't exist


def insert(database, table, register):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.insert(database, table, register)
        return value_return
    except:
        return 2  # database doesn't exist

def loadCSV(file, database, table):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.loadCSV(file, database, table)
        return value_return
    except:
        return []

def insert(database, table, register):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.insert(database, table, register)
        return value_return
    except:
        return 2  # database doesn't exist

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

def showTables(database):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.showTables(database)
        return value_return
    except:
        return 2  # database doesn't exist


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
