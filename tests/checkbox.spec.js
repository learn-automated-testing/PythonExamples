from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practiceautomatedtesting.com/webelements/Checkboxes")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'checkbox1'))
)

checkbox1 = driver.find_element_by_id('checkbox1')
checkbox2 = driver.find_element_by_id('checkbox2')

checkbox1.click()
result1 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/iframe").get_attribute("src")
assert result1.includes("smiley")

checkbox2.click()
result2 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/iframe").get_attribute("src")
assert result2.includes("smiley")

driver.close()