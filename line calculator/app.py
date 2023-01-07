from os import walk
import time

text_ext = ["txt", "py"]

filenames = next(walk(input("enter absolute path: ")), (None, None, []))[2]

lines = 0

for file in filenames:

    fe = file.split(".")[1]

    if fe in text_ext:
        with open(file, "r") as file:
            lines += len(file.readlines())

print(F"TOTAL PROJECT LINES - {lines}")
time.sleep(5)
#input("ENTER TO CLOSE")