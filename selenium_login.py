from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:5000/login"


def login(driver, username, password):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    return wait.until(EC.presence_of_element_located((By.ID, "message"))).text


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

assert login(driver, "admin", "admin123") == "Login successful"
print("Valid login test passed")

assert login(driver, "admin", "wrong") == "Invalid username or password"
print("Invalid login test passed")

driver.quit()
