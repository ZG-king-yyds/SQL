from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.maximize_window()

driver.find_element_by_id('kw').send_keys("长城炮")
driver.find_element_by_id('su').click()

time.sleep(3)
driver.quit()



