from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getCountries(country_name):
    try:
        html = urlopen('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2')
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
        country_flag_list = []
        countriesFlagsList = bsObj.find('table').findAll('img',{'class':'thumbborder'})
        for flag in countriesFlagsList:
            country_flag_list.append(flag.attrs['src'][2:])
        countriesNamesFull = bsObj.find('table').findAll('tr')
        country_name_list = []
        for i in range(1,len(countriesNamesFull)):
            countryName = bsObj.find('table').findAll('tr')[i].findAll('td')[2].find('a').get_text()
            country_name_list.append(countryName)
        full_country_name_list = []
        for i in range(1,len(countriesNamesFull)):
            countryNameFull = bsObj.find('table').findAll('tr')[i].findAll('td')[3].get_text()
            full_country_name_list.append(countryNameFull.rstrip())
        country_info_list = []
        for i in range(0,len(countriesNamesFull)-1):
            country_info_list.append({'country':country_name_list[i],'full_country_name':full_country_name_list[i],'same_letter_count':0,'flag_url':country_flag_list[i]})
        same_letter_count_list = []
        letter_count = 0
        for i in range(1040,1072):
            for word in country_name_list:
                if word.startswith(chr(i)):
                    letter_count += 1
            same_letter_count_list.append({chr(i):letter_count})
            letter_count = 0
        print(same_letter_count_list)
        for letter in same_letter_count_list:
            for country in country_info_list:
                if country['country'].startswith(''.join(map(str, letter.keys()))):
                    country['same_letter_count'] = int(''.join(map(str, letter.values())))
        full_country_name_words = []
        for country in full_country_name_list:
            full_country_name_words.append({'words':country.count(' ')+1,'full_country_name':country})
        print(full_country_name_words)
        print(country_info_list)
        if country_name:
            for country_name_dict in  country_info_list:
                if country_name == country_name_dict['country']:
                    return country_name_dict
    except AttributeError as e:
        return None

country_info = getCountries('Австралия')

if country_info == None:
    print("Country could not be found!")
else:
    print("[{country : %s,\nfull_country_name : %s,\nsame_letter_count : %s,\nflag_url : %s}]"%(country_info['country'],country_info['full_country_name'],country_info['same_letter_count'],country_info['flag_url']))