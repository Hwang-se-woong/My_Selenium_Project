from selenium import webdriver
from bs4 import BeautifulSoup
import private_info

delay = 3
driver = webdriver.Chrome()
# driver.get('https://www.naver.com/')
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

driver.find_element_by_name('id').send_keys(private_info.id)
driver.find_element_by_name('pw').send_keys(private_info.pw)
driver.find_element_by_xpath('//*[@id="log.login"]').click()

driver.get('https://mail.naver.com')
driver.implicitly_wait(delay)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

mailList = soup.select('ol.mailList > li > div.mTitle > div.subject > a > span.text > strong.mail_title')

num = 0

for n in mailList:
    print("\n")
    num += 1
    print(num)
    print(n.text.strip())

driver.close()