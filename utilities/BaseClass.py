import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # loggerName gives the name from which getLogger method being called
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")  # in which format to print
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # pass object of class filehandler as an argument in addHandler method,
        # addHandler()
        # - in what file below logs have to be printed, filehandler - is file location comes from parent i.e.logging
        logger.setLevel(logging.DEBUG)
        return logger

    def VerifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)


