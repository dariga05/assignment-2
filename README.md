
# Project: Selenium Automation Tasks 

This repository contains multiple automation tasks using **Selenium** WebDriver. Below are the tasks with descriptions, code, and video demonstrations for each one.
(There is a video under each task, please open it in another tab)

## Task 1: YouTube Search Automation

### Description
This script automates the process of searching for a "makeup tutorial" on YouTube. It uses Selenium WebDriver to open the website, input a search query, and verify that the search results are displayed.

### Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def search_youtube():
    driver = webdriver.Edge()  
    
    try:
        driver.get("https://www.youtube.com")
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("makeup tutorial")
        search_box.submit()
        time.sleep(3)
        result_stats = driver.find_element(By.XPATH, "//ytd-video-renderer")
        if result_stats.is_displayed():
            print("Search results displayed successfully.")
    except Exception as e:
        print(e)
    finally:
        driver.quit()

search_youtube()

Video Demonstration
Here is a video demonstrating the task:
https://github.com/user-attachments/assets/e2fec751-12ce-4c2b-8f6a-9bc9a53f0ba2

## Task 2: Twitter Login Automation

### Description
This script automates the process of logging into **jut.su** using **Selenium** WebDriver. The script opens the website, enters login credentials, and verifies successful login by checking for the "Exit" button after login. It then logs out of the website.

### Code
```python
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def twitter_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://jut.su")
        driver.maximize_window()
        time.sleep(3)

        login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Войти']")))
        login_btn.click()

        username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login_input1']")))
        username.send_keys("darigasekerbek")
        time.sleep(3)

        password_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='login_input2']")))
        password_field.send_keys("dariga2005")

        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login_submit']")))
        login_button.click()
        time.sleep(10)

        try:
            exit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='[Выйти]']")))
            print("Вход успешно выполнен!")
        except:
            print("Не удалось войти. Проверьте учетные данные.")

        exit_btn.click()
        time.sleep(2)

        print("Выход успешно выполнен!")
    finally:
        driver.quit()

print()
twitter_login()
print()
Video Demonstration
https://github.com/user-attachments/assets/98ee33cb-7e13-4b51-921e-40e76ad47cc4

## Task 3: Flight Booking Automation

### Description
This script automates the process of booking a flight on the **BlazeDemo** website. It selects departure and destination cities, fills in personal and credit card information, and completes the purchase of a flight. The confirmation message is printed after a successful booking.

### Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://www.blazedemo.com/')
    driver.maximize_window()

    departure_city = driver.find_element(By.NAME, 'fromPort')
    departure_city.send_keys('Boston')

    destination_city = driver.find_element(By.NAME, 'toPort')
    destination_city.send_keys('New York')

    find_flights_button = driver.find_element(By.XPATH, '//input[@value="Find Flights"]')
    find_flights_button.click()

    time.sleep(5)

    select_flight_button = driver.find_element(By.XPATH, '//input[@value="Choose This Flight"]')
    select_flight_button.click()

    time.sleep(5)

    name_field = driver.find_element(By.NAME, 'inputName')
    name_field.send_keys('Dariga Sekerbek')

    address_field = driver.find_element(By.NAME, 'address')
    address_field.send_keys('21000 West 10 Mile Rd')

    city_field = driver.find_element(By.NAME, 'city')
    city_field.send_keys('New York')

    state_field = driver.find_element(By.NAME, 'state')
    state_field.send_keys('NY')

    zip_code_field = driver.find_element(By.NAME, 'zipCode')
    zip_code_field.send_keys('10001')

    credit_card_number_field = driver.find_element(By.NAME, 'creditCardNumber')
    credit_card_number_field.send_keys('1234567890000000')

    credit_card_month_field = driver.find_element(By.NAME, 'creditCardMonth')
    credit_card_month_field.send_keys('07')

    credit_card_year_field = driver.find_element(By.NAME, 'creditCardYear')
    credit_card_year_field.send_keys('2025')

    name_on_card_field = driver.find_element(By.NAME, 'nameOnCard')
    name_on_card_field.send_keys('Dariga Sekerbek')

    purchase_flight_button = driver.find_element(By.XPATH, '//input[@value="Purchase Flight"]')
    purchase_flight_button.click()

    time.sleep(5)

    confirmation_message = driver.find_element(By.XPATH, '//h1')
    print(confirmation_message.text)

finally:
    driver.quit()
Video Demonstration
https://github.com/user-attachments/assets/81861e17-8139-404c-85ca-36154127d3da
