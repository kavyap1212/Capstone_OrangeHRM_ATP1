from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
from LoginPage import LoginPage
from PIMPage import PIMPage
ORANGEHRM_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

class TestCases:
    def __init__(self, port=9515):
        self.driver = None
        self.port = port  # Store the port number
        self.initialize_driver()
        self.login_page = LoginPage(self.driver)
        self.pim_page = PIMPage(self.driver)

    def initialize_driver(self):
        retry_count = 0
        max_retries = 3
        while retry_count < max_retries:
            try:
                chrome_service = Service(executable_path="c:/Users/new/OneDrive/Documents/Python_Scripts/Chromedriver/chromedriver.exe", port=self.port)
                chrome_options = Options()
                self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
                self.driver.maximize_window()
                break
            except WebDriverException as e:
                print(f"WebDriver initialization failed: {e}")
                retry_count += 1
                time.sleep(2)  # Add a delay before retrying
        if not self.driver:
            raise Exception("Failed to initialize WebDriver after several attempts.")

    def open_orangehrm(self):
        retry_count = 0
        max_retries = 3
        while retry_count < max_retries:
            try:
                self.driver.get(ORANGEHRM_URL)
                break
            except WebDriverException as e:
                print(f"Failed to open URL: {e}")
                retry_count += 1
                time.sleep(2)  # Add a delay before retrying
        if retry_count == max_retries:
            raise Exception("Failed to open URL after several attempts.")

    def close(self):
        if self.driver:
            self.driver.quit()

    def TC_Login_01(self):
        try:
            self.open_orangehrm()
            self.login_page.login('Admin', 'admin123')
            time.sleep(1)
            print("Logged in successfully (if no error message is displayed)")
        finally:
            self.close()

    def TC_Login_02(self):
        try:
            self.open_orangehrm()
            self.login_page.login('Admin', 'Invalidpassword')
            time.sleep(3)
            error_message = self.login_page.get_error_message()
            if error_message:
                print(f"Error message displayed: {error_message}")
            else:
                print("No error message displayed.")
        except Exception as e:
            print(f"An error occurred in TC_Login_02: {e}")
        finally:
            self.close()
    
        
    def TC_PIM_01(self):
        try:
            self.open_orangehrm()
            self.login_page.login('Admin', 'admin123')
            self.pim_page.navigate_to_pim()
            self.pim_page.add_new_employee('John', 'Doe')
            print("New employee added successfully.")
        except Exception as e:
            print(f"An error occurred in TC_PIM_01: {e}")
        finally:
            self.close()
        

    def TC_PIM_02(self):
        try:
            self.open_orangehrm()
            self.login_page.login('Admin', 'admin123')
            self.pim_page.navigate_to_pim()
            self.pim_page.edit_employee('John Doe', 'Jane', 'Doe')
            print("Tested Employee details editing successfully.")
        except Exception as e:
            print(f"An error occurred in TC_PIM_02: {e}")
        finally:
            self.close()

    def TC_PIM_03(self):
        try:
            self.open_orangehrm()
            self.login_page.login('Admin', 'admin123')
            self.pim_page.navigate_to_pim()
            self.pim_page.delete_employee('Jane Doe')
            print("Employee deleted successfully.")
        except Exception as e:
            print(f"An error occurred in TC_PIM_03: {e}")
        finally:
            self.close()

if __name__ == "__main__":
    # Specify different ports for each test case
    test_ports = {
        "TC_Login_01": 9515,
        "TC_Login_02": 9516,
        "TC_PIM_01": 9517,
        "TC_PIM_02": 9518,
        "TC_PIM_03": 9519
    }

    for test_case, port in test_ports.items():
        print(f"\nRunning {test_case} on port {port}:")
        tests = TestCases(port=port)
        
        # Run the appropriate test case based on the name
        getattr(tests, test_case)()