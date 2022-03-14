from csv import reader
import statistics
import pandas as pd
import matplotlib as plt
import numpy as np

for i in range(1,11):
    with open(f'D:\Programming\Portfolio\Project 2 - API Web Scrape\CSV data/file{i}.csv', 'r') as read_obj:
        #csv_reader = (read_obj)
        #header = next(csv_reader)
        #if header != None:
        #    for row in csv_reader:
        #        print((row))

        #Dictionary
        #winningcalls = DictReader(read_obj)
        #for call in winningcalls:
            #print(call)

        #list
        #winningcalls = reader(read_obj)
        #header=next(winningcalls)
        #if header != None:
        #    for call in winningcalls:
        #        print(call)
