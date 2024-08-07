from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_module = (By.XPATH, '//span[text()="PIM"]')
        self.add_button = (By.XPATH, '//button[text()=" Add "]')
        self.first_name_field = (By.NAME, 'firstName')
        self.last_name_field = (By.NAME, 'lastName')
        self.save_button = (By.XPATH, '//button[@type="submit"]')
        self.second_save_button = (By.XPATH, '//button[contains(@class, "oxd-button--secondary") and text()=" Save "]')
        self.employee_list = (By.XPATH, '//input[@placeholder="Type for hints..."]')
        self.search_button = (By.XPATH, '//button[@type="submit"]')
        self.edit_button_img = (By.XPATH, '//i[contains(@class, "bi-pencil-fill")]')
        self.delete_button_img = (By.XPATH, '//i[contains(@class, "bi-trash")]')
        self.confirm_delete_button = (By.CSS_SELECTOR, '#app > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > div.orangehrm-modal-footer > button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin')

    def scroll_to_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except Exception as e:
            print(f"Error scrolling to element: {by_locator}. Error: {e}")
            return None

    def navigate_to_pim(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pim_module)).click()
            print("Navigated to PIM module successfully.")
            time.sleep(2)  # Added delay
        except Exception as e:
            print(f"Error navigating to PIM module: {e}")

    def add_new_employee(self, first_name, last_name):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.add_button)).click()
            print("Clicked Add button.")
            time.sleep(2)  # Added delay
            
            first_name_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.first_name_field))
            first_name_field.send_keys(first_name)
            print("Entered first name.")
            time.sleep(2)  # Added delay
            
            last_name_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.last_name_field))
            last_name_field.send_keys(last_name)
            print("Entered last name.")
            time.sleep(2)  # Added delay
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.save_button)).click()
            print("Clicked save button on first page.")
            time.sleep(2)  # Added delay
            
            # Click save button on the next page
            second_save_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.second_save_button))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", second_save_button)
            second_save_button.click()
            print("Clicked save button on second page.")
            time.sleep(2)  # Added delay
            
            print("New employee added successfully.")
        except Exception as e:
            print(f"Error adding new employee: {e}")

    def edit_employee(self, employee_name, new_first_name, new_last_name):
        try:
            employee_list = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.employee_list))
            employee_list.send_keys(employee_name)
            employee_list.send_keys(Keys.RETURN)
            print("Entered employee name for search.")
            time.sleep(2)  # Added delay
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.search_button)).click()
            print("Clicked search button.")
            time.sleep(2)  # Added delay
            
            self.scroll_to_element(self.edit_button_img)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.edit_button_img)).click()
            print("Clicked edit button.")
            time.sleep(2)  # Added delay
            
            first_name_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.first_name_field))
            first_name_field.clear()
            time.sleep(2)  # Added delay
            first_name_field.send_keys(new_first_name)
            print("Entered new first name.")
            time.sleep(2)  # Added delay
            
            last_name_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.last_name_field))
            last_name_field.clear()
            time.sleep(2)  # Added delay
            last_name_field.send_keys(new_last_name)
            print("Entered new last name.")
            time.sleep(2)  # Added delay
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.save_button)).click()
            print("Clicked save button on first page.")
            time.sleep(2)  # Added delay
            
            # Click save button on the next page
            second_save_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.second_save_button))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", second_save_button)
            second_save_button.click()
            print("Clicked save button on second page.")
            time.sleep(2)  # Added delay
            
            print("Employee details edited successfully.")
        except Exception as e:
            print(f"Error editing employee: {e}")

    def delete_employee(self, employee_name):
        try:
            employee_list = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.employee_list))
            employee_list.send_keys(employee_name)
            employee_list.send_keys(Keys.RETURN)
            print("Entered employee name for search.")
            time.sleep(2)  # Added delay
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.search_button)).click()
            print("Clicked search button.")
            time.sleep(2)  # Added delay
            
            self.scroll_to_element(self.delete_button_img)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.delete_button_img)).click()
            print("Clicked delete button.")
            time.sleep(2)  # Added delay
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.confirm_delete_button)).click()
            print("Clicked confirm delete button.")
            time.sleep(2)  # Added delay
            
            print("Employee deleted successfully.")
        except Exception as e:
            print(f"Error deleting employee: {e}")