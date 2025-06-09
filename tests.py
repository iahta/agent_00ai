import unittest

from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_root(self):
        result = get_files_info("calculator", ".")
        print("ROOT")
        print(result)
        print("\n")

    def test_pkg(self):
        result = get_files_info("calculator", "pkg")
        print("PKG")
        print(result)
        print("\n")
    
    def test_bin(self):
        result = get_files_info("calculator", "/bin")
        print("BIN")
        print(result)
        print("\n")

    def test_error(self):
        result = get_files_info("calculator", "../")
        print("ERROR")
        print(result)
        print("\n")
    
    def test_file(self):
        result = get_files_info("calculator", "tests.py")
        print("FILE")
        print(result)
        print("\n")

if __name__ == "__main__":
    unittest.main()