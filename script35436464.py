import re
from selenium import webdriver
import time

url = input("Enter URL to monitor: ")
text_to_check = "(E|e)mir"
ignore_text = "(D|d)emir"

driver = webdriver.Chrome()
driver.get(url)

while True:
    page_source = driver.page_source
    if re.search(text_to_check, page_source) and not re.search(ignore_text, page_source):
        print("bulundu!")
        with open("isimler.txt", "a") as f:
            f.write(re.findall(text_to_check, page_source)[0] + "\n")

    time.sleep(0.25)
