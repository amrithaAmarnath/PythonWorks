# 1. Add a list of elements to a set
set1 = {1,2}
lst= [10,20,30]
set1.update(lst)
print(set1)
# set1.add(3) # 'add' for 'set' objects doesn't apply to a 'list' object, can
# add integer to set 1 by 1
# print(set1)
# set1.add("Hello")
# print(set1)



#2. Get only unique items from two sets

Set1 = {5,25,15,4,3}
Set2 = {5,25,15,2,1}
print(f'unique elements = {Set1 | Set2}')
# Set1 | Set2 or Set1.union(Set2)

#3. Check if two sets have any elements in common,
# display the common elements
print(f'common elements = {Set1 & Set2}')
# use isdisjoint() >> checks if two sets have any elements in common.
# If no items in common return true otherwise return False

if Set1.isdisjoint(Set2):
    print("not items in common")
else:
    print("have items in common")
    print(Set1 & Set2)

# 4. Remove items from set1 that are not common to both set1 and set2
# intersection_update() >> update the set with intersection result
# intersection() >> returns the common elements from two sets, but not update to any set
Set1 = {5,25,15,4,3}
Set2 = {5,25,15,2,1}
Set1.intersection_update(Set2)  # or use &= like Set1 &= Set2
print(Set1)

Set1 = {5,25,15,4,3}
Set2 = {5,25,15,2,1}
Set1.difference_update(Set2)  # or use -= like Set1 &= Set2
print(Set1)

