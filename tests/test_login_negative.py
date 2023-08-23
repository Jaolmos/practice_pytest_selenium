import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        # driver = webdriver.Chrome()
        time.sleep(2)

        # Go to webpage "https://practicetestautomation.com/practice-test-login/"
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(4)

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # PushSubmit button
        submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be "

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        # driver = webdriver.Chrome()
        time.sleep(2)

        # Go to webpage "https://practicetestautomation.com/practice-test-login/"
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(4)

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # PushSubmit button
        submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be "

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_password(self, driver):
        # Open page
        # driver = webdriver.Chrome()
        time.sleep(2)

        # Go to webpage "https://practicetestautomation.com/practice-test-login/"
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(4)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(4)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be "

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
