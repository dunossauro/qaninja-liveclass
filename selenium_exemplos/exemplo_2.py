from selenium import webdriver
from page_objects import PageObject, PageElement


class Google(PageObject):
    search_bar = PageElement(id_='lst-ib')
    btn_search = PageElement(name='btnK')
    btn_lucky = PageElement(name='btnI')

    def search(self, text):
        self.search_bar.send_keys(text)
        self.btn_search.click()

    def lucky(self, text):
        self.search_bar.send_keys(text)
        self.btn_lucky.click()


browser = webdriver.Firefox()

g = Google(browser, 'http://google.com/')
g.search('live de python')
# g.lucky('live de python')
# g.search_bar.send_keys('live de python')
# # g.btn_search.click()
# g.btn_lucky.click()
