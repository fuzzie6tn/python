import random
# meal to pay
name_string = input("Give me everybody's  names, seperated by comma. ")
names = name_string.split(", ")
length_of_list = len(names)
# names[length_of_list]
randomly = random.randint(0, length_of_list - 1)
person_who_will_pay = names[randomly]
print(f"The bill is going to be paid by {person_who_will_pay}")