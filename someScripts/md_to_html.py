"""
Конвертер markdown в HTML файлы
"""


import sys
import markdown
import os

filename = sys.argv[1].split("=")[1]

print(filename)


def main():
    with open(filename, "r", encoding="UTF-8") as file:
        md = file.read()

    with open("".join(filename.split(".")[:-1]) + ".html", "w", encoding="UTF-8") as html_file:
        html_file.write(markdown.markdown(md))

    os.system("pause")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(exc)
