import unittest

from functions.get_file_content import get_file_content

class TestGetFilesInfo(unittest.TestCase):
    def test_root(self):
        result = get_file_content("calculator", "main.py")
        print("MAIN")
        print(result)
        print("\n")

    def test_pkg(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print("PKG")
        print(result)
        print("\n")
    
    def test_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        print("BIN")
        print(result)
        print("\n")


if __name__ == "__main__":
    unittest.main()