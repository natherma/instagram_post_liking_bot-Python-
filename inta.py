# this Code may not work if Instagram changed there sourceCode
# max 21 posts can be liked by this instagram liking bot
# this python code will only work if Selenium and chrome driver are installed

# importing selenium other required tools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Source Code
# Enter a proper username
un = input("Enter a instagram Username\n")
# Enter Password
psw = input("Enter password\n")
# Enter the username of other user whose post you want to like
other = input("Enter exact username of other Instagram user\n")

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
sleep(3)
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
submit = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
username.send_keys(un)
password.send_keys(psw)
sleep(3)
submit.click()
sleep(3)
ok = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
ok.click()
sleep(2)
ok2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
ok2.click()

instasearch = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
instasearch.send_keys(other)
sleep(2)
other_username = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div')
other_username.click()
sleep(3.5)
for x in range(1, 8):
   for y in range(1, 4):
        post = driver.find_element_by_xpath(f'//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[{x}]/div[{y}]/a/div/div[2]')
        post.click()
        sleep(3)
        like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like.click()
        sleep(1.5)
        back = driver.find_element_by_xpath('/html/body/div[5]/div[3]/button')
        back.click()
        sleep(1.5)

