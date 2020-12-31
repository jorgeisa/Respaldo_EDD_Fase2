# LIST WITH DIFFERENT MODES
databases = {}


def check_mode(mode):
    if mode == 'avl':
        print('mode_AVL')
        from storage.avl import avl_mode as j
        return j

    elif mode == 'b':
        print('mode_b')
        from storage.b import b_mode as j
        return j

    elif mode == 'bplus':
        print('mode_bplus')
        from storage.bplus import bplus_mode as j
        return j

    elif mode == 'dict':
        print('mode_dict')
        from storage.dict import dict_mode as j
        return j

    elif mode == 'isam':
        print('mode_isam')
        from storage.isam import isam_mode as j
        return j

    elif mode == 'json':
        print('mode_json')
        from storage.json import json_mode as j
        return j

    elif mode == 'hash':
        print('mode_hash')
        from storage.hash import hash_mode as j
        return j


# CREATE DATABASE
def createDatabase(database, mode, encoding):
    j = check_mode(mode)

    print(j.createDatabase('database_encoding'))
    databases[database] = [mode, encoding]

'''
createDatabase('db1', 'avl', 'ascii')
createDatabase('db2', 'b', 'utf8')
createDatabase('db3', 'bplus', 'ascii')
createDatabase('db4', 'json', 'utf8')'''

createDatabase('db7', 'hash', 'ascii')
createDatabase('db5', 'dict', 'ascii')
createDatabase('db6', 'isam', 'utf8')

print(databases)