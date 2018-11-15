import time
from selenium import webdriver

def like_by_nickname(nickName):
    driver.get('https://instagram.com/' + nickName)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
    time.sleep(5)
    for i in range(9):
        like()


def like_by_tag(tag):
    driver.get('https://instagram.com/explore/tags/' + tag)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
    time.sleep(5)
    for i in range(9):
        like()


def like():
    elementClass = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span').get_attribute('class')
    if (elementClass.find('red') == -1):
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()

    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
    time.sleep(5)


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

driver.find_element_by_name('username').send_keys('nickname')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_xpath('//button').submit()
time.sleep(5)
like_by_tag('осень')







