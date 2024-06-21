heights = input("Enter heights of students? ").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(heights)    

#total height / len of height
total_height = 0
for i in heights:
    total_height += i
print(total_height)

num_of_students = 0
for i in heights:
    num_of_students += 1
print(num_of_students)

average = round(total_height/num_of_students)
print(f"Average is {average}")
#without for loop
# '''
# total height = sum(heights)
# number of students = len(heights)
# avg = round(total height / number of students)
# print(average)
# '''

