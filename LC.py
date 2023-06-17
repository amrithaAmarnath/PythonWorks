"""List Comprehension"""
#Find all of the words in as string that are less than 4 letters
st=input("enter string")
words=st.split(" ")
letters=[x for x in words if len(x) < 4]
print(letters)
