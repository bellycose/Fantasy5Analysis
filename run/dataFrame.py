import sys
pathway='D:\Programming\Portfolio\Project 2 - API Web Scrape\JSON data'
import json
from glom import glom
import pandas as pd

#selected data and table assembly

def table():

    df = pd.DataFrame()
    
    for i in range(1,10): #Originally 11
        with open(f'{pathway}\calls_{i}.json','r') as json_file:
            data = json.load(json_file)

            specsA=('PreviousDraws',['DrawNumber'])
            draw=((glom(data,specsA)))#list type
            df['DrawNumbers'] = draw
            
            for j in range(0,5):
                specsB=('PreviousDraws',['WinningNumbers'],[f'{j}'],['Number'])
                number=(glom(data,specsB)) #list type
                df[f'Index{j}'] = number

        df.to_excel(f"file{i}.xlsx", index=False)

table()
