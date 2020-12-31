
from fase2.team13.storage.b import b_mode as j

from fase2.team13.storage.dict import dict_mode as j
from fase2.team13.storage.hash import hash_mode as j
from fase2.team13.storage.isam import isam_mode as j
from fase2.team13.storage.json import json_mode as j


def createDatabase(database: str, mode: str, encoding: str) -> int:
    j = None
    if mode == "avl":
        from fase2.team13.storage.avl import avl_mode as j
    elif mode == "blplus":
        from fase2.team13.storage.bplus import bplus_mode as j
    j.createDatabase(database)
    return 1
