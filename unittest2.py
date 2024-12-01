import unittest
from unittest.mock import patch, MagicMock
import streamlit as st
from page import login  # Replace `page` with the actual module name where the `login` function is defined

class TestLogin(unittest.TestCase):
    @patch("page.st.text_input")
    @patch("page.st.button")
    @patch("page.auth.sign_in_with_email_and_password")
    @patch("page.st.success")
    @patch("page.st.warning")
    @patch("page.subprocess.Popen")
    @patch("page.os._exit")
    def test_successful_login(
        self,
        mock_exit,
        mock_popen,
        mock_warning,
        mock_success,
        mock_sign_in,
        mock_button,
        mock_text_input,
    ):
        # Mock user inputs
        mock_text_input.side_effect = ["showrav5665@gmail.com", "123321"]
        mock_button.return_value = True  # Simulate the login button being pressed
        mock_sign_in.return_value = {"email": "showrav5665@gmail.com"}  # Simulate successful authentication

        # Call the function
        login()

        # Assertions
        mock_sign_in.assert_called_once_with("showrav5665@gmail.com", "123321")
        mock_success.assert_called_once_with("Logged in successfully!")
        mock_popen.assert_called_once()  # Ensure subprocess is invoked
        mock_exit.assert_called_once_with(0)  # Ensure the application exits
        mock_warning.assert_not_called()  # Ensure no warnings are displayed

    @patch("page.st.text_input")
    @patch("page.st.button")
    @patch("page.auth.sign_in_with_email_and_password")
    @patch("page.st.success")
    @patch("page.st.warning")
    @patch("page.subprocess.Popen")
    @patch("page.os._exit")
    def test_failed_login(
        self,
        mock_exit,
        mock_popen,
        mock_warning,
        mock_success,
        mock_sign_in,
        mock_button,
        mock_text_input,
    ):
        # Mock user inputs
        mock_text_input.side_effect = ["showrav5665@gmail.com", "wrongpassword"]
        mock_button.return_value = True  # Simulate the login button being pressed
        mock_sign_in.side_effect = Exception("Login failed")  # Simulate authentication failure

        # Call the function
        login()

        # Assertions
        mock_sign_in.assert_called_once_with("showrav5665@gmail.com", "wrongpassword")
        mock_warning.assert_called_once_with("Incorrect email or Incorrect password!")
        mock_success.assert_not_called()  # Ensure success is not displayed
        mock_popen.assert_not_called()  # Ensure subprocess is not invoked
        mock_exit.assert_not_called()  # Ensure the application does not exit

if __name__ == "__main__":
    unittest.main()
