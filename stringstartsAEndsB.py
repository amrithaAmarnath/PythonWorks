#write a program to print the strings that start with the letter 'c' and
# end with letter 'b

names=['crab', 'tab', 'cab', 'pan']
#new_names=[x for x in names if x[0] == 'c' and x[len(x)-1] == 'b']
# OR

new_names=[x for x in names if x.startswith('c') and x.endswith('b')]

print(new_names)

