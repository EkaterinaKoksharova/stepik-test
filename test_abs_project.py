from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        assert (abs(-42) == 42, "Should be absolute value of a number") 

if __name__ == "__main__":
    print("All tests passed!")
    unittest.main()