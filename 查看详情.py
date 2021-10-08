from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("redmi note10 pro")
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
driver.find_element_by_xpath("//*[@src='//img12.360buyimg.com/n2/jfs/t1/201434/23/9640/148958/6157ca54Ea9237608/3c72c1e8b2fe5a09.jpg']").click()

time.sleep(3)
driver.quit()



