from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
from utilities.BaseClass import BaseClass


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.ID, "exampleFormControlSelect1")
    # driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")
    # driver.find_element(By.CLASS_NAME, "alert-success")
    # driver.find_element(By.XPATH, "//input[@type = 'submit']")

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.NAME, "email")
    paswd = (By.ID, "exampleInputPassword1")
    name = (By.CSS_SELECTOR, "input[name='name']")
    checkbox = (By.ID, "exampleCheck1")
    drop_down = (By.ID, "exampleFormControlSelect1")
    radio_btn = (By.CSS_SELECTOR, "#inlineRadio1")
    sumbit_btn = (By.XPATH, "//input[@type = 'submit']")
    suc_message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def GetName(self):
        return self.driver.find_element(*HomePage.name)

    def GetEmail(self):
        return self.driver.find_element(*HomePage.email)

    def GetPaswd(self):
        return self.driver.find_element(*HomePage.paswd)

    def GetCheck(self):
        return self.driver.find_element(*HomePage.checkbox)

    def GetGender(self):
        return self.driver.find_element(*HomePage.drop_down)

    def GetRadio(self):
        return self.driver.find_element(*HomePage.radio_btn)

    def GetSucesMessage(self):
        return self.driver.find_element(*HomePage.suc_message)

    def GetSubmit(self):
        return self.driver.find_element(*HomePage.sumbit_btn)


    # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")