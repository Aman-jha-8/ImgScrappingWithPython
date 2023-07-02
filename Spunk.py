import urllib.request
import requests
from bs4 import BeautifulSoup
import os

#Amazon url -----------------------------------------------------------

url = 'https://www.amazon.com/s?k=mobile+phone&crid=3FKN4OJK8DOBO&sprefix=mobile+ph%2Caps%2C5409&ref=nb_sb_noss_2'

# Make the request
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)

# Read the HTML content
html_content = response.read()

# Parse the HTML content
page_soup = BeautifulSoup(html_content, 'html.parser')

div_element = page_soup.select('div.s-product-image-container')

img_tag=div_element[3].find('img')
image_url=img_tag['src']
folder_name = 'mobile_phone_images'
response=requests.get(image_url)
os.makedirs(folder_name, exist_ok=True)
image_name = image_url.split('/')[-1]
with open(os.path.join(folder_name, image_name), 'wb') as f:
    f.write(response.content)
    print(f'Saved image: {image_name}')

#snapdeal url-----------------------------------------------------------------------

url='https://www.snapdeal.com/search?keyword=phone&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'

# Make the request
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)

# Read the HTML content
html_content = response.read()

page_snap_soup=BeautifulSoup(html_content,'html.parser')

div_element=page_snap_soup.select('div.product-tuple-image ')
img_tag_snap=div_element[2].find('img')
image_url_snap=img_tag_snap['src']
image_name = image_url_snap.split('/')[-1]
response=requests.get(image_url_snap)
with open(os.path.join(folder_name, image_name), 'wb') as f:
    f.write(response.content)
    print(f'Saved image: {image_name}')


