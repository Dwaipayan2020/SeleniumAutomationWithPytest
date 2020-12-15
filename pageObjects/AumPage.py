from selenium.webdriver.common.by import By


class AumPage:

    def __init__(self, driver):
        self.driver = driver
    #locators
    invescoLogo = (By.CSS_SELECTOR, "[title*='Invesco']")
    aboutCompanyText = (By.XPATH, "//div[@class='PaneContentInner']//p[3]")

    #Methods
    def getCompanyLogo(self):
        return self.driver.find_element(*AumPage.invescoLogo)

    def getAboutInvescoText(self):
        return self.driver.find_element(*AumPage.aboutCompanyText)



