import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit() 

def test_checkboxes(driver):
    driver.get("https://practiceautomatedtesting.com/webelements/Checkboxes")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    labels = driver.find_elements_by_class_name('checkbox-label ')
    for label in labels:
        label.click()
        span = label.find_element_by_tag_name('span')
        assert ('smiley' in span.get_attribute('class') or 'bad smiley' in span.get_attribute('class')), f"Checkbox {label.text} did not display the correct icon."