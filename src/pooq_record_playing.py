#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
import sys
import random
import threading
import glob
import cv2

pooq_login_url = "https://www.pooq.co.kr/member/login.html?referer=https%3A%2F%2Fwww.pooq.co.kr%2Findex.html"
pooq_content_url_superman = "http://www.pooq.co.kr/player/vod.html?programid=K02_T2005-0230_2&contentid=K02_PS-2019007539-01-000.2"
pooq_content_url_livealone = "https://www.pooq.co.kr/player/vod.html?programid=M_1002831100000100000&contentid=M_1002831100304100000.1"
pooq_id = sys.argv[1]
pooq_pwd = sys.argv[2]

def take_screenshot(webdriver):
	while True:
		webdriver.save_screenshot("./screenshot/live_alone/"+str(time.time())+".png")


def execute_pooq_service():
	
	## Set Chrome options

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--start-maximized')
	chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
	
	## Execute Chrome
	
	driver = webdriver.Chrome("./linux_chromedriver/chromedriver",chrome_options=chrome_options)

	## Login to Service
	
	driver.get(pooq_login_url)
	time.sleep(random.randint(0, 5))
	elements_list = driver.find_elements_by_class_name('input-style01')
	text_id = elements_list[0]
	text_password = elements_list[1]
	login_button = driver.find_element_by_class_name('btn-purple')
	actions = ActionChains(driver)
	actions.send_keys_to_element(text_id, pooq_id)
	actions.send_keys_to_element(text_password,pooq_pwd)
	actions.click(login_button)
	actions.perform()
	time.sleep(random.randint(0, 5))

	## Go to "superman" / "live alone" page
	driver.get(pooq_content_url_livealone)
	time.sleep(5)
	button_elements	 = driver.find_elements_by_tag_name('button')
	close_btn = ""
	play_btn = ""

	for button in button_elements:
		if button.text == "close":
			close_btn = button
			break

	actions = ActionChains(driver)
	actions.move_to_element(close_btn)
	actions.click()
	actions.perform()
	time.sleep(3)

	button_elements	 = driver.find_elements_by_tag_name('button')
	for button in button_elements:
		if button.text == "play":
			play_btn = button
			break

	## Execute Thread - Take screenshots
	t = threading.Thread(target=take_screenshot, args=(driver,))
	t.daemon = True
	
	actions = ActionChains(driver)
	actions.move_to_element(play_btn)
	actions.click()
	actions.perform()

	t.start()
	
	time.sleep(5)
	driver.quit()


def main():
	if len(sys.argv) < 2:
		print("Input pooq id and password")
		sys.exit(1)
	execute_pooq_service()

if __name__ == "__main__":
	main()