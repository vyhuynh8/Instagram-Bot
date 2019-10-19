from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver

		driver.get("http://www.instagram.com")
		time.sleep(2)

		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(2)

		user_name = driver.find_element_by_xpath("//input[@name='username']")
		user_name.clear()
		user_name.send_keys(self.username)

		password = driver.find_element_by_xpath("//input[@name='password']")
		password.clear()
		password.send_keys(self.password)

		password.send_keys(Keys.RETURN)
		time.sleep(3)

		notifs_popup = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

	def likeTimeLinePhotos(self):
		driver = self.driver
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		driver.find_element_by_xpath("//button/span[@aria-label='Like']").click()

	def goToPage(self, user_id):
		driver = self.driver
		driver.get("http://www.instagram.com/" + user_id)

	def likeUsersPost(self):
		pic_href = []
		driver = self.driver
		last_height = driver.execute_script("return document.body.scrollHeight")

		while True:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			href = [element.get_attribute("href") for element in driver.find_elements_by_tag_name('a') if "/p/" in element.get_attribute("href")]
			[pic_href.append(hr) for hr in href if hr not in pic_href]

			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height


		num_photos = len(pic_href)

		for pic in pic_href:
			driver.get(pic)
			time.sleep(2)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			time.sleep(random.randint(2,5))
			like = driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
			time.sleep(random.randint(2,4))
			print("Liked: " + pic + " | Photos Remaining: " + str(num_photos))

			num_photos -= 1

		
		print(pic_href)



IG = InstagramBot("username", "password")

try:
	IG.login()
	IG.goToPage("username_2")
	IG.likeUsersPost()
except Exception as e:
	print(e)
	IG.closeBrowser()
