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
