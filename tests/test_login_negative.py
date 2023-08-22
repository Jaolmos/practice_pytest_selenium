import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self):
        # Open page
        driver = webdriver.Chrome()
        time.sleep(2)

        # Go to webpage "https://practicetestautomation.com/practice-test-login/"
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Puch Submit button
        submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be "

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"
