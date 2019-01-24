#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 19:30:07 2019

@author: jan
"""
import json
from bs4 import BeautifulSoup
from requests import get
from time import time
import os

accountList=['alicija.koe','kimjdammer','selinahcok','annkathringotze','melisslana','_yaraline_','lenalswk','celinegntm2019','sophiasky_','catharinamaranca','enisa.bukvic','anthoniagntm2019','chiaragntm','chiara_1808','lucy_m_thomas','anthoniia__','celine.hamann']

baseURL='https://www.instagram.com/'

t = time()

for acc in accountList:
    #print(acc)
    url = str(baseURL)+str(acc)
    soup = BeautifulSoup(get(url).text, 'html.parser')
    
    if os.path.exists(acc+'.csv') == False:
        entry = ['epoch','followers','following','media']
        file=open(acc+".csv", "a")
        row = [str(i) for i in entry]
        file.write(",".join(row) + "\n")
        
    try:
        base = json.loads(soup.find_all('script')[4].text[21:-1])['entry_data']['ProfilePage'][0]['graphql']['user']
        follower_count=base['edge_followed_by']['count']
        following_count = base['edge_follow']['count']
        media_count = base['edge_owner_to_timeline_media']['count']
        #images = base['edge_owner_to_timeline_media']['edges']
        entry = t,follower_count,following_count,media_count
        file=open(acc+".csv", "a")
        row = [str(i) for i in entry]
        file.write(",".join(row) + "\n")
        
        file.close()
    except Exception as e:
        print(e)
        
