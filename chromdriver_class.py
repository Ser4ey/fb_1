import csv
import os
import pickle
import threading
import pyautogui
import selenium
from selenium import webdriver
import time
import data

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# selenium.webdriver.common.keys


class FireFoxDriver:
    def __init__(self, user_agent):

        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True

        profile = webdriver.FirefoxProfile('/home/ser4/.mozilla/firefox/8da9zz4w.default-release')

        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("general.useragent.override", user_agent)

        driver = webdriver.Firefox(
            executable_path=data.path_to_geckodriver,
            firefox_binary=data.firefox_binary,
            capabilities=firefox_capabilities,
            options=options,
            firefox_profile=profile)

        self.driver = driver
        self.is_login_in_positivebet = False



    def close_session(self):
        self.driver.close()
        self.driver.quit()




