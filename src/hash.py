"""module dealing with hashing"""

from hashlib import sha256, file_digest
from _hashlib import HASH  # only for type annotations
from pathlib import Path
from base64 import b64encode


def hash_path(path: Path) -> str:
    """return b64 encoded hash of file system under path"""
    assert path.exists()
    # init
    hash = sha256()
    # get hash
    hash = update_hash_path(path, hash)
    # encode
    value = b64encode(s=hash.digest(), altchars=b"-_").decode("utf-8")
    # return
    return value


def update_hash_path(path: Path, hash: HASH) -> HASH:
    """update hash with file or directory"""
    # hash contents
    if path.is_dir():
        hash = update_hash_dir(path, hash)
    elif path.is_file():
        hash = update_hash_file(path, hash)
    else:  # should be unreachable
        raise Exception("neither file nor dir?!")
    # hash name
    file_name = str(path).encode("utf-8")
    hash.update(file_name)
    # return
    return hash


def update_hash_file(path: Path, hash: HASH) -> HASH:
    """update hash with file contents"""
    with open(path, "rb") as file:
        hash = file_digest(file, lambda: hash)
    return hash


def update_hash_dir(path: Path, hash: HASH) -> HASH:
    """update hash with directory contents"""
    for child in sorted(path.iterdir()):
        hash = update_hash_path(child, hash)
    return hash
