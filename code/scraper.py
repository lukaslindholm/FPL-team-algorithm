from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import shutil
from pathlib import Path

#open the site
driver = webdriver.Firefox()
driver.get(url = 'https://fplform.com/export-fpl-form-data')
time.sleep(3)

#select and click the right amount of columns for the data
column_selection_button = driver.find_element(By.ID, 'extra')
column_selection_button.click()

#find and click the button to download the data
download_button = driver.find_element(By.ID, 'submit')
download_button.click()

#close the browser
driver.quit()
time.sleep(3)

#get path to downloaded file
downloads_path = str(Path.home() / 'Downloads' / 'fpl-form-predicted-points.csv')
path_to_remove = str(Path.cwd() / 'fpl-form-predicted-points.csv') #get path to old data in the project
#delete the old data if it exists
if os.path.exists(path_to_remove):
    os.remove(path_to_remove)
#move the downloaded to the current directory
shutil.move(downloads_path, Path.cwd())
