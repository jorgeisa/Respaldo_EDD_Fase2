# LIST WITH DIFFERENT MODES
databases = {}
modes = {}


# SHOW DICTIONARY
def showDict():
    print('-- DATABASES --')
    for key in databases:
        print(key, ":", databases[key])


# SHOW MODE
def showMode(mode):
    j = modes.get(mode)
    print(mode, j.showDatabases())


# CHECK MODE
def checkMode(mode):
    if mode == 'avl':
        print('mode_AVL')
        from storage.avl import avl_mode as j
        modes['avl'] = j
        return j

    elif mode == 'b':
        print('mode_b')
        from storage.b import b_mode as j
        modes['b'] = j
        return j

    elif mode == 'bplus':
        print('mode_bplus')
        from storage.bplus import bplus_mode as j
        modes['bplus'] = j
        return j

    elif mode == 'dict':
        print('mode_dict')
        from storage.dict import dict_mode as j
        modes['dict'] = j
        return j

    elif mode == 'isam':
        print('mode_isam')
        from storage.isam import isam_mode as j
        modes['isam'] = j
        return j

    elif mode == 'json':
        print('mode_json')
        from storage.json import json_mode as j
        modes['json'] = j
        return j

    elif mode == 'hash':
        print('mode_hash')
        from storage.hash import hash_mode as j
        modes['hash'] = j
        return j


# CREATE DATABASE
def createDatabase(database, mode, encoding):
    j = checkMode(mode)

    print(j.createDatabase(database))
    databases[database] = [mode, encoding]


# ALTER DATABASEMODE
def alterDatabaseMode(database, mode):
    print('alterDatabaseMode: ')
    j = modes.get(mode)
    actual_mode = modes.get(databases.get(database)[0])

    if databases.get(database):
        # UPDATING DICTIONARY MODE
        databases.get(database)[0] = mode
        # DELETING OLD MODE DATABASE
        actual_mode.dropDatabase(database)
        # CREATING NEW DATABASE
        j.createDatabase(database)
    else:
        print('DB no existe')


createDatabase('db1', 'avl', 'ascii')
createDatabase('db2', 'avl', 'utf8')
createDatabase('db6', 'b', 'utf8')
createDatabase('db3', 'bplus', 'ascii')
createDatabase('db8', 'dict', 'ascii')
createDatabase('db9', 'isam', 'utf8')
createDatabase('db4', 'json', 'utf8')
createDatabase('db5', 'json', 'utf8')
createDatabase('db7', 'hash', 'ascii')


#showDict()
showMode('bplus')
showMode('avl')
alterDatabaseMode('db1', 'bplus')
#showDict()
showMode('bplus')
showMode('avl')


'''
# SHOW MODES
showMode('avl')
showMode('b')
showMode('bplus')
showMode('dict')
showMode('isam')
showMode('json')
showMode('hash')

# SHOW DICT
showDict()
'''
