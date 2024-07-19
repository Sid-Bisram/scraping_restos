import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    URL = "https://www.simplygoodfood.mu/en/list"
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html5lib')
    out_file_path = 'output/site2.html'
    with open(out_file_path, 'w') as file:
        file.write(page.text)