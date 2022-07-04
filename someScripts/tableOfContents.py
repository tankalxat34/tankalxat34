import pyperclip

f = open("README.md", "r", encoding="utf-8")
file = f.readlines()
f.close()

titleList = ""

summator = {}
summator["last"] = "#"

for i in range(len(file)):
    line = file[i]
    titleLine = line.split()
    
    if line[0] == "#":

        if titleLine[0] != summator["last"] and titleLine[0] != "#":
            summator[titleLine[0]] = 0

        summator["last"] = titleLine[0]

        try:
            summator[titleLine[0]] += 1
        except Exception:
            summator[titleLine[0]] = 0
            summator[titleLine[0]] += 1
        
        titleList += "    " * (len(titleLine[0]) - 1) + f"{summator[titleLine[0]]}. [{' '.join(titleLine[1::]).replace(')','')}](#{' '.join(titleLine[1::]).replace(')','').replace('(','').replace(' ', '-')}])\n"

print(titleList)

pyperclip.copy(titleList)
