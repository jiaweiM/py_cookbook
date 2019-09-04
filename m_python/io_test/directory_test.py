import os

dir = "Z:\\MaoJiawei\\test\\pd"

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    print(filename)
