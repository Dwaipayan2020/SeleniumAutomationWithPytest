from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    flightButton = (
    By.CSS_SELECTOR, "a.active.makeFlex.hrtlCenter.column span.chNavIcon.appendBottom2.chSprite.chFlights.active")
    travelCategories = (By.XPATH, "//ul[@class='fswTabs latoBlack greyText']/li/span")
    travelFrom = (By.CSS_SELECTOR, "div.fsw_inputBox.searchCity.inactiveWidget input#fromCity")
    textboxFrom = (By.XPATH, "//input[@placeholder='From']")
    errorMessage = (By.CSS_SELECTOR, "span.redText.errorMsgText")
    travelTo = (By.XPATH, "//span[contains(text(),'To')]")
    textboxTo = (By.XPATH, "//input[contains(@placeholder,'To')]")
    cityList = (By.CSS_SELECTOR, "div.calc60 p.font14.appendBottom5.blackText")
    # destCityList = (By.CSS_SELECTOR, "#react-autowhatever-1 ul.react-autosuggest__suggestions-list p.font14.appendBottom5.blackText")
    departureDateButton = (By.CSS_SELECTOR, "div.fsw_inputBox.dates.inactiveWidget label[for='departure']")
    monthList = (By.XPATH, "//div[@class='DayPicker-Caption']/div")
    travellersClass = (By.XPATH, "//span[contains(text(),'Travellers & CLASS')]")
    adultsCount = (By.CSS_SELECTOR, "div.appendBottom20 ul.guestCounter.font12.darkText li[data-cy*='adults']")
    childrenCount = (By.CSS_SELECTOR, "div.appendBottom20 ul.guestCounter.font12.darkText li[data-cy*='children']")
    infantsCount = (By.CSS_SELECTOR, "div.appendBottom20 ul.guestCounter.font12.darkText li[data-cy*='infants']")
    journeyClassList = (By.CSS_SELECTOR, "div.appendBottom20 ul.guestCounter.font12.darkText li[data-cy*='travel']")
    applyButton = (By.CSS_SELECTOR, "button.primaryBtn.btnApply.pushRight")
    regularFareButton = (By.CSS_SELECTOR, "li.font12.blackText.latoBold.activeItem")
    searchButton = (By.CSS_SELECTOR, "a.primaryBtn.font24.latoBold.widgetSearchBtn")

    # Methods
    def hitFlightButton(self):
        self.driver.find_element(*LandingPage.flightButton).click()

    def getTravelCategoryList(self):
        return self.driver.find_elements(*LandingPage.travelCategories)

    def typeFrom(self):
        action = ActionChains(self.driver)
        departureTab = self.driver.find_element(*LandingPage.travelFrom)
        action.move_to_element(departureTab).perform()
        departureTab.click()

    def typeTo(self):
        action = ActionChains(self.driver)
        destinationTab = self.driver.find_element(*LandingPage.travelTo)
        action.move_to_element(destinationTab).perform()
        destinationTab.click()

    def writeInFrom(self):
        return self.driver.find_element(*LandingPage.textboxFrom)

    def writeInTo(self):
        return self.driver.find_element(*LandingPage.textboxTo)

    def getCityList(self):
        cities = self.driver.find_elements(*LandingPage.cityList)
        return cities

    '''def getDestCityList(self):
        return self.driver.find_elements(*LandingPage.destCityList)
        # cityList destCityList
    '''
    def hitDepartureButton(self):
        return self.driver.find_element(*LandingPage.departureDateButton).click()

    def getMonthList(self):
        return self.driver.find_elements(*LandingPage.monthList)

    def hitTravellersClassButton(self):
        return self.driver.find_element(*LandingPage.travellersClass).click()

    def countFromAdults(self):
        return self.driver.find_elements(*LandingPage.adultsCount)

    def getJourneyClassList(self):
        return self.driver.find_elements(*LandingPage.journeyClassList)

    def hitApplyButton(self):
        self.driver.find_element(*LandingPage.applyButton).click()

    def hitRegularFareButton(self):
        self.driver.find_element(*LandingPage.regularFareButton).click()

    def hitSearchButton(self):
        self.driver.find_element(*LandingPage.searchButton).click()
