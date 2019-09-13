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
        driver.get("https://www.google.com/search?q=%E0%B8%AB%E0%B8%A1%E0%B8%B2&source=lnms&tbm=isch&sa=X&ved=0ahUKEwie4d3omM3kAhUPeysKHX7hBLsQ_AUIEigB&biw=1366&bih=654")
        self.assertIn("Google", driver.title)
        # search google
        # search__input = driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        
        # search__input.send_keys("หมา")
        # driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[3]/center/input[1]").click()
        # test
        # driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]")
        # 


        # /html/body/div/div[4]/form/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]/div/span
        # search image
        # driver.find_element_by_class_name('q.qs').click()
        # scroll down a page
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        # click search more
        driver.find_element_by_id('smbw').click()
        # scroll down a page
        lenOfPageTwo = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPageTwo=document.body.scrollHeight;return lenOfPageTwo;")
        match=False
        while(match==False):
            lastCount = lenOfPageTwo
            time.sleep(3)
            lenOfPageTwo = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPageTwo=document.body.scrollHeight;return lenOfPageTwo;")
            if lastCount==lenOfPageTwo:
                match=True

        
        photoAll = driver.find_elements_by_class_name("rg_ic.rg_i")
        # image = driver.find_elements_by_tag_name("img")
        # img_src = image.get_attribute("src")
        # print(image)
      


        # listphoto = []
        for i in photoAll:
            
            print(i.get_property("src"))
            print("\n")
        print(len(photoAll))

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()