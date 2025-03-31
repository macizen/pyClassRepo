import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# chrome options for chromedriver
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

webdriver_path = 'chromedriver-mac-arm64/chromedriver'
# init chromedriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# url for scraping
url = "https://www.smallslive.com/search/archive/"
driver.get(url)

# selenium automation to load all the necessary elements
try:
    # wait for page to load
    WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.event-display"))
    )

    # filter search bar to show piano results only
    search_bar = driver.find_element(By.ID, "desktop-search-bar")
    search_bar.send_keys("piano")
    time.sleep(1)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(1)

    # i needed this so that the script would know when to stop clicking the "show more" button
    previous_articles_count = len(driver.find_elements(By.CSS_SELECTOR, "article.event-display"))

    while True:
        # start by scrolling to the bottom 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)  
        try:
            # find show more button
            show_more_div = driver.find_element(By.XPATH, "//div[@data-callback-name='searchMoreArtists']")
            if show_more_div.is_displayed():                
                # click and wait 
                driver.execute_script("arguments[0].click();", show_more_div)
                time.sleep(1.5)  

                # keep tab of how many articles (the containers of the images i'm scraping) there are
                # if there are no new articles, break the loop and move on
                current_articles_count = len(driver.find_elements(By.CSS_SELECTOR, "article.event-display"))
                if current_articles_count <= previous_articles_count:
                    break
                previous_articles_count = current_articles_count
        except Exception as e:
            print(e)
            break

    # store info from page after rendering everything
    page_source = driver.page_source

finally:
    driver.quit()

# now time for scraping!!
from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'html.parser')

# all the images are stored in these elements with the same class
artist_articles = soup.find_all('article', class_='event-display')

# var to store unique urls
unique_image_urls = set()

# dir to download images
image_dir = "artist_img"
os.makedirs(image_dir, exist_ok=True)

# iterate through all the containers w images
for article in artist_articles:
    # the html/css uses aria-labels to identify the elements, so i'm them to get only the images i'm looking for 
    if article and 'aria-label' in article.a.attrs:
        aria_label = article.a['aria-label']
        
        if 'piano' in aria_label.lower():            
            img_element = article.find('img', src=True)

            if img_element:
                img_url = img_element['src']

                # fix for relative urls
                if not img_url.startswith(('http://', 'https://')):
                    img_url = "https://www.smallslive.com" + img_url
                
                unique_image_urls.add(img_url)

for img_url in unique_image_urls:
    # make filename and path to dowload images
    filename = os.path.basename(img_url)
    file_path = os.path.join(image_dir, filename)

    if not os.path.exists(file_path):
        try:
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            with open(file_path, 'wb') as f:
                f.write(img_response.content)
        except Exception as e:
            print(e)

# lmk when its done
print('images downloaded')