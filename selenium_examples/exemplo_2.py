from page_objects import PageObject, PageElement
from selenium import webdriver


class Google(PageObject):
    search_bar = PageElement(id_='lst-ib')
    btn_search = PageElement(name='btnK')
    btn_lucky = PageElement(name='btnI')


browser = webdriver.Firefox()

g = Google(browser, 'http://www.google.com')

# Search
# g.get('')
# g.search_bar.send_keys('Live de Python')
# g.btn_search.click()

# lucky
g.get('')
g.search_bar.send_keys('Live de Python')
g.btn_lucky.click()
