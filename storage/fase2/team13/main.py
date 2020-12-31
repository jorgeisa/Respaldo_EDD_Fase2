# LIST WITH DIFFERENT MODES
databases = {}
modes = {}


# SHOW DICTIONARY
def show_Dict():
    print('-- DATABASES --')
    for key in databases:
        print(key, ":", databases[key])


def check_mode(mode):
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
    j = check_mode(mode)

    print(j.createDatabase(database))
    databases[database] = [mode, encoding]


# SHOW MODE
def showMode(mode):
    j = modes.get(mode)
    print(mode, j.showDatabases())


createDatabase('db1', 'avl', 'ascii')
createDatabase('db2', 'avl', 'utf8')
createDatabase('db3', 'bplus', 'ascii')
createDatabase('db4', 'json', 'utf8')
createDatabase('db5', 'json', 'utf8')
createDatabase('db1', 'b', 'utf8')


showMode('avl')
showMode('bplus')
showMode('json')
showMode('b')


# THESE MODES DON'T WORK
'''
createDatabase('db7', 'hash', 'ascii')
createDatabase('db5', 'dict', 'ascii')
createDatabase('db6', 'isam', 'utf8')
'''

