from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 10)

# language = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
language = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#langSelect-EN")))
language.click()

for i in range(5):
    wait = WebDriverWait(driver, 10)
    buy = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"#productPrice{i}")))
    numbers = int(buy.text)
    cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
    for i in range(numbers):
        cookie.click()

    wait = WebDriverWait(driver, 10)
    buy = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"#productPrice{i}")))
    buy.click()



