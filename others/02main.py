from selenium import webdriver
from selenium.webdriver.common.by import By

# 1、初始化浏览器对象，打开网页(确保不自动关闭、手动关闭)
# 确保打开的网页不会自动关闭：detach 设置为 True; close是手动关闭活动页面，quit 是手动关闭整个浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# 初始化一个要驱动的浏览器对象, 打开一个网页
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/-/zh/dp/B0B3M4VVPR/ref=sbl_dpx_kitchen-mixers_B07HC8MS3Z_0?th=1")
driver.get("https://www.python.org/")

# 2、获取网页的元素: By: class, name (input 类), id, selector, Xpath
# .text, .tag_name
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_Link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_Link.text)
bug_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
print(bug_link.text)

driver.find_elements()

# driver.close()
driver.quit()
