#Author: Dillon Duguid
#Date: 28/09/19
#Test

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from datetime import date
import os
import time

#Enter security message, username, password
Sk = input("Enter security answer")
username_value = input("Enter username")
password_value = input("Enter password")

#Set browser prefernces so statements download to default location
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.preferences.instantApply",True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml")
fp.set_preference("browser.helperApps.alwaysAsk.force",False)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.folderList",0)

#Go to TSB page
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://internetbanking.tsb.co.uk/personal/logon/login/#/login")
time.sleep(3)


#Stage 1: Enter login credentials
#Find page element for username, then enter username
username = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/div/div[1]/input"

driver.find_element_by_xpath(username).send_keys(username_value)

#Find page element for username, then enter password
password = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[2]/div/div[1]/input"
driver.find_element_by_xpath(password).send_keys(password_value)

#Click login button
login = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[4]/div/div[3]/button/span"
driver.find_element_by_xpath(login).click()
time.sleep(2)

#Stage 2: Get security key values based on random number from page
#Read security numbers, get corresponding element from security key, then enter that number in dropdown
first = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div[2]/div[1]/span'
second = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div[2]/div[2]/span'
third = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div[2]/div[3]/span'

num1 = driver.find_element_by_xpath(first).text
num1 = int(num1[10])
num2 = driver.find_element_by_xpath(second).text
num2 = int(num2[10])
num3 = driver.find_element_by_xpath(third).text
num3 = int(num3[10])

box1 = '//*[@id="charXPos"]'
driver.find_element_by_xpath(box1).send_keys(Sk[num1 - 1])
box2 = '//*[@id="charYPos"]'
driver.find_element_by_xpath(box2).send_keys(Sk[num2 - 1])
box3 = '//*[@id="charZPos"]'
driver.find_element_by_xpath(box3).send_keys(Sk[num3 - 1])

#Click secondary login button
final_login = "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/form/div[4]/div/button/span"
driver.find_element_by_xpath(final_login).click()


#stage 3 - get statements
time.sleep(7)
student_account = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div/proteo-ui-account-summary/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/ul/li[1]/a/span[2]'
driver.find_element_by_xpath(student_account).click()

time.sleep(5)
export = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/ui-view/div/div/div[2]/div/div[5]/div/div[1]/proteo-ui-export-statement/a/a/span[2]'
driver.find_element_by_xpath(export).click()

today = date.today()
day = today.strftime("%d")
month = today.strftime("%b")
year = today.strftime("%Y")

time.sleep(0.5)

currentView = '//*[@id="currentView"]'
driver.find_element_by_xpath(currentView).click()

submitExport = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/ui-view/div/div/div[2]/div/div[5]/div/div[1]/proteo-ui-export-statement/form/div/div/div/ng-transclude/div[3]/div/div/div/div[2]/modal-call-back/div/div/button/span'
driver.find_element_by_xpath(submitExport).click()

time.sleep(5)

os.remove("/Users/dillon/Desktop/exportStatements.csv")

accountDropDown = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/div/select'
driver.find_element_by_xpath(accountDropDown).click()
driver.find_element_by_xpath(accountDropDown).send_keys("p")
driver.find_element_by_xpath(accountDropDown).send_keys(u'\ue007')
