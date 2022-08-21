import pytest

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all the card titles")
        # //a[contains(@href,'shop')] XPATH
        # a[href*='shop']   CSS
        products = checkoutPage.Getcards()
        # products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for self.product in products:

            # self.productName = self.product.find_element(By.XPATH, "div/h4/a").text
            self.productName = checkoutPage.GetcardTitles().text

            if self.productName == "Blackberry":
                # self.product.find_element(By.XPATH, "div/button").click()
                checkoutPage.GetcardButton().click()
        checkoutPage.GetcardCheckout0().click()
        confirmPage = checkoutPage.GetcardCheckout()
        log.info("Entering country name as ind")
        # driver.find_element(By.ID, "country").send_keys("ind")
        confirmPage.GetCountry().send_keys("ind")

        self.VerifyLinkPresence("india")
        # driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.GetCountry_name().click()
        # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.GetCountry_check().click()
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmPage.GetCountry_btn().click()
        # assert "Success!" in self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        assert "Success!" in confirmPage.GetVerify_success().text
        log.info("The text received from application is" + confirmPage.GetVerify_success().text)
        self.driver.close()
