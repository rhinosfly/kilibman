import unittest
from pathlib import Path
from main import *


class TestStore(unittest.TestCase):
    def test_store(self):
        STORE_PATH = Path("../target/test/")
        FILE_PATH = Path("./test_main.py")
        store(store_path=STORE_PATH, file_path=FILE_PATH, name="testfile")


if __name__ == "__main__":
    unittest.main()
