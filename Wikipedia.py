# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:42:26 2018

@author: Beheerder
"""

import requests
import json

article = input("What subject do you like?").strip().replace(" ", "_")

language = ["en", "nl", "es"]

for item in language:
    url = f"https://{item}.wikipedia.org/api/rest_v1/page/summary/{article}"

    req = requests.get(url)
    
    status = int(req.status_code)
    
    if status != 200:
    	print("Error server not found")
    	exit()
    
    else: 
        print(f'\nSome information about the subject {article}.')
    
    data= json.loads(req.text)
        
    print(f'The title of the article:{data["title"]}\n')
    print(f'The extract:\n{data["extract"]}\n')
    
    if "description" not in data:
        print("Description doesn't exist")    	
    
    else:
        print(f'The description:\n{data["description"]}\n')
