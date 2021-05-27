Macbook = {
    'name': 'Macbook',
    'price': 200000,
    'company': 'Apple'
}

Sceptre = {
    'name': 'Spectre',
    'price': 100000,
    'company': 'HP'
}

Yoga = {
    'name': 'Yoga',
    'price': 75000,
    'company': 'Lenovo'
}

li = [Yoga, Macbook, Sceptre] # list of dictionaries 
print(li)

li_of_num = [7,8,-1,0,9,5]
print("Before sorting", li_of_num)

# sort the same list

li_of_num.sort() # use the sort function on list
print("After sorting in asc order", li_of_num)

li_of_num2 = [7,8,-1,0,9,5]
print("Before sorting", li_of_num2)

li_of_num2.sort(reverse = True)
print("After sorting in desc order", li_of_num2)

# if you don't want to sort the same list and and want to return a new one

li_new = [3,7,1,9,2,0]

print("Before sorting", li_new)
result = sorted(li_new) # it returns a new sorted list

print("After sorting", li_new)
print("Result", result)

