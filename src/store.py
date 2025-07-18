from pathlib import Path
from enum import Enum
from shutil import copy
from typing import Self

class Store:
    '''a location to store files to'''
    
    class State(Enum):
        MISSING = 1
        MALFORMED = 2
        VALID = 3
    
    def __init__(self, path: Path):
        self.path = Path(path)
        
    def get_state(self) -> State:
        store_path = self.path
        '''check if store is missing malformed or valid'''
        #check is if dir
        if not store_path.exists():
            return self.State.MISSING
        if not store_path.is_dir():
            return self.State.MALFORMED
        #try writing
        TEST_FILE_NAME = "__testfile__.txt"
        TEST_FILE_PATH = store_path / TEST_FILE_NAME
        TEST_FILE_CONTENTS = "hello world"
        try:
            TEST_FILE_PATH.write_text(TEST_FILE_CONTENTS)
            test_text = TEST_FILE_PATH.read_text()
            TEST_FILE_PATH.unlink()
        except:
            return self.State.MALFORMED
        if test_text != TEST_FILE_CONTENTS:
            return self.State.MALFORMED
        return self.State.VALID
    
    
    def init(self) -> Self:
        '''create store at store_path if DNE'''
        store_path = self.path
        store_state = self.get_state()
        if store_state == self.State.MALFORMED:
            raise Exception("store is malformed")
        if store_state == self.State.VALID:
            return self
        if store_state == self.State.MISSING:
            store_path.mkdir()
            return self
        else:
            # should be unreachable
            raise Exception("invald store state?!")
    
    def store_file(self, file_path: Path, name: str) -> None:
        '''store file_path in store_path'''
        store_path = self.path
        # 1. create store if DNE
        # not needed, just call init first
        #create_store(store_path)
        # 2. generate name
        # hash later
        package_name = name
        # 3. create directories
        package_path = store_path / package_name
        package_path.mkdir()
        # 4. copy file
        copy(src=file_path, dst=package_path)
