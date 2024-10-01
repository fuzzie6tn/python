# FileNotFound Error
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt", 'w')
# else:
#     print("There is a file")

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["anduf"])
#
# except KeyError as error_message:
#     print(f"the key {error_message} doesnt exist")
#
# except:
#     file = open("a_file.txt", "w")
#     file.write("someting")
#
# else:
#     content =file.read()
#     print(content)
# finally:
#     raise KeyError("The message is errror")

# raise is used to raise our own exceptions

height = float (input("Height:"))
weight = float (input("Weight:"))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
