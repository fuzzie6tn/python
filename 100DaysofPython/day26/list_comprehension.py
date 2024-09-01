numbers = [1,2,3,4,5,6,7,8,9]
new_list =[]
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

# to reduce this code into shorter using list comprehension

new_list2 = [n+1 for n in numbers]
print(new_list2)

name = "Fazila"
new_list3 = [letter for letter in name]
print(new_list3)

new_list = [r * 2 for r in range(1,5)]
print(new_list)

names = ["fazila", "bethany", "ale", "memememee"]
name_upper = [name.upper() for name in names if len(name)>= 5]
print(name_upper)