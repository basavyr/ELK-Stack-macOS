import os
from numpy import random as rd
import time


def writeLines(number, file):
    for _ in range(number):
        random_line = rd.choice(lines).strip()+'\n'
        # print(random_line)
        file.write(random_line)


file = open('/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial.log', 'r+')

lines = file.readlines()

for _ in range(5):
    print('writing to file...')
    writeLines(150, file)
    time.sleep(30)


file.close()
