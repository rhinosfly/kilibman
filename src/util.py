'''utility functions'''

from pathlib import Path
from shutil import copy, copytree

def rmdir_recurse(path: Path):
    '''as it sounds'''
    children = path.iterdir()
    for child in children:
        remove_path(child)
    path.rmdir()
    
def remove_path(path: Path):
    '''as it sounds'''
    if not path.exists():
        return
    if not path.is_dir():
        path.unlink()
        return
    rmdir_recurse(path)


def copy_path(src: Path, dst: Path):
    '''copy a path (file or dir) from src to path'''
    assert(src.exists())
    if src.is_file():
        copy(src=src, dst=dst)
    elif src.is_dir():
        new_dst = dst / src.absolute().name
        copytree(src=src, dst=new_dst)
    else: #unreachable
        raise Exception("neither file nor dir")