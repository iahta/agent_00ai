import unittest

from functions.run_python import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    def test_root(self):
        result = run_python_file("calculator", "main.py")
        print("MAIN")
        print(result)
        print("\n")

    def test_pkg(self):
        result = run_python_file("calculator", "tests.py")
        print("TESTS")
        print(result)
        print("\n")
    
    def test_bin(self):
        result = run_python_file("calculator", "../main.py")
        print("ERROR")
        print(result)
        print("\n")

    def test_nonexistent(self):
        result = run_python_file("calculator", "nonexistent.py")
        print("NONEXISTENT")
        print(result)
        print("\n")

if __name__ == "__main__":
    unittest.main()