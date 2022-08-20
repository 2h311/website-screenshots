'''
TODO: write a bash script to automate this
/usr/bin/google-chrome --remote-debugging-port=9222 --new-window https://google.com --user-data-dir=./selenium/ChromeProfile
'''

import re
import time
from pathlib import Path

from Screenshot import Screenshot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

images_folder = Path(Path.cwd(), 'images')
if not images_folder.exists():
	images_folder.mkdir()


def get_file_content(file: str):
	filename = file if file else input("\aEnter a valid filename: ")
	
	if (path_object := Path(filename)).exists():
		with path_object.open() as file_handler:
			content = [ line.strip() for line in file_handler.readlines() ]
	else:
		content = list()

	return content	


def get_chromedriver_object():
	chrome_options = Options()
	# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
	chromedriver_path = Path('driver') / Path('chromedriver')
	return webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)


# read in urls from txt file
urls = get_file_content('urls.txt')
url = urls[5]

driver = get_chromedriver_object()
driver.get(url)

# def make_filename_with_timestamp(url: str, separator: str = '|'):

separator: str = '|'
timestamp = time.time()
domain = re.search('(\w{3}.)(\w+.\w+)', url).groups()[1]
screenshot_name = f"{domain}{separator}{timestamp}.png"
dict_ = {
	'title_of_the_website': driver.title,
	'screenshot_url': screenshot_name,
	'timestamp': timestamp,
	'website_url': url,
}
print(dict_)



# screenshot_object = Screenshot.Screenshot()
# img_url = screenshot_object.full_Screenshot(driver, save_path=images_folder.name, image_name='Myimage.png', multi_images=True)

# print(img_url)