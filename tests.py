import unittest

from functions.write_file import write_file

class TestGetFilesInfo(unittest.TestCase):
    def test_root(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print("LOREM")
        print(result)
        print("\n")

    def test_pkg(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print("MORELOREM")
        print(result)
        print("\n")
    
    def test_bin(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print("ERROR")
        print(result)
        print("\n")


if __name__ == "__main__":
    unittest.main()