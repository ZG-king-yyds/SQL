from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.maximize_window()

driver.find_element_by_id('kw').send_keys("奔驰大G")
driver.find_element_by_id('su').click()

# time.sleep(3)
# driver.quit()



