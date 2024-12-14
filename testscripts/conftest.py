import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def demo():
    print("this code executes only once and at the time of starting the session")
    yield
    print("this code executes only once and at the time of end the session")


@pytest.fixture(scope="function",autouse=True)
def setup_and_teardown(request):
    print("this code excutes before the function")

    yield
    print("this code excutes after the function")