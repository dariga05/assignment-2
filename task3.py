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
