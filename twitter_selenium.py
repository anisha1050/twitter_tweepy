from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r"C:\projects\learning\chromedriver.exe"
# Access to Twitter
url    = r'https://twitter.com/AndrewYNg/status/1290029141522173952?s=20'
driver = webdriver.Chrome(chrome_path)
driver.get(url)
driver.maximize_window()

login_xpath  =  '/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[1]/a'
login_element= driver.find_element_by_xpath(login_xpath)
login_element.click()


email_xpath        = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath     = "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input"
login_button_xpath = "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div"

email_element        = driver.find_element_by_xpath(email_xpath)
password_element     = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

print("Element is visible? " + str(email_element.is_displayed()))

email_element.send_keys('XXXXXXXXX')
password_element.send_keys('XXXXXXXXXXXX')
login_button_element.click()

print(driver.title)

elem = driver.find_element_by_tag_name("body")
len(elem)
no_of_pagedowns = 10

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

twitter_elm = driver.find_elements_by_class_name("tweet")
len(twitter_elm)
for post in twitter_elm:
    username = post.find_elements_by_class_name("username")
    print(username.text)
    if username.text.lower() == "@" + 'AndrewYNg'.lower():
        tweet = post.find_element_by_class_name("tweet-text")
        print(tweet.text)

reply_1_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[6]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/span'
reply_2_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[8]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div'

reply_1_element = driver.find_element_by_xpath(reply_1_xpath)
reply_1_element.text
reply_2_element = driver.find_element_by_xpath(reply_2_xpath)
reply_2_element.text

