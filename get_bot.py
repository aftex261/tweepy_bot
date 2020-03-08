import requests
import os
from bs4 import BeautifulSoup as bs

link = 'https://www.google.com/search/tech/'

page = requests.get(link)
soup = bs(page.text, 'html.parser')/*For making the html page*/

img_tags = soup.findAll('img')

if not os.path.exists('tech'):
    os.makedirs('tech')/*Creating the directory if not present*/

os.chdir('tech')
x = 0

for image in img_tags:
    try:
        link = image['src']
        source = requests.get(link)
        if source.status_code == 200:
            with open('tech-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(link).content)
                f.close()
                x += 1
    except:
        pass
