# f=open('test1','r')
# #print(f.read())
#
# print(f.read(8))

# print(f.readline())
# print(f.readline())

# for i in f:
#     print(i)
#
# f.close()
#append will append content to end of file

# f=open('test1','a')
# f.write('python is a oop')
# f.close()
#
# f=open('test1','r')
# print(f.read())
# f.close()


#write() overwrites existing file
# f=open('test1','w')
# f.write('python is a oop')
# f.close()

# f=open('test1','r')
# print(f.read())
# f.close()

#seek() method
# f=open('test1','r')
# f.seek(4)
# print(f.read())
# f.close()

#tell() - get current file position
#fileobject.tell()

# f=open('test1','r')
# f.readline() #to change position
# pos=f.tell()
# f.close()
# print('Position is:: ', pos)

# def file_read(fna):
#     with open(fna) as f:  # with open(fna) >> by default read fna as read mode and close after operation
#                           # as f >> provide alias name to fna
#         output_list=f.readlines()
#
#     print(output_list)
#
# file_read('test1')

#copyfile() method to copy one file to another, creates new copy
# from shutil import copyfile
# copyfile('test1','test2')

#normal method to count each word in a string
# str1 = 'cat rat mat cat pat rancat sat cat sat'
# print(str1)
# lst=str1.split(" ")
# d={}
# for i in lst:
#     if i in d:
#        d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)



f=open('test','r')
dic={}
for i in f:
    v = i.split(' ')
    for j in v:
        if j not in dic:
            dic[j]=1
        else:
            dic[j] += 1
print(dic)



