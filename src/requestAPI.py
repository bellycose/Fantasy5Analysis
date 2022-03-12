import requests as r
import pandas
import json
import os

'''
This file takes the API/JSON data and saves a JSON file for local storage. (Require Code CLean)
'''


def requestAPI():
    
    #If the first attempt does not work, try again.
    s=r.Session()

    #Read each API response, result in a python object
    for i in range(1,11):
        endpoint = f"https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/10/{i}/20"
        response = s.get(endpoint)

        #export a JSON file from each responses in JSON data folder.
            #directory PATH
        target_path='D:\Programming\Portfolio\Project 2 - API Web Scrape\JSON data'
        full_path = os.path.join(target_path, f'calls_{i}.json')
        with open(full_path,'w') as f:
            f.write(str(response.text))
            print(f'A JSON file {i} has been created')
        

requestAPI()
