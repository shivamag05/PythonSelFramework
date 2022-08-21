import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, GetData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("firstname is" + GetData["firstname"])
        homePage.GetName().send_keys(GetData["firstname"])
        homePage.GetEmail().send_keys(GetData["lastname"])
        # homePage.GetPaswd().send_keys("12345")
        homePage.GetCheck().click()
        self.selectOptionByText(homePage.GetGender(), GetData["gender"])
        # dropdown = Select(homePage.GetGender())
        # dropdown.select_by_visible_text("Male")

        homePage.GetRadio().click()
        homePage.GetSubmit().click()
        message = homePage.GetSucesMessage().text

        # driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        # driver.find_element(By.ID, "exampleCheck1").click()
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("shivam agarwal")
        # driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_value()
        # driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
        # message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message
        self.driver.refresh()

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("shivam agarwal")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def GetData(self, request):
        return request.param
