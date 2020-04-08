import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.subito.it/audio-video/eragon-pistoia-334066663.htm").text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

price = soup.find('h4', {'class' : 'Atoms__TextAtom--sbt-text-atom-L2hvbWUv Atoms__TextAtom--token-h4-L2hvbWUv size-normal Atoms__TextAtom--weight-semibold-L2hvbWUv AdElements__ItemPrice--price-L2hvbWUv'})

print(price.text)