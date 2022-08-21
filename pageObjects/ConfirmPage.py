from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.ID, "country")
    country = (By.ID, "country")

    # driver.find_element(By.LINK_TEXT, "India")
    country_name = (By.LINK_TEXT, "India")

    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    country_check = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    country_btn = (By.XPATH, "//input[@type='submit']")
    # self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']")
    verify_success = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def GetCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def GetCountry_name(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    def GetCountry_check(self):
        return self.driver.find_element(*ConfirmPage.country_check)

    def GetCountry_btn(self):
        return self.driver.find_element(*ConfirmPage.country_btn)

    def GetVerify_success(self):
        return self.driver.find_element(*ConfirmPage.verify_success)


