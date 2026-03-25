from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import keyboard
from keyboard import press
from selenium.common.exceptions import NoSuchElementException

df = pd.read_csv('San_Diego_Non_Profits_EIN.csv') 
df['EIN'] = df['EIN'].astype(str)
df['EIN'] = df['EIN'].str.replace(".0","")
df['EIN'] = df['EIN'].str.zfill(9)


for i in range(967, 7518):

    ein = df['EIN'][i]
        
    try: 
        driver = webdriver.Firefox()
        driver.get("https://apps.irs.gov/app/eos/")
        driver.find_element(By.CSS_SELECTOR,"#einTerm").send_keys(ein)
        driver.find_element(By.CSS_SELECTOR,"button.border-2:nth-child(2)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"a.focus\:focus\:ring-2").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#returnsAccordion-0-accordionButton > svg:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#returnsAccordion-0-accordionBody > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > a:nth-child(2)").click()
        time.sleep(2)

        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        driver.find_element(By.CSS_SELECTOR,"#downloadButton").click()

        time.sleep(2)
        keyboard.press('enter')
        keyboard.release('enter')

        time.sleep(10)
        driver.quit()

    except NoSuchElementException:
        driver.quit()








