from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://google.com')
browser.current_url
browser.tittle
