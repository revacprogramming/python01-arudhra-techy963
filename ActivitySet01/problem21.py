#3rd networking

import urllib
from bs4 import  BeautifulSoup 
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')