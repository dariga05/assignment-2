TASK - 1
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
This Python script uses Selenium to automate the process of searching for a "makeup tutorial" on YouTube. The script opens the YouTube website, inputs a search query, and verifies that the search results are displayed.
