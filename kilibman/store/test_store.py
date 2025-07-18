"""test store module and class"""

from .store import Store
from pathlib import Path
import unittest


STORE_PATH = Path(".test/store")
store = Store(STORE_PATH).init()


class TestStore(unittest.TestCase):
    def test_file_copy(self):
        FILE_PATH = Path("__main__.py")
        store.store_file(file_path=FILE_PATH, name="main")

    def test_dir_copy(self):
        FILE_PATH = Path("store")
        store.store_file(file_path=FILE_PATH, name="store")
