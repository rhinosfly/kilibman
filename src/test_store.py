'''test store module and class'''

import unittest
from pathlib import Path
from store import Store


class TestStore(unittest.TestCase):
    def test_store(self):
        STORE_PATH = Path("../target/test/")
        FILE_PATH = Path("./test_store.py")
        store = Store(STORE_PATH).init()
        store.store_file(file_path=FILE_PATH, name="testfile")