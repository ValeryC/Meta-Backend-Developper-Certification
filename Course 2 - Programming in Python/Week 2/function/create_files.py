try:
    with open('newfile.txt', "w") as file:
        file.writelines("This is a new file created\nThis is another line to be added.")
except FileNotFoundError as e:
    print("Error", e)
