import os
from numpy import random as rd
import time

backup_logfile = open(
    '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial_backup.log', 'r')


def writeLines(number, file):
    for _ in range(number):
        random_line = rd.choice(lines).strip()+'\n'
        # print(random_line)
        file.write(random_line)


# The path to the logfile that must be constantly update
file = open('/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial.log', 'r+')

# Store the initial log-file content into an array of lines
lines = file.readlines()


def LogLineWriter(file, nLines, nReps):
    logstash_init_time = 2
    lines_beat_time = 1
    print(f'⏳Wait for the logstash instance to start...')
    time.sleep(logstash_init_time)
    for _ in range(nReps):
        print(f'Writing an additional {nLines} lines to the logfile...📑 ')
        # writeLines(nLines, file)
        time.sleep(lines_beat_time)
    print(f'Finished writing the entire log batch to the logfile...')


LogLineWriter(file, 150, 5)

file.close()
