import pytest

from TestData.MasterData import MasterData
from pageObjects.LandingPage import LandingPage
from pageObjects.SearchResultsPage import SearchResultsPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_availableFlights(self, getData):
        # Object creation of respective pages
        log = self.getLogger()
        landingPage = LandingPage(self.driver)

        # Execution_Steps and Methods
        log.info("Landed on Airport :) ")
        log.info("Clicking on Aeroplane Icon, flights")
        landingPage.hitFlightButton()
        log.info("Select Trip Type : Oneway, Round Trip Or MultyCity")
        travelCategoryList = landingPage.getTravelCategoryList()
        travelCategory = getData["TravelCategory"]
        self.selectOptionFromList(travelCategoryList, travelCategory)
        log.info("Selected Trip Type is : " + travelCategory)
        log.info("Choose From :")
        fromCity = getData["From"]
        landingPage.typeFrom()
        # landingPage.writeInFrom().click()
        landingPage.writeInFrom().send_keys(fromCity)
        self.waitImplicitly(1)
        departureCity = getData["DepartureCity"]
        deptCityNames = landingPage.getCityList()

        self.selectOptionFromList(deptCityNames, departureCity)
        self.waitImplicitly(2)
        log.info("From : " + " selected Departure City is " + departureCity)
        log.info("Choose Fly To : ")
        toCity = getData["To"]
        destinationCity = getData["DestinationCity"]
        landingPage.typeTo()
        # landingPage.writeInTo().click()
        landingPage.writeInTo().send_keys(toCity)
        self.waitImplicitly(1)
        destCityNames = landingPage.getCityList()

        self.selectOptionFromList(destCityNames, destinationCity)

        log.info("To : " + " selected Destination City  is " + destinationCity)
        log.info("Click Departure to decide the day of travel : ")
        landingPage.hitDepartureButton()
        monthsList = landingPage.getMonthList()
        departureMonth = getData["DepartureMonth"]
        departureDay = getData["DepartureDay"]
        self.dateSelecter(departureMonth, departureDay)
        log.info("You have entered Departure Date as  : " + departureDay + " , " + departureMonth)
        log.info("Click Traveller Class   : " + " Choose no. of Adults,children or infants and also to select Class ")
        landingPage.hitTravellersClassButton()
        adults = landingPage.countFromAdults()
        adultCount = getData["AdultsCount"]
        self.selectOptionFromList(adults, adultCount)
        log.info(adultCount + " adults are looking for available flights.")
        log.info("Click Apply")
        travellerJourneyClass = landingPage.getJourneyClassList()
        travelClassName = getData["TravelClass"]
        self.selectOptionFromList(travellerJourneyClass, travelClassName)
        landingPage.hitApplyButton()
        self.waitImplicitly(2)
        landingPage.hitRegularFareButton()
        log.info("Traveller has chosen Regular Fare option.")
        log.info("Now Click SEARCH  to check for available flight on this route.")
        landingPage.hitSearchButton()
        log.info("Make my trip is searching available flights for you !")
        '''searchResPage = SearchResultsPage(self.driver)
        activeBlueIcon = searchResPage.getActiveDayIcon()
        displayActiveBlueIcon = self.waitExplicitlyUntilVisibilityOfElement(activeBlueIcon)
        log.info("Blue icon displays date as " + displayActiveBlueIcon.text)
        log.info("Search is performed! ")
        flightNames = searchResPage.getAirwaysNameList()
        flightCodes = searchResPage.getFliCodeList()
        log.info("Available flights are : " + self.captureKeyValueInList(flightNames, flightCodes))'''

    @pytest.fixture(params=MasterData.getTestData("JourneyInformation"))
    def getData(self, request):
        print(request.param)
        return request.param
