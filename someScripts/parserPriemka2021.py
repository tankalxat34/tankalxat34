"""
[
    {
        "firstname": "Имя",
        "lastname: "Фамилия",
        "patronymic": "Отчество",
        "id": "012345Д",
        "marks": {
            "russian": 90,
            "math": 90,
            "social": 90,
            "additional": 10
        },
        "has-soglasie": true
    },
    {
        "firstname": "Имя",
        "lastname: "Фамилия",
        "patronymic": "Отчество",
        "id": "012345М",
        "marks": {
            "russian": 90,
            "math": 90,
            "social": 90,
            "additional": 10
        },
        "has-soglasie": false
    },
]
"""

import json
from bs4 import BeautifulSoup

info = str()
result = []

lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

vowel = "аеёиоуыэюя"
consonant = "бвгджзйклмнпрстфхчцшщ"

counter = 0


soup = BeautifulSoup(open("Списки Поступающих Экономика 2021.html", "r", encoding="UTF-8").read(), "lxml")
for e in soup.find_all("td"):
    # info += e.text + "\n"
    # print(e)
    if counter == 0:
        result.append(dict())
        result[len(result) - 1]["number"] = int(e.text)
    elif counter == 1:
        result[len(result) - 1]["lastname"] = e.text.split()[0].capitalize()
        result[len(result) - 1]["firstname"] = e.text.split()[1].capitalize()
        try:
            result[len(result) - 1]["patronymic"] = e.text.split()[2].capitalize()
        except Exception:
            result[len(result) - 1]["patronymic"] = None
    elif counter == 2:
        result[len(result) - 1]["id"] = e.text
    elif counter == 3:
        try:
            result[len(result) - 1]["marks"]["additional"] = int(e.text)
        except KeyError:
            result[len(result) - 1]["marks"] = dict()
            result[len(result) - 1]["marks"]["additional"] = int(e.text)
    elif counter == 4:
        try:
            result[len(result) - 1]["marks"]["russian"] = int(e.text)
        except ValueError:
            result[len(result) - 1]["marks"]["russian"] = None
    elif counter == 5:
        try:
            result[len(result) - 1]["marks"]["math"] = int(e.text)
        except ValueError:
            result[len(result) - 1]["marks"]["math"] = None
    elif counter == 6:
        try:
            result[len(result) - 1]["marks"]["social"] = int(e.text)
        except ValueError:
            result[len(result) - 1]["marks"]["social"] = None


        try:
            result[len(result) - 1]["marks"]["sum-full"] = result[len(result) - 1]["marks"]["additional"] + result[len(result) - 1]["marks"]["russian"] + result[len(result) - 1]["marks"]["math"] + result[len(result) - 1]["marks"]["social"]
        except Exception:
            result[len(result) - 1]["marks"]["sum-full"] = None

        try:
            result[len(result) - 1]["marks"]["sum"] = result[len(result) - 1]["marks"]["russian"] + result[len(result) - 1]["marks"]["math"] + result[len(result) - 1]["marks"]["social"]
        except Exception:
            result[len(result) - 1]["marks"]["sum"] = None
    elif counter == 7:
        if e.text.lower() == "да":
            result[len(result) - 1]["has-agreement"] = True
        elif e.text.lower() == "нет":
            result[len(result) - 1]["has-agreement"] = False
        else:
            result[len(result) - 1]["has-agreement"] = None

    counter += 1

    if counter >= 8:
        counter = 0


# print(result)

with open("priemka2021.json", "w", encoding="UTF-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False, sort_keys=False)
