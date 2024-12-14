import pytest
from selenium.webdriver.common.by import By

from testscripts.BaseTest import BaseTest



class Test_Dependent(BaseTest):


    def test_sampletestcase1(self):
       print("This is  testcaase1")
       assert 10 == 10

    def test_sampletestcase2(self):
        print("This is  testcaase2")
        assert 10 == 10



