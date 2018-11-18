import time
from selenium import webdriver

class instagram:

    def like_by_nickname(self, nickName):
        driver.get('https://instagram.com/' + nickName)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
        time.sleep(5)
        for i in range(9):
            self.like()


    def like_by_tag(self, tag):
        driver.get('https://instagram.com/explore/tags/' + tag)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
        time.sleep(5)
        for i in range(9):
            self.like()


    def like(self):
        elementClass = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span').get_attribute('class')
        if (elementClass.find('red') == -1):
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()

        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        time.sleep(5)


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

driver.find_element_by_name('username').send_keys('tsarevna_laygushka')
driver.find_element_by_name('password').send_keys('Dasha190194')
driver.find_element_by_xpath('//button').submit()
time.sleep(5)

instagram = instagram()
instagram.like_by_tag('осень')







