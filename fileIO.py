# f = open("myFile.txt", "r")
f = open("myFile.txt", "w")
# f = open("myFile.txt", "a")

print("File name:", f.name)
print("Check if File is readable:", f.readable())
print("Check if File is writable:", f.writable())
f.close()
