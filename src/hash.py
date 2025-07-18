'''module dealing with hashing'''
from hashlib import sha256, file_digest
from _hashlib import HASH
from pathlib import Path
from base64 import b64encode


def hash_path(path: Path) -> str:
    assert(path.exists())
    hash = sha256()
    hash = update_hash_path(path, hash)
    value = b64encode(s=hash.digest(), altchars=b'-_').decode("utf-8")
    return value


def update_hash_path(path: Path, hash: HASH) -> HASH:
    '''get hash of file or directory'''
    # hash contents
    if path.is_dir():
        hash = update_hash_dir(path, hash)
    elif path.is_file():
        hash = update_hash_file(path, hash)
    else: #should be unreachable
        raise Exception("neither file nor dir?!")
    # has name
    file_name = str(path).encode("utf-8")
    hash.update(file_name)
    # return
    return hash


def update_hash_file(path: Path, hash: HASH) -> HASH:
    '''get hash of file contents'''
    with open(path, "rb") as file:
        hash = file_digest(file, lambda :hash)
    return hash


def update_hash_dir(path: Path, hash: HASH) -> HASH:
    '''get hash of directory'''
    for child in sorted(path.iterdir()):
        hash = update_hash_path(child, hash)
    return hash
