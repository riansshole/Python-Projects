from selenium import webdriver
import time
import pyautogui

driver=webdriver.Chrome()

driver.get("play.slamtoken.com")
search = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/a/button").click()