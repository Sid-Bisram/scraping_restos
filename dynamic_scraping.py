from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time

timeout = 20
### locators
login_btn_locator = '/html/body/app-root/app-layout/div/div/app-restaurants-new/div[1]/app-header/div[1]/div[1]/div[2]/ul/li[2]/a/i'
email_field_locator = '//*[@id="signinPopup"]/div/div/form[1]/div[1]/app-phone-email-hybrid/form/div/input'
password_field_locator = '//*[@id="siPassword"]'
btn_sign_in_locator = '//*[@id="signinPopup"]/div/div/form[1]/div[4]/button'


def is_element_ready(attribute, locator):
    try:
        element_present = EC.element_to_be_clickable((attribute, locator))
        WebDriverWait(driver, timeout).until(element_present)
        element_object=driver.find_element(attribute, locator)
        print("Element is visible? " + str(element_object.is_displayed()))

        return True,element_object
    except TimeoutException:
        print("Timed out waiting for page to load")
        return False,False

def custom_selector(tag):
	# Return "span" tags with a class name of "target_span"
	return tag.name == "div" and tag.has_attr("class") and "card_right ng-tns-c21-2 ng-star-inserted" in tag.get("class")


def getResponseCode(url):
    conn = urllib.request.urlopen(url)
    return conn.getcode()

if __name__ == "__main__":

    import urllib.request
    
    url_to_scrape = "https://www.simplygoodfood.mu/en/list"
    print("Response code from site: ",getResponseCode(url_to_scrape))

    email     = "******"
    password  = "******"

    service = Service(executable_path=r"C:\Users\reebis\Downloads\chromedriver.exe")
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--dns-prefetch-disable")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url_to_scrape)
    driver.maximize_window()

    try:
        element_present = EC.element_to_be_clickable((By.XPATH, login_btn_locator))

        element_object  = WebDriverWait(driver, timeout).until(element_present)

        driver.execute_script('arguments[0].click()', element_object)
        print("Element is visible? " + str(element_object.is_displayed()))
        print("modal is clicked")

        email_field_present = EC.visibility_of_element_located((By.XPATH,email_field_locator))
        email_field = WebDriverWait(driver, timeout).until(email_field_present)
        if email_field.is_displayed():
            email_field.send_keys(email)
            print("email pasted...")
        else:
            print("email field not visible")

        password_field_present = EC.visibility_of_element_located((By.XPATH, password_field_locator))
        password_field = WebDriverWait(driver, timeout).until(password_field_present)
        if password_field.is_displayed():
            password_field.send_keys(password)
            print("password pasted...")
        else:
            print("email field not visible")

        btn_signin_present = EC.element_to_be_clickable((By.XPATH, btn_sign_in_locator))
        btn_sign = WebDriverWait(driver, timeout).until(btn_signin_present)
        driver.execute_script('arguments[0].click()', btn_sign)
        print("Sign in successful")
        time.sleep(10)

        resto_panels_present = EC.presence_of_element_located((By.XPATH, '//*[@id="listviewscroll"]/div[3]/div[1]/div/div/div[2]/div[1]/p[1]'))
        resto_panels = WebDriverWait(driver,timeout).until(resto_panels_present)
        print(resto_panels.text)


        bottom_panel = driver.find_element(By.XPATH, "//*[@class='footer-container dp-none ng-star-inserted']")
        # if(bottom_panel.is_displayed()):
        #     print("bottom panel found")
        #     driver.execute_script("arguments[0].scrollIntoView();", bottom_panel)
        #     time.sleep(5)

        all_panels = driver.find_elements(By.XPATH, '//p[contains(@class,"card_heading margin")]')



        print(all_panels)
        print(len(all_panels))
        for panel in all_panels:
            print(panel.text)

        restos = []


    except TimeoutException:
        print("Timed out waiting for page to load")


