from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    activeDayIcon = (By.CSS_SELECTOR, "div.item.blue_active")
    airwaysNameList = (By.CSS_SELECTOR, "div.dept-options-section.clearfix  span.airways-name")
    fliCodeList = (By.CSS_SELECTOR, "div.pull-left.airways-info-sect p.fli-code")


    # Method Names:
    def getAirwaysNameList(self):
        return self.driver.find_elements(*SearchResultsPage.airwaysNameList)

    def getFliCodeList(self):
        return self.driver.find_elements(*SearchResultsPage.fliCodeList)

    def getActiveDayIcon(self):
        return self.driver.find_element(*SearchResultsPage.activeDayIcon)
