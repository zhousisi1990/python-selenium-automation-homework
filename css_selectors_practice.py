from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# open the url
# driver.get('https://stackoverflow.com/users/signup')

#find Create your account
#driver.find_element(By.CSS_SELECTOR,'h1.fs-headline1')
driver.find_element(By.XPATH,"//h1[text()='Create your account']")

#find terms of service link
driver.find_element(By.CSS_SELECTOR,"a[name='tos']")

#find privacy policy link
driver.find_element(By.CSS_SELECTOR,"a[name='privacy']")

#find email input
driver.find_element(By.CSS_SELECTOR,"#email")

#find password input
driver.find_element(By.CSS_SELECTOR,"#password")

#find eye icon
driver.find_element(By.CSS_SELECTOR,".js-password svg:not(.d-none)")

#find sign up button
driver.find_element(By.CSS_SELECTOR,"#submit-button")

#find Sign up with Google button
driver.find_element(By.CSS_SELECTOR,"[data-provider='google']")

#find Sign up with Github button
driver.find_element(By.CSS_SELECTOR,"[data-provider='github']")

#find Get Stack Overflow Internal free for up to 50 users link
# driver.find_element(By.CSS_SELECTOR,"[href *= 'teams?']")
driver.find_element(By.XPATH,"//a[contains(text(),'50 users')]")