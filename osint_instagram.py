from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote_plus
import time

default_url = "https://www.instagram.com/explore/tags/"
search_tag = input('>>')

full_url = default_url + quote_plus(search_tag)


driver = webdriver.Chrome('chromedriver.exe')
driver.get(full_url)

time.sleep(5)

html = driver.page_source
crawl = BeautifulSoup(html)
definition_crawl = crawl.select('.v1Nh3.kIKUG._bz0w')

body = driver.find_element_by_tag_name("body")
pagesdown = 5

while pagesdown:
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(2)
	pagesdown -=1

count = 1

for i in definition_crawl:
	img_save = i.select_one('.KL4Bh').img['src']
	with urlopen(img_save) as f:
		with open('./image/'+str(count)+'.jpg','wb') as h:
			img = f.read()
			h.write(img)
	count += 1

driver.close()




