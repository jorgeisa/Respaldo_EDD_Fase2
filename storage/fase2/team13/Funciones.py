import os
import pickle
import shutil


databases = {}  # LIST WITH DIFFERENT MODES
dict_encoding = {'ascii': 1, 'iso-8859-1': 2, 'utf8': 3}
dict_modes = {'avl': 1, 'b': 2, 'bplus': 3, 'dict': 4, 'isam': 5, 'json': 6, 'hash': 7}


# SHOW DICTIONARY
def showDict():
    print('-- DATABASES --')
    for key in databases:
        print(key, ":", databases[key])


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


# CREATE DATABASE
def createDatabase(database, mode, encoding):
    if dict_modes.get(mode) is None:
        return 3
    if dict_encoding.get(encoding) is None:
        return 4
    else:
        j = checkMode(mode)
        j.createDatabase(database)
        databases[database] = [mode, encoding]
        save(databases,  'metadata')
        return 0


# ALTER DATABASEMODE
def alterDatabaseMode(database, mode):
    dict_databases = load('metadata')
    actual_mode = dict_databases.get(database)[0]

    if dict_modes.get(mode) is None:
        return 4

    insertAgain(database, actual_mode, mode)


def insertAgain(database, mode, newMode):
    j = checkMode(mode)
    new_mode = checkMode(newMode)
    tables = j.showTables(database)
    size = len(j.extractTable(database, tables[0]))

    for name_table in tables:
        new_mode.createDatabase(database)
        new_mode.createTable(database, name_table, size)

        for list_register in j.extractTable(database, name_table):
            new_mode.insert(database, name_table, list_register)

    j.dropDatabase(database)


# ------------------------------------------------------ FASE 1 --------------------------------------------------------
def createTable(database, table, numberColumns, mode):
    j = checkMode(mode)
    j.createTable(database, table, numberColumns)


def insert(database, table, register, mode):
    j = checkMode(mode)
    j.insert(database, table, register)


def showTables(mode, database):
    j = checkMode(mode)
    print(mode, j.showTables(database))


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