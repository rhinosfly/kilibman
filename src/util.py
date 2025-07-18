'''utility functions'''

from pathlib import Path

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
