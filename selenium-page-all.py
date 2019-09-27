import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import requests

# api = requests.get('https://scrape-name-surname.herokuapp.com/').json()
# print(len(api))

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pantip.com/search?q=%E0%B8%8B%E0%B8%B2%E0%B8%A5%E0%B8%B2%E0%B9%80%E0%B8%9B%E0%B8%B2%E0%B8%A7%E0%B8%A3%E0%B8%B2%E0%B8%A0%E0%B8%A3%E0%B8%93%E0%B9%8C")
        # self.assertIn("Google", driver.title)


    


        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        # formular
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        # 
        link_header = driver.find_elements_by_class_name("datasearch-in")
        list_all_website = []
        for i in range(0,len(link_header)):
            link_web_site = driver.find_elements_by_class_name("datasearch-in")[i].get_property("href")
            if link_web_site not in list_all_website:
                if 'comment' not in link_web_site:
                    list_all_website.append(link_web_site)
        print(list_all_website)
        # print(list_all_website)
        # click search more
        # driver.find_element_by_id('smbw').click()
        # scroll down a page


        # lenOfPageTwo = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPageTwo=document.body.scrollHeight;return lenOfPageTwo;")
        # match=False
        # while(match==False):
        #     lastCount = lenOfPageTwo
        #     time.sleep(3)
        #     lenOfPageTwo = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPageTwo=document.body.scrollHeight;return lenOfPageTwo;")
        #     if lastCount==lenOfPageTwo:
        #         match=True

        
        # photoAll = driver.find_elements_by_class_name("rg_ic.rg_i")

      


        # for i in photoAll:
            
        #     print(i.get_property("src"))
        #     print("\n")
        # print(len(photoAll))

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()