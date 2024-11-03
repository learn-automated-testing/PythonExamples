from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

def test_checkboxes(setup):
    driver = setup
    driver.get("https://practiceautomatedtesting.com/webelements/Checkboxes")

    labels = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.checkbox-label ')))
    
    for label in labels:
        checkbox_class_before_click = label.find_element_by_xpath('./span').get_attribute("class")
        label.click()
        checkbox_class_after_click = label.find_element_by_xpath('./span').get_attribute("class")
        
        assert checkbox_class_before_click != checkbox_class_after_click