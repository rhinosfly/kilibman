'''test store module and class'''

import unittest
from pathlib import Path
from store import Store

STORE_PATH = Path("../target/test/")
store = Store(STORE_PATH).init()

class TestStore(unittest.TestCase):
    def test_file_copy(self):
        FILE_PATH = Path("./test_store.py")
        store.store_file(file_path=FILE_PATH, name="testfile")
    def test_dir_copy(self):
        FILE_PATH = Path(".")
        store.store_file(file_path=FILE_PATH, name="src")