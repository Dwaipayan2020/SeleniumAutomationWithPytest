import inspect
import logging

import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    '''def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
    '''
    '''def verifyElementPresence(self, webElement):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(webElement))
    '''

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    # Method to reload application url
    def reload_ApplicationUrl(self, url):
        self.driver.get(url)

    # Method to wait implicitly for 10 seconds
    def waitImplicitly(self, TimeInSeconds):
        sec = TimeInSeconds
        self.driver.implicitly_wait(sec)

    # Method to wait explicitly for 10 seconds
    def waitExplicitlyUntilVisibilityOfElement(self, element):
        wait = WebDriverWait(self.driver, 10)
        expectedElement = wait.until(EC.visibility_of_element_located(element))
        return expectedElement

    # Method to scoll through webelement
    def scrollPage(self, webElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", webElement)

    # Method to view text Content
    def viewTextContent(self, webElement):
        stringElement = webElement.text
        return stringElement

        # Method to navigate to a child link

    def clickSelected_ChildLink_In_ParentLink(self, ParentElements, linkName, subLinkName):
        try:

            action = ActionChains(self.driver)
            elements = ParentElements

            for element in elements:
                if element.text == linkName:
                    print(element.text)
                    action.move_to_element(element).perform()
                    sub_links = element.find_elements_by_css_selector(
                        "ul.submenu.is-dropdown-submenu.first-sub.vertical li.is-submenu-item.is-dropdown-submenu-item a")
                    break

            for sub_link in sub_links:
                print(sub_link.text)
                if sub_link.text == subLinkName:
                    sub_link.click()
                    break
        except NoSuchElementException as exeption:
            print("No such link name is found and test failed")

    # This method returns selected option
    def selectOptionFromList(self, optionList, optionName):

        try:
            # wait = WebDriverWait(self.driver, 5)
            # options = wait.until(EC.presence_of_all_elements_located(optionList))
            # action = ActionChains(self.driver)
            options = optionList
            for option in options:
                if option.text.strip() == optionName:
                    print("choiceIs" + option.text)
                    # action.move_to_element(option).click().perform()
                    option.click()
                    break

        except StaleElementReferenceException as exception:

            e = exception.stacktrace
            options = optionList
            for option in options:
                if option.text.strip() == optionName:
                    print("choiceIs" + option.text)
                    # action.move_to_element(option).click().perform()
                    option.click()
                    break

            print("StaleElementReferenceException is occured .")

    # DatePickerFunction
    def pickYourDate(self, monthList, monthName, day):
        try:
            nextMonthButton = self.driver.find_element_by_css_selector(
                "span.DayPicker-NavButton.DayPicker-NavButton--next")
            months = monthList
            for month in months:

                if month.text == monthName:
                    print(month.text)
                    dates = month.find_elements_by_xpath("//parent::div/following-sibling::div")
                    for dateClassName in dates:
                        if dateClassName.get_attribute("class") == 'DayPicker-Day--selected':
                            selectedDate = dateClassName.find_element_by_xpath("//div[@class='dateInnerCell']/p[1]")
                            if selectedDate.text == day:
                                selectedDate.click()
                                break
                        elif dateClassName.get_attribute("class") == 'DayPicker-Day--today':
                            currentDate = dateClassName.find_element_by_xpath("//div[@class='dateInnerCell']/p[1]")
                            if currentDate.text == day:
                                currentDate.click()
                                break
                        elif dateClassName.get_attribute("class") == 'DayPicker-Day':
                            anyOtherDates = dateClassName.find_elements_by_xpath("//div[@class='dateInnerCell']/p[1]")
                            for anyDate in anyOtherDates:
                                if anyDate.text == day:
                                    anyDate.click()
                                    break
                        elif dateClassName.get_attribute("class") == 'DayPicker-Day--disabled':
                            disabledDates = dateClassName.find_elements_by_xpath("//div[@class='dateInnerCell']/p[1]")
                            for disabledDate in disabledDates:
                                if disabledDate.text == day:
                                    # assertEqual(actual, expected, errorMessage)
                                    self.assertEqual(disabledDate.text, day, "The entered date is a past date ")
                                    break

                    break
                else:
                    nextMonthButton.click()

        except NoSuchElementException as exception:
            e = exception.stacktrace
            print("Incorrect Test Data Passed as Date " + e)

    def dateSelecter(self, monthName, day):
        nextMonthButton = self.driver.find_element_by_css_selector(
            "span.DayPicker-NavButton.DayPicker-NavButton--next")
        currentDateValue = self.driver.find_element_by_css_selector("div[class*='today'] p:nth-child(1)")
        print("Current date is - " + currentDateValue.text)
        currentMonth = currentDateValue.find_element_by_xpath(
            "//parent::div/parent::div/parent::div/parent::div/parent::div")
        nextMonth = self.driver.find_element_by_css_selector("div.DayPicker-Months div.DayPicker-Month:nth-child(2)")
        currentMonthValue = currentMonth.find_element_by_xpath("//div[@class='DayPicker-Caption']/div")
        nextMonthValue = self.driver.find_element_by_css_selector(
            "div.DayPicker-Months div.DayPicker-Month:nth-child(2) div.DayPicker-Caption div")
        print("Current month is - " + currentMonthValue.text)
        print("Next month is - " + nextMonthValue.text)
        if (currentMonthValue.text == monthName):
            anyOtherDates = currentMonth.find_elements_by_xpath(
                "//div[@class='DayPicker-Day']//div[@class='dateInnerCell']/p[1]")
            selectedDate = currentMonth.find_elements_by_xpath(
                "//div[@class='DayPicker-Day DayPicker-Day--selected']//div[@class='dateInnerCell']/p[1]")
            currentDate = currentDateValue
            disabledDatesCurrentMonth = currentMonth.find_elements_by_xpath(
                "//div[@class='DayPicker-Day--disabled']//div[@class='dateInnerCell']/p[1]")
            flag = False
            flag1 = False
            flag2 = False
            flag3 = False
            selectedDateVal = None
            anydateValue = None
            disableDate = None

            if currentDate.text == day:
                c = currentDate
                flag = True

            for d in selectedDate:
                if d.text == day:
                    selectedDateVal = d
                    flag1 = True
                    print("d is :")
                    print(flag1)
                    break

            for anydate in anyOtherDates:
                print("AnyDate in current month : " + anydate.text)
                print("expdate in current month : " + day)
                print("Current_Date in current month : " + currentDateValue.text)
                if anydate.text == day:
                    anydateValue = anydate
                    flag2 = True
                    break
            for anyDisabledDate in disabledDatesCurrentMonth:
                if (anyDisabledDate.text == day):
                    disableDate = anyDisabledDate
                    flag3 = True
                    # self.assertEqual(anyDisabledDate.text, day,"Please enter a valid date. The entered date is a past date ")
                    break
            # If current date and anydate both matches
            if flag == True and flag1==False and flag2 == True and flag3 == False:
                c.click()
            # If only current date matches not anydate
            elif flag == True and flag1==False and flag2 == False and flag3== False:
                c.click()
            # If current date doesn't match but anydate except current date matches
            elif flag == False or flag1==False and (flag2 == True and flag3== False):
                anydateValue.click()
            # If current date , selected date and anydate all matches
            elif flag == True and flag1 == True and flag2 == True and flag3== False:
                c.click()
            # If selected date and anydate both matches the same day but not the current date
            elif flag == False and flag1 == True and flag2 == True and flag3== False:
                selectedDateVal.click()
            # If current date and selected date both matches  but not the any date
            elif flag == True and flag1 == True and flag2 == False and flag3== False:
                c.click()
            # If the day matches anydate except current date and selected date
            elif flag == False and flag1 == False and flag2 == True and flag3== False:
                anydateValue.click()
            # If the day matches both a disabled date and anydate
            elif flag == False or flag1 == False and (flag2 == True and flag3 == True):
                self.assertNotEqual(disableDate.text, day, "Please enter a valid date. The entered date is a past date ")

            # If the day matches only a disabled date.
            elif flag== False and flag1 == False and flag2 == False and flag3 == True:
                self.assertNotEqual(disableDate.text, day,"Please enter a valid date. The entered date is a past date ")

        elif (nextMonthValue.text == monthName):
            nextMonthDates = nextMonth.find_elements_by_xpath(
                "//div[@class='DayPicker-Day']//div[@class='dateInnerCell']/p[1]")
            disabledDatesNextMonth = nextMonth.find_elements_by_xpath(
                "//div[@class='DayPicker-Day--disabled']//div[@class='dateInnerCell']/p[1]")

            flag1 = False
            flag2 = False

            anyNextMonthdateValue = None
            disableDateValue = None

            for anyNextMonthdate in nextMonthDates:
                print("Any month Date in next month : " + anyNextMonthdate.text)
                if anyNextMonthdate.text == day:
                    anyNextMonthdateValue = anyNextMonthdate
                    flag1 = True
                    break
            for disabledDate in disabledDatesNextMonth:
                if (disabledDate.text == day):
                    disableDateValue = disabledDate
                    flag2 = True

                    break
            if flag1 == True:
                anyNextMonthdateValue.click()
            elif flag2 == True:
                self.assertEqual(disableDateValue.text, day,
                                 "Please enter a valid date. The entered date is a past date ")


        else:
            nextMonthButton.click()
            print("Next month button is clicked first time.")
            othermonthNames = self.driver.find_elements_by_css_selector("div.DayPicker-Month")
            for othermonth in othermonthNames:
                othermonthName = othermonth.find_element_by_xpath("//div[@class='DayPicker-Caption']/div")
                print("Other month name is " + othermonthName.text)
                if othermonthName.text == monthName:
                    expectedDatesMonth = othermonth.find_elements_by_xpath(
                        "//div[@class='DayPicker-Body']//div[@class='DayPicker-Day']//div[@class='dateInnerCell']/p[1]")
                    disabledDates = othermonth.find_elements_by_xpath(
                        "//div[@class='DayPicker-Day--disabled']//div[@class='dateInnerCell']/p[1]")
                    flag1 = False
                    flag2 = False
                    anyOtherMonthDate = None
                    disabledOtherMonthDate = None
                    for date in expectedDatesMonth:
                        print("Any date in other month is: " + date.text)
                        if date.text == day:
                            anyOtherMonthDate = date
                            flag1 = True
                            break

                    for disabledDate in disabledDates:
                        if (disabledDate.text == day):
                            disabledOtherMonthDate = disabledDate
                            flag2 = True
                            # self.assertEqual(disabledDate.text, day,"Please enter a valid date. The entered date is a past date ")
                            break
                    if flag1 == True:
                        anyOtherMonthDate.click()
                    elif flag2 == True:
                        self.assertEqual(disabledOtherMonthDate.text, day,
                                         "Please enter a valid date. The entered date is a past date ")

                    break
                else:
                    nextMonthButton.click()
                    print("Next month button is clicked again.")
                    continue

    def captureKeyValueInList(self, keys, values):
        item = {}
        for key in keys:
            keyItem = key.text

        for value in values:
            valueItem = value.text

        for i in range(0, len(keyItem)):
            item[keyItem[i]] = valueItem[i]
            data = keyItem[i] + item[keyItem[i]]

        return data
