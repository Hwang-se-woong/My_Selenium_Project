from selenium import webdriver
import private_info

driver = webdriver.Chrome()
# driver.get('https://www.naver.com/')
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

driver.find_element_by_name('id').send_keys(private_info.id)
driver.find_element_by_name('pw').send_keys(private_info.pw)
driver.find_element_by_xpath('//*[@id="log.login"]').click()