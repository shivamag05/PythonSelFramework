from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver,product):
        self.driver = driver
        self.product = product


    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    card = (By.XPATH, "//div[@class='card h-100']")
    # find_element(By.XPATH, "div/h4/a")
    cardTitle = (By.XPATH, "div/h4/a")
    # find_element(By.XPATH, "div/button")
    cardButton = (By.XPATH, "div/button")
    # driver.find_element(By.XPATH, "(//li/a)[3]")
    cardcheckout0 = (By.XPATH, "(//li/a)[3]")
    # driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']")
    cardcheckout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def Getcards(self):
        return self.driver.find_elements(*CheckOutPage.card)

    def GetcardTitles(self):
        return self.product.find_element(*CheckOutPage.cardTitle)

    def GetcardButton(self):
        return self.product.find_element(*CheckOutPage.cardButton)

    def GetcardCheckout0(self):
        return self.driver.find_element(*CheckOutPage.cardcheckout0)

    def GetcardCheckout(self):
        self.driver.find_element(*CheckOutPage.cardcheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
