from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Cosmo:
    def __init__(self):
        self.loginId = "mitunpokkisham@gmail.com"
        self.passCode = "LINKEDIN"
        self.cosmoBanner = """ """
        self.chromeDriver =  webdriver.Chrome(service= Service(ChromeDriverManager().install()))
        self.targetLink = "https://in.linkedin.com/"
    
    def getWindow(self):
        self.chromeDriver.get(self.targetLink)
        email_field = self.chromeDriver.find_element(
            By.ID,
            "session_key"
        )
        passcode_field = self.chromeDriver.find_element(
            By.ID,
            "session_password"
        )