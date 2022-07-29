import os

packageName = str(input("Package name: "))
with open("badges.txt", "r", encoding="UTF-8") as file:
    print(file.read().replace("PACKAGE_NAME", packageName))

os.system("pause")