import os

print(os.path.exists("test.csv"))
print(os.path.isfile("test.csv"))
print(os.path.isdir("design"))


os.rename("renamed.txt", "text.txt")
