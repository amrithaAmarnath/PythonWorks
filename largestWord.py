#Write a program to print the largest word from a string without using any built-in-function
st=input("enter a string")
word=""
words=[]
# to split words without built-in function
for i in range(len(st)):
    if st[i] != " ":
        word = word + st[i]
    else:
        words.append(word)
        word=""
words.append(word)
# to find the largest word/words
large = words[0]
l=[]
for i in range(1,len(words)):

    if len(large) < len(words[i]) :
        large = words[i]
        l.append(large)
    else:
        if len(large) == len(words[i]) and large != words[i] :
            l.append(words[i])
print('largest word :',l)



