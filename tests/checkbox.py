import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_checkboxes(self):
        self.driver.get("https://practiceautomatedtesting.com/webelements/Checkboxes")
        checkboxes = ['checkbox1', 'checkbox2']

        for checkbox_id in checkboxes:
            checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, checkbox_id)))
            checkbox.click()
            self.assertTrue(checkbox.is_selected())

            # Depending on how the smiley or bad smiley is implement, 
            # additional checks can be done here.
            # e.g. finding the smiley element and asserting it's displayed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()