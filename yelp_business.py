from bs4 import BeautifulSoup
from parser import simple_get

# raw_html = open('test.html').read()

raw_html = simple_get('https://www.yelp.com/biz/jacks-prime-san-mateo-4?osq=burger')
print("done")
html = BeautifulSoup(raw_html, 'html.parser')

class Business():
    pass 



    






















