#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:49:39 2019

@author: manzars
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.vnci.nl/over-vnci/overzicht-leden?startwith="
req = requests.get(url + 'A')

soup = BeautifulSoup(req.text, 'lxml')
div = soup.findAll('div', {'class': 'organisation-item'})

alpha = []
for i in range(65, 91):
    alpha.append(chr(i))

f = open('assignment.csv', 'w')
header = "Company Name, Phone, Email, Website\n"
f.write(header)
    
for alp in alpha:
    url = "https://www.vnci.nl/over-vnci/overzicht-leden?startwith=" + str(alp)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    div = soup.findAll('div', {'class': 'organisation-item'})
    for ins_div in div:
        name = ins_div.h3.text
        name = name.replace('\r\n', '').replace('            ', '').replace('        ', '')
        #print(name)
        para = ins_div.findAll('div', {'class': 'phone'})
        phone = para[0].a.text.replace('\r\n', '').replace('                            ', '').replace('                        ', '')
        if('0' not in phone):
            phone = 'NaN'
        #print(phone)
        
        para = ins_div.findAll('div', {'class': 'email'})
        email = para[0].a.text
        if('@' not in email):
            email = 'NaN'
        #print(email)
        website = para[1].a.text
        if('www' not in website):
            website = 'NaN'
        print(website)
        f.write(name.replace(',', '') + ',' + phone.replace(',', '') + ',' + email.replace(',', '') + ',' + website.replace(',', '') + '\n' )

f.close()        
import pandas as pd
f = pd.read_csv('assignment.csv')