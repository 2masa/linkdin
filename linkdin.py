from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
ACCOUNT="ENTER YOUR EMAIL"
PASSWORD="ENTER YOUR  PASSWORD"
PHONE="ENTER YOUR NUMBER"
chrome_driver_path="/home/ibrahim/work/development/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(2)
sign_in_button=driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_button.click()
time.sleep(5)
email_field=driver.find_element(By.ID,"username")
email_field.send_keys(ACCOUNT)
password_email=driver.find_element(By.ID,"password")
password_email.send_keys(PASSWORD)
password_email.send_keys(Keys.ENTER)
time.sleep(5)
all_listing=driver.find_elements(By.CLASS_NAME,"job-card-container--clickable")
for list1 in all_listing:
    print("called")
    list1.click()
    time.sleep(2)
    try:
        apply_button=driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        phone=driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
        if phone=="":
            phone.send_keys(PHONE)
        submit_button=driver.find_element(By.CSS_SELECTOR,"footer button")
        if submit_button.get_attribute("data-control-name")=="continue_unify":
            close_button=driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            print("Complex application,skipped")
            continue
        else:
            submit_button.click()
        time.sleep(2)
        close_button=driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button,skipped")
        continue
time.sleep(5)
driver.quit()