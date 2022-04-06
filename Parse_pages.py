import os
from bs4 import BeautifulSoup
import re
import pandas as pd


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

bd = pd.DataFrame(columns=['name','address', 'e-mail','site', 'telephone'])

for root, dirs, files in os.walk('.'):
    iter = 0
    files.sort(key=natural_keys)
    for name in files:
        fullname = os.path.join(root, name)
        if os.path.isfile(fullname) and (
                re.search(r'.html', fullname)):
            print(fullname)
            with open(fullname, encoding='utf-8', errors='ignore') as fp:
                iter += 1
                soup = BeautifulSoup(fp, "html5lib")

                name = None
                if soup.find('h1', {'class': '_3a1XQ88S'}):
                    name = soup.find('h1', {'class': '_3a1XQ88S'}).text

                address = None
                if soup.find('span', {'class': '_2saB_OSe'}):
                    address = soup.find('span', {'class': '_2saB_OSe'}).text

                site = None
                if soup.find_all('a', {'class': '_2wKz--mA _27M8V6YV'}).__len__() > 1:
                    site = soup.find_all('a', {'class': '_2wKz--mA _27M8V6YV'})[1]
                    site = site.get('href')
                    # print(site)

                email = None
                if soup.find('span', {'class': 'ui_icon email _3ZW3afUk'}):
                    email1 = soup.find('span', {'class': 'ui_icon email _3ZW3afUk'})
                    email = email1.find_parent('a').get('href')
                    # print(email)

                telephone = None
                if soup.find('span', {'class': 'ui_icon phone _3ZW3afUk'}):
                    telephone1 = soup.find('span', {'class': 'ui_icon phone _3ZW3afUk'})
                    telephone = telephone1.find_parent('a').get('href')
                    # print(telephone)

                bd = bd.append({'name': name, 'address': address, 'e_mail': email, 'site': site, 'telephone':telephone}, ignore_index=True)
        bd.to_csv('Tripadvisor_Bermigham' + '.csv', sep=';')
bd.to_csv('Tripadvisor_Bermingham' + '.csv', sep=';')