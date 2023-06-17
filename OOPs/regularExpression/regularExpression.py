"""
Regular expression:
-The regex or regexp or regular expression is a sequence of different characters
 which describe the particular search pattern.
-It is also referred/called as a Rational expression.
-It is mainly used for searching and manipulating text strings.
-In simple words, you can easily search the pattern and replace
them with the matching pattern with the help of regular expression.
- server side validation
-There are following different type of characters of a regular expression:

.Metacharacters
.Quantifier
.Groups and Ranges
.Escape Characters or character classes

-Metacharacters
**************
  ^  - This character is used to match an expression to its right at the start
       of a string

  $  - The $sign is used to match an expression to its left at the end of a string

  .  - This character is used to match any single character in a string except
       the line terminator, i.e. /n.
  |  - It is used to match a particular character or a group of characters on
        either side. If the character on the left side is matched, then the right side's character is ignored.

  \  - It is used to escape a special character after this sign in a string.

-Quantifiers:
*************
 The quantifiers are used in the regular expression for specifying the number
  of occurrences of a character.

  +  - This character specifies an expression to its left for one or more times.

  ?  - This character specifies an expression to its left for 0 (Zero) or
       1 (one)times.

  *  - This character specifies an expression to its left for 0 or more times

  {x} - It specifies an expression to its left for only x times.

  {x, } - It specifies an expression to its left for x or more times.

  {x,y}	- It specifies an expression to its left, at least x times but less
         than y times.

Groups and Ranges:
*****************
 The groups and ranges in the regular expression define the collection of characters
enclosed in the brackets.
    ()	- It is used to match everything which is in the simple bracket.

    {}  - It is used to match a particular number of occurrences defined
         in the curly bracket for its left string.

    []  - It is used to match any character from a range of characters defined
          in the square bracket.

    [pqr] - It matches p, q, or r individually.
    [pqr][xy]- It matches p, q, or r, followed by either x or y.

    [a-z] - It matches letters of a small case from a to z.
    [A-Z] - It matches letters of an upper case from A to Z.

    ^[a-zA-Z] - It is used to match the string, which is either
           starts with a small case or upper-case letter.

    [0-9] - It matches a digit from 0 to 9.

    [aeiou]	- 	This square bracket only matches the small case vowels.

    ab[^4-9] - It matches those digits or characters which are not defined in the square bracket.

Escape Characters or Character Classes
*************************************

\s	It is used to match a one white space character.
\S	It is used to match one non-white space character.
\0	It is used to match a NULL character.
\a	It is used to match a bell or alarm.
\d	It is used to match one decimal digit, which means from 0 to 9.
\D	It is used to match any non-decimal digit.
\n It helps a user to match a new line.
\w	It is used to match the alphanumeric
[0-9a-zA-Z] characters.
\W	It is used to match one non-word character
\b	It is used to match a word boundary.



Use of Regular Expression in Python (Python Regex)
You can use the regular expression (Regex) in the code of Python by importing the re module in your script. This module defines the various function or methods which are used for handling the regular expression.

The following table defines the various functions:

Methods	Description
re.match()	The re.match() method is used to return a string which is matched with the regular expression.
re.search()	The re.search() method returns an object of the match when the pattern is found in a string or text.
re.findall()	The re.findall() method is used to return a string list containing all the matches.
re.split()	The re.split() method is used to divide the string on the basis of matching with the regular expression.
re.sub()	The re.sub() method is used to replace the matched string with another string.




 ## Library >> regexlib.com
"""


#findall()

import re
# str='rose is as beautiful and colorful flower'
# s=re.findall('ful',str)
# print(s)
#
# s1=re.findall('full',str)
# print(s1)
#
# d='cat mat pat rat sat'
# a=re.findall('[scr]',d)
# print(a)
#
# d='cat mat pat rat sat'
# a=re.findall('[scr]at',d)  # string have 's' or 'c' or 'r' followed by 'at'
# print(a)
#
# d='cat mat pat rat sat'
# a=re.findall('[^scr]at',d)  # except 's || 'c' || 'r'
# print(a)
#
#
# d='cat mat pat rat sat 999888 9998 777 9 6666'
# a=re.findall('\d{3}',d)  # match digit with 3 times concurrent occurance
# print(a)
#
# d='cat mat pat rat sat 999888 9998 777 9 6666'
# a=re.findall('\d{1,3}',d)  # match digit with 3 times concurrent occurance
# print(a)
#
# d='cat mat pat rat sat 999888 9998 777 9 6666'
# a=re.findall('\d{2,4}',d)  # match digit with 3 times concurrent occurance
# print(a)
#
# d='cat mat pat rat sat 999888 9998 777 9 6666 12345'
# a=re.findall(r'\b\d{1,5}\b',d)  # match word boundary
# print(a)


#returns a match object if there is amatch anywhere in the string
# search()-

# str="class will start at 10am"
# s=re.search("\s",str)
# print(s) # //returns psition /address of matching element
#
# str="class will start at 10am"
# s=re.search('\s',str)  # return position of whitespace
# print(s.start())
#
# str="class will start at 10am"
# s1=re.search('\d',str)
# print(s1.start())
#
# s2=re.search('python',str)
# print(s2)
#
# s3=re.search('^class.*10am$',str)
# print(s3)
# if s3:
#     print('Find')
# else:
#     print('Not Find')
#
#split() method
#
# str="class will start at 10am"
# s=re.split(" ",str)
# print(s)
# s1=re.split(" ",str,2)
# print(s1)
#
# s2=re.split("a",str)
# print(s2)

#match method
# str="Python"
# b=re.fullmatch(str,'Python')
# print(b)

#sub() -- replace/substitute
# input="rose and jasmine are flowers"
# g=re.sub(' ','*',input)
# print(g)
#
# g=re.sub(' ','*',input,3)
# print(g)


#regular expression for email validation in python

#import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")

isValid('hh@kk.com')

#interview questions for regular expression























