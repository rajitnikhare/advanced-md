'''
Created on Jan 11, 2019

@author: Rajit
'''
import requests
import json

def githubToJasonJob():
    print(">>>>>>>>>>Downloading JSON from GitHub>>>>>>>>>>")
    
    r1 = requests.get('https://api.github.com/repos/pandas-dev/pandas/stats/participation')
    r2 = requests.get('https://api.github.com/repos/pandas-dev/pandas/stats/punch_card')
    
    data1 = r1.json();
    data2 = r2.json();
    try:
        with open('participation.json', 'w') as f:
            json.dump(data1, f)
        with open('punch_card.json', 'w') as f:
            json.dump(data2, f)    
    except Exception as err:
        print("Error occurred in downloading JSON file from GITHUB",str(err))
        return False
    print(">>>>>>>>>>Downloading JSON from GitHub complete>>>>>>>>>>")
    return True