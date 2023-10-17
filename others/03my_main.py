from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

names = [name.text for name in driver.find_elements(By.CSS_SELECTOR, value=".shrubbery .menu a")[5:10]]
times = [time.text for time in driver.find_elements(By.CSS_SELECTOR, value=".shrubbery .menu time")[5:10]]

result_dict = {}

for idx, (name, time) in enumerate(zip(names, times)):
    result_dict[idx] = {'time': time, 'name': name}

print(result_dict)
driver.quit()