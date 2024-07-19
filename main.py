### Bringing the libraries
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == '__main__':
    extracted = []

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

    URL = "https://restaurants.mu/en/mauritius-restaurants-dining-directory.html"

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    restos = []  # a list to store restaurant informations

    # wait for page to load
    time.sleep(5)

    table = soup.find_all('div', attrs={'class': 'resto container d-none d-md-block'})

    for resto in table:
        resto_details = []
    # soup = BeautifulSoup(current_tag, 'html5lib')
        resto_name = resto.find('a')
        if(resto_name is not None):
            resto_name = resto_name.h3.get_text()
            print("# resto_name: ", resto_name)
            resto_details.append(resto_name)

        location = resto.find(class_='resto-location')

        if(location is not None):
            resto_location = location.get_text()
            print("# resto_location: ",resto_location)
            resto_details.append(resto_location)

        resto_contact_no = resto.find(class_='resto-contact-number')

        if(resto_contact_no is not None):
            resto_contact_no = resto_contact_no.get_text()
            print("# resto_contact_no: ", resto_contact_no)
            resto_details.append(resto_contact_no)
        print("--------------------------------------------------------------")
        extracted.append(resto_details)

    column_names = ['Restaurant_Name', 'Restaurant_Location', 'Restaurant_Contact_No']
    df = pd.DataFrame(columns=column_names,data=extracted)
    df.to_csv(path_or_buf='output/resto_info_v1.csv',encoding='utf-8',index=False)



