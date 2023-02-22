import urllib.request
from bs4 import BeautifulSoup

# URL of website to scrape
url = "https://www.imdb.com"
# Connect to the URL
response = urllib.request.urlopen(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response, 'html.parser')

# Find all images on the page
img_tags = soup.find_all('img')

# Create directory to save images, 
import os
os.makedirs('images', exist_ok=True)

# Download images and save to directory
for img in img_tags:
    img_url = img['src']
    filename = os.path.join('images', img_url.split('/')[-1])
    urllib.request.urlretrieve(img_url, filename)
