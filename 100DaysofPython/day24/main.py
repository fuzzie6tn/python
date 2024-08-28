with open("/home/fazidev/Desktop/file.txt") as file:
    content = file.read()
    print(content)

with open("new_file.txt", mode = "w") as file:
    text = file.write("Hello world")
