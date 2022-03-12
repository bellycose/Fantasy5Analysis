import sys
pathway='D:\Programming\Portfolio\Project 2 - API Web Scrape\JSON data'
import json
import pandas as pd
from glom import glom


def lastTable():

    df = pd.DataFrame()

    target = f'{pathway}\calls_10.json'
    with open(target,'r') as f:
        data = json.load(f)

        specsA=('PreviousDraws',['DrawNumber'])
        draw=(glom(data,specsA)) 
        df['DrawNumbers'] = draw

        for j in range(0,5):
            specsB=('PreviousDraws',['WinningNumbers'],[f'{j}'],['Number'])
            number=(glom(data,specsB))  
            df[f'Index{j}'] = number

    return df.to_csv("file10.csv", index=False)

lastTable()
