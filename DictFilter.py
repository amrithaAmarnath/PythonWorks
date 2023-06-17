"""
Write a program to filter the dictionary ,from a dictionary of people’s heights and 
you wanted to filter out anyone below a certain height.

Let’s filter out anyone less than 170cm.
"""""

heights = {
    'Alice': 165,
    'Bob': 180,
    'Charlie': 170,
    'David': 175,
    'Eve': 160
}

print(f'Original dictionary : \n{heights}')

res={k:v for (k,v) in heights.items() if v >= 170}
print(f'Filtered_heights : \n{res}')



