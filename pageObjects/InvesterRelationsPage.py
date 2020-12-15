from selenium.webdriver.common.by import By


class InvesterRelationsPage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    aum = (By.CSS_SELECTOR, "a.ModuleHeadline")

    # Methods
    # Method_to_navigate_to_Asset under management Page
    def navigateToAumLink(self):
        self.driver.find_element(*InvesterRelationsPage.aum).click()
        # Navigating to the newly opened window
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
