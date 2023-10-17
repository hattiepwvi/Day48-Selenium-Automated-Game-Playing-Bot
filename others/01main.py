from selenium import webdriver

# 1、初始化浏览器对象，打开网页(确保不自动关闭、手动关闭)
# 确保打开的网页不会自动关闭：detach 设置为 True; close是手动关闭活动页面，quit 是手动关闭整个浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# 初始化一个要驱动的浏览器对象, 打开一个网页
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# driver.close()
driver.quit()
