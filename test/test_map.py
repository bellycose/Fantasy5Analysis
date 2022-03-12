import sys
pathway='D:\Programming\Portfolio\Project 2 - API Web Scrape\JSON data'
import json
import pandas as pd
from glom import glom

#Create an empty dataframe
df = pd.DataFrame()

#Selecting Data into List
i=10
target = f'{pathway}\calls_{i}.json'
with open(target,'r') as f:
    data = json.load(f)

    specsA=('PreviousDraws',['DrawNumber'])
    draw=(glom(data,specsA)) #list type
    #print(draw)

    # insert the draw to the dataframe
    df['DrawNumbers'] = draw

    for j in range(0,5):
        specsB=('PreviousDraws',['WinningNumbers'],[f'{j}'],['Number'])
        number=(glom(data,specsB)) #list type
        #print(number)

        # insert each number to the dataframe
        df[f'Index{j}'] = number

#Now assembling lists into a table using pandas
print(df)
