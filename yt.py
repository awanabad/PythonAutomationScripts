#! python3 
import sys
from selenium import webdriver

# waiting for the page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.youtube.com/')


if sys.argv[1] == 'p':
    searchTerm = ' '.join(sys.argv[2:])
    driver.get('https://www.youtube.com/results?search_query=' + searchTerm)

    try:
        firstResult = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')))
        firstResult.click()
    except TimeoutException:
        print("The browser took too long to load.")


else:
    searchTerm = ' '.join(sys.argv[1:])
    driver.get('https://www.youtube.com/results?search_query=' + searchTerm)