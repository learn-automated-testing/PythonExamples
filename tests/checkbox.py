from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestCheckboxesPage:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_checkboxes(self):
        self.driver.get("https://practiceautomatedtesting.com/webelements/Checkboxes")

        checkbox1 = self.wait.until(EC.element_to_be_clickable((By.ID, "checkbox1")))
        checkbox2 = self.wait.until(EC.element_to_be_clickable((By.ID, "checkbox2")))

        checkbox1.click()
        assert checkbox1.is_selected(), "Checkbox 1 not selected"

        checkbox2.click()
        assert checkbox2.is_selected(), "Checkbox 2 not selected"
        
        checkbox1.click()
        assert not checkbox1.is_selected(), "Checkbox 1 not deselected"
        
        checkbox2.click()
        assert not checkbox2.is_selected(), "Checkbox 2 not deselected"

if __name__ == "__main__":
    pytest.main()