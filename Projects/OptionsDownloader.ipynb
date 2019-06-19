import time
start = time.time() 
# end = time.time()
#print(end - start)
import re
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # determine the download location
from selenium.webdriver.common.keys import Keys # import special keys like RETURN
from selenium.webdriver.support.select import Select  # need Select class for dropdown menu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait           #  for file upload
from selenium.webdriver.support import expected_conditions as EC  # for file upload 
import os   # get the current working directory etc. 

#-----------------------------------------------------------------
#  determine the download location
#-----------------------------------------------------------------
downloadLocation = os.getcwd()
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory":  downloadLocation,
  "download.prompt_for_download": True,
  "download.directory_upgrade":   True,
  "safebrowsing.enabled": True
})
#-----------------------------------------------------------------
# while running show no verbose log
# valid args: INFO = 0,WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3

chrome_options.add_argument("headless")
#-----------------------------------------------------------------
chrome_options.add_argument('log-level=3')
# in the above lines we define the options we want for the chrome 
# now we start the driver with the above options
driver = webdriver.Chrome(chrome_options=chrome_options)
#-----------------------------------------------------------------
#  allow download in the headless mode
#-----------------------------------------------------------------
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': downloadLocation}}
command_result = driver.execute("send_command", params)

f = open("ariva_list.txt","r")
lines = f.readlines()  # need to read line by lineL
print("########################################################")
print(" options downloader    |     contact: Me@corporate.com")
print("########################################################")
k = 0  # counter for the number of shares to be downloaded    
for line in lines:
    k += 1
    line = line.strip('\n')
    print(f"{k}. File: please wait while downloading {line}...")
    url = 'https://www.ariva.de/'+line+'/historische_kurse'
    driver.get(url)
    time.sleep(0.5)
    body = driver.find_element_by_css_selector('body')
    # zoom out to control the download button
    #driver.execute_script("document.body.style.zoom='60%'")
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    #driver.implicitly_wait(2)
    DOWNLOAD_BUTTON_XPATH = '//input[@type="submit" and @value="Download"]'
    button = driver.find_element_by_xpath(DOWNLOAD_BUTTON_XPATH)
    time.sleep(0.5)
    button.click()

end = time.time()
print(f"\n Final Report:\n{k} shares heruntergeladen in {(end - start)/60:.2} Minuten")
print("*****************************************************************")
input("Press Enter to continue...")
