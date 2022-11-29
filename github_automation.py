from selenium import webdriver
import time
import logindata
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Users/SKCT/Desktop/Project/freelancing/Python/Automation/chromedriver/chromedriver.exe', chrome_options=options)
time.sleep(1)

driver.get('http://www.github.com')
time.sleep(3)

#find the element
continue_link = driver.find_element(By.LINK_TEXT, 'Sign in')

#use click function
continue_link.click()
time.sleep(3)

if driver.find_element(By.NAME, 'login'):
    pass
else:
    time.sleep(2)
    

login = driver.find_element(By.NAME, "login")
password = driver.find_element(By.NAME, "password")
time.sleep(0.5)

login.send_keys('''your github email or user name''')
time.sleep(1)

password.send_keys('''your github password''')
time.sleep(1)

button = driver.find_element(By.NAME, 'commit')
button.click()
time.sleep(2)

#create a repository
new_repository = driver.find_element(By.LINK_TEXT, 'New')
new_repository.click()
time.sleep(2)

repository_name = driver.find_element(By.ID, 'repository_name')
repository_name.send_keys('github_automation v.1')
time.sleep(2)

repository_description = driver.find_element(By.ID, 'repository_description')
repository_description.send_keys('Github Automation using Python and Selenium')
time.sleep(2)

repository_auto_init = driver.find_element(By.ID, 'repository_auto_init')
repository_auto_init.click()
time.sleep(2)

create_repo_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.btn')
create_repo_button.click()
time.sleep(2)

                                    
