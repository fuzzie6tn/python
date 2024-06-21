       #  0     1    2
row1 = ["⭐️","⭐️","⭐️"]# 0
row2 = ["⭐️","⭐️","⭐️"]# 1
row3 = ["⭐️","⭐️","⭐️"]# 2

map = [row1, row2, row3] #nested list

print(f"{row1}\n{row3}\n{row3}")

position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row3}\n{row3}")