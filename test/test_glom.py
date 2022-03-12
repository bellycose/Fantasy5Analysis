import json
from glom import glom

data = {'a':{'b':{'c':'d'}}}
result=glom(data, 'a.b.c')
print(result)

target = {'a':{'b':[{'c':'d'},{'c':'e'}]}}
spec=(('a.b',['c']))
print(glom(target,spec))

target ={'a':
         {'b':
          [{'name':'earth','moons':1},
           {'name':'jupiter','moons':69}
           ]
          }
         }
print(glom(target,('a.b',['name'])))
spec={'name':('a.b',['name']),'moons':('a.b',['moons'])}
print(glom(target,spec))

#ANSWER
'''
d
['d', 'e']
['earth', 'jupiter']
{'name': ['earth', 'jupiter'], 'moons': [1, 69]}
'''
