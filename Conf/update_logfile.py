import os
from numpy import random as rd
import time

backup_logfile = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial_backup.log'


def ResetFile(backup_file, file):
    with open(backup_file) as f:
        lines = f.readlines()
        with open(file, 'w') as ff:
            print(
                f'Resetting the logfile to its standard beat content due to increased size...')
            for line in lines:
                ff.write(line)
                # print(line)


def WriteLines(file, lines, number):
    # file.write('\n')
    for _ in range(number):
        random_line = rd.choice(lines).strip()+'\n'
        # print(random_line.strip())
        file.write('\n'+random_line.strip())


# The path to the logfile that must be constantly update
logfile = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial.log'

# Use this method to reset the contents of the initial logbeat file
# ResetFile(backup_logfile, logfile)


def LogLineWriter(file, nLines, nReps):
    logstash_init_time = 2
    lines_beat_time = 5
    print(f'⏳Wait for the logstash instance to start...')
    time.sleep(logstash_init_time)
    with open(file, 'r+') as logfile:
        lines = logfile.readlines()
        if(len(lines) > 500):
            ResetFile(backup_logfile, file)
        for _ in range(nReps):
            print(f'Writing an additional {nLines} lines to the logfile...📑 ')
            WriteLines(logfile, lines, nLines)
            time.sleep(lines_beat_time)
    print(f'Finished writing the entire log batch to the logfile...')


LogLineWriter(logfile, 100, 2)
