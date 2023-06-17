dict1 = {1: ["Amritha", 21, 'Data Structures'],
        2: ["Veda", 20, 'Machine Learning'],
        3: ["Lakshmi", 21, 'java'],
        }
print(dict1.values())
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
for i in dict1.values():
       print( '{:<10} {:<10} {:<10}'.format(i[0], i[1], i[2]))






#>>> '{1} {0}'.format('Python', 'Format')
#'Format Python'

