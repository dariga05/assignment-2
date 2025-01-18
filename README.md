# Project: Selenium Automation Tasks

This repository contains multiple automation tasks using **Selenium** WebDriver. Below are the tasks with descriptions, code, and video demonstrations for each one.

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


