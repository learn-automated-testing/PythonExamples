from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Firefox()

@pytest.fixture
def setup():
    driver.get('https://practiceautomatedtesting.com/webelements/Checkboxes')
    yield
    driver.quit()

@pytest.mark.parametrize('checkbox_id', ['checkbox1', 'checkbox2'])
def test_checkbox_selection(setup, checkbox_id):
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, checkbox_id)))
    checkbox.click()

    assert checkbox.get_attribute('checked') == 'true', 'Fail: Checkbox not selected'

    smiley = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'smiley')))
    assert smiley.is_displayed(), 'Fail: Smiley not displayed'

    bad_smiley = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bad_smiley')))
    assert not bad_smiley.is_displayed(), 'Fail: Bad smiley displayed'