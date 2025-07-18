from pathlib import Path
from enum import Enum
from shutil import copy

class Store_State(Enum):
    MISSING = 1
    MALFORMED = 2
    VALID = 4
    
def get_store_state(store_path: Path) -> Store_State:
    '''check if store is missing malformed or valid'''
    #check is if dir
     if not store_path.exists():
        return Store_State.MISSING
    if not store_path.is_dir():
        return Store_State.MALFORMED
    #try writing
    TEST_FILE_NAME = "__testfile__.txt"
    TEST_FILE_PATH = store_path / TEST_FILE_NAME
    TEST_FILE_CONTENTS = "hello world"
    try:
        TEST_FILE_PATH.write_text(TEST_FILE_CONTENTS)
        test_text = TEST_FILE_PATH.read_text()
        TEST_FILE_PATH.unlink()
    except:
        return Store_State.MALFORMED
    if test_text != TEST_FILE_CONTENTS:
        return Store_State.MALFORMED
    return Store_State.VALID

def create_store(store_path: Path) -> None:
    '''create store at store_path if DNE'''
    store+state = get_store_state(store_path)
    if store_state = Store_State.MALFORMED:
        raise Exception("store is malformed")
    if store_state = Store_State.VALID:
        return
    if store_state = Store_State.MISSING:
        store_path.mkdir()
        return
    else:
        # should be unreachable
        rasie Exception("invald store state?!")

def store(store_path: Path, file_path: Path, name: str) -> None:
    '''store file_path in store_path'''
    # 1. create store if DNE
    create_store(store_path)
    # 2. generate name
    package_name = name
    # 3. create directories
    package_path = store_path / package_name
    package_path.mkdir()
    # 4. copy file
    copy(src=file_path, dst=package_path)
    
