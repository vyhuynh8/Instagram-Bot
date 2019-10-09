from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		# "//a[@href'accounts/login']"
		driver = self.driver

		driver.get("http://www.instagram.com")
		time.sleep(4)

		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(4)

		user_name = driver.find_element_by_xpath("//input[@name='username']")
		user_name.clear()
		user_name.send_keys(self.username)

		password = driver.find_element_by_xpath("//input[@name='password']")
		password.clear()
		password.send_keys(self.password)

		password.send_keys(Keys.RETURN)
		time.sleep(4)


IG = InstagramBot("username", "password")
IG.login()