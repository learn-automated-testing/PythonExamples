import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_checkbox_interaction():
    driver = webdriver.Firefox()
    driver.get('https://practiceautomatedtesting.com/webelements/Checkboxes')

    checkbox1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'checkbox1')))
    checkbox2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'checkbox2')))

    ActionChains(driver).click(checkbox1).perform()

    # Replace 'smiley' with the actual id, class or xpath of the smiley element
    smiley1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'smiley')))
    assert smiley1.is_displayed()

    ActionChains(driver).click(checkbox2).perform()

    # Replace 'badsmiley' with the actual id, class or xpath of the bad smiley 
    bad_smiley2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'badsmiley')))
    assert bad_smiley2.is_displayed()

    driver.quit()