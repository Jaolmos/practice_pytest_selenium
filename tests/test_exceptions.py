import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as excond


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")


        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(excond.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        #row_2_input_locator= driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
