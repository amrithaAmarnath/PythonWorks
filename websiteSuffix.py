"""
8. ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
Write a python program to print website suffixes (com , org , net ,in) from this list.

"""

web=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

suffix=[x[x.rindex(".")+1:len(x)] for x in web ]
print(suffix)
