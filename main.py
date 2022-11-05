"""
Author: Miloš Bokšan
Date and time of creation: 22.10.2022 19:22

This autofill script was used practically to quickly fill out a form on a real webpage.
The names and values have been replaced with imaginary ones to hide personal information that was included originally
The script does not work as is. It is only for demonstration purposes.

Dependency: chromedriver.exe
Download URL: https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/
Browser type and version (at the time of writing): Google Chrome 107.0.5304.62

Instructions:
1. Run the script
2. Paste in the target url
3. When you press "SPACE" the script attempts to fill in the form.
   If the page is not accessible, it returns a message.
   If it is accesible it performs the task.
4. This can be repeated by pressing "SPACE" again.
5. When you press "ESC" the scrip exits.
"""

import os
import time
from pynput.keyboard import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def formfill():
    # Initialise data dictionary
    working_data = {"website": input("Paste in URL: "), "no_page": 0, "ssn": "1234567890123",
                    "email": "email@email.com", "name": "Name", "surname": "Surname", "date": "22.02.2022.",
                    "phone": "+11234541227157"}

    # Initialise browser and target page
    path = os.getcwd().replace("\\", "\\\\") + "\\chromedriver.exe"
    browser = webdriver.Chrome(path)
    browser.get(working_data["website"])
    browser.maximize_window()
    time.sleep(0.5)

    if working_data["no_page"] == 0:
        try:
            # First page execution
            form_radio_button = browser.find_element(By.XPATH, value="/html/body/div/main/div[4]/div[2]/div[1]/label")
            form_radio_button.click()
            confirm = browser.find_element(By.XPATH, value="/html/body/div/main/div[4]/button")
            confirm.click()

            # Second page exectution
            time.sleep(0.2)
            form_field1 = browser.find_element(By.ID, "j1m4b5g6")
            form_field1.send_keys(working_data["ssn"])
            form_field2 = browser.find_element(By.ID, "email")
            form_field2.send_keys(working_data["email"])
            form_name = browser.find_element(By.ID, "name2")
            form_name.send_keys(working_data["name"])
            form_surname = browser.find_element(By.ID, "surname2")
            form_surname.send_keys(working_data["surname"])
            form_dropdown = browser.find_element(By.XPATH, value="//*[@id='employeer']/option[3]")
            form_dropdown.click()
            form_date = browser.find_element(By.ID, "birthdate")
            form_date.send_keys(working_data["date"])
            form_phone = browser.find_element(By.ID, "cell321Number996")
            form_phone.send_keys(working_data["phone"])
            form_captcha = browser.find_element(By.XPATH, value="/html/body/div[1]/main/div[10]/form/div/div/div/input")
            form_captcha.send_keys("a")
            form_captcha.send_keys(Keys.BACKSPACE)

            time.sleep(15)
            browser.quit()

        # If website cannot be resolved or the form isnt up yet, throws exception
        except Exception as e:
            print(f"Raised exception: {e}.")
            print("Website not open yet...")
            working_data["no_page"] = 1

    # If an exception was thrown earlier close the browser
    else:
        browser.quit()


# Action on SPACE keypress
def press_on(key):
    if key == Key.space:
        formfill()


# Action on ESC keypress
def press_off(key):
    if key == Key.esc:
        return False


def main():
    with Listener(on_press=press_on, on_release=press_off) as listener:
        listener.join()


if __name__ == "__main__":
    main()
