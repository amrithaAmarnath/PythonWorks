str1 = input("enter string with wild character")
str2 = input("enter string without wild character")
l1 = len(str1)
l2 = len(str2)
l=0
bool="false"
for i in str1:

      if i == '*':
        print(str1[l+1:])
        if str1[l+1:l1] in str2[l+1:l2]:
            bool = "true"
        else:
            bool = "false"
      if i == '?':
        print(str1[l+1:l1])
        print(str2[l + 1:l2])
        if str1[l+1:l1] == str2[l+1:l2]:
            bool = "true"
        else:
            bool = "false"

      l += 1
print(bool)