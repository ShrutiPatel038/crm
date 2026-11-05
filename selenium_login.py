import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:5000/login"


def login(driver, username, password):
    driver.get(URL)
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(2)
    return wait.until(EC.presence_of_element_located((By.ID, "message"))).text


driver = webdriver.Edge()
driver.maximize_window()

assert login(driver, "admin", "admin123") == "Login successful"
print("Valid login test passed")

assert login(driver, "admin", "wrong") == "Invalid username or password"
print("Invalid login test passed")

time.sleep(2)
driver.quit()
