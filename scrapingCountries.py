from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from collections import Counter
def getCountries(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
        # print(bsObj)
        # countriesNamesFull = bsObj.findAll('a',{'class': 'image'}).parents.parents.next_siblings.next_sibling.get_text()
        # for nameFull in countriesNamesFull:
        #     print(nameFull)
        countriesFlagsList = bsObj.findAll('img',{'class':'thumbborder'})
        for flag in countriesFlagsList:
            print(flag.attrs['src'])
        countriesNames = bsObj.findAll('a', {'class': 'image'})
        for name in countriesNames:
            print(name.attrs['title'])
    except AttributeError as e:
        return None
    # return title

title = getCountries('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2')
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)