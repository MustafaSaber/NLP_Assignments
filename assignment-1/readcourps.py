import os
import glob

path = '/Users/mostafasaber/Desktop/tempNLP/Khaleej-2004/Economy'

l = []
for i in os.listdir(path):
    tempfile = os.path.join(path, i)
    with open(tempfile, 'r') as file:
        temp = ""
        for line in file:
            temp += line
        l.append(temp)
with open("courps.txt", 'w') as filename:
    for i in l:
        filename.write(i + '\n')

