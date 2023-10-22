# to read file

# file = open("my_file.txt")
# the line above does the same thing as line 3
with open("/Users/chris/OneDrive/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
    # we don't have to remember to close the file because of line 3
    # f.close()

# to write in a file
# mode w will erase previous content of the file
# mode a appends to the previous content
with open("/Users/chris/OneDrive/Desktop/my_file.txt", mode="a") as file:
    file.write("\nNew Text")
