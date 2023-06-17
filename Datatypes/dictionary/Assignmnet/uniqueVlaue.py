#print unique value

SampleData = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
              {"V":"S009"}, {"VIII":"S007"}]
#print(SampleData)
dataSet= set()
for i in SampleData:
    for i in i.values():
        dataSet.add(i)

print(dataSet)




#anotheer method

# u=[]
# dataSet= set()
# for i in SampleData:
#     print(i.values())
#     print(list(i.values()))
#     u.extend(list(i.values()))
#
# print(u)
# u=set(u)
# print(u)
