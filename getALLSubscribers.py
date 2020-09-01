from selenium import webdriver
import logininfo
import time

browser = webdriver.Firefox(executable_path = "C:\\Users\\hp\\Desktop\\Selenium Python\\geckodriver.exe")

browser.get("https://instagram.com")

time.sleep(4)

username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

username.send_keys(logininfo.my_username)
password.send_keys(logininfo.my_password)

time.sleep(3)

login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
login.click()

time.sleep(3)

not_now = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
not_now.click()

time.sleep(2)
# Not now for notification
not_now_notify = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
not_now_notify.click()

time.sleep(2)

account_button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
account_button.click()

time.sleep(2)

profile = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]")
profile.click()

time.sleep(3)

followers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()

time.sleep(5)

jscommand = """

followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

time.sleep(5)

followersList =[]

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")


for follower in followers:
    followersList.append(follower.text)
    
with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
        

browser.close()
