import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_checkboxes(driver):
    driver.get('https://practiceautomatedtesting.com/webelements/Checkboxes')

    checkbox1 = driver.find_element_by_id('checkbox1')
    checkbox1.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'checkbox1')))
    assert checkbox1.is_selected(), "Checkbox1 not activated!"

    checkbox2 = driver.find_element_by_id('checkbox2')
    checkbox2.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'checkbox2')))
    assert checkbox2.is_selected(), "Checkbox2 not activated!"
    
    smiley = driver.find_element_by_class_name('smiley')
    assert smiley.is_displayed(), "Smiley is not displayed!"

    bad_smiley = driver.find_element_by_class_name('bad_smiley')
    assert not bad_smiley.is_displayed(), "Bad smiley is displayed!"