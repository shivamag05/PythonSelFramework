import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")  # to retrieve the command line value
    if browser_name == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    # firefox invocation Gecko driver
    #     elif browser_name == "firefox":
    #  IE driver

    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver  # driver which u declare here will be send to class(cls) object(driver)
# i.e. assigning local driver of this fixture to class driver (cls.driver), which of the class uses
# this fixture in that class if there is driver variable then this driver will go and assign to that.
