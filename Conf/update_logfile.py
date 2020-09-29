import os
from numpy import random as rd
import time

backup_logfile = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial_backup.log'


# The path to the logfile that must be constantly update
logfile = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/logstash-tutorial.log'


def ResetFile(backup_file, file):
    with open(backup_file, 'r') as f:
        lines = f.readlines()
        with open(file, 'w') as ff:
            print(
                f'🔄 Resetting the logfile to its standard beat content due to increased size...')
            for line in lines:
                ff.write(line)


def FillFile(backup_file, file):
    with open(backup_file, 'r') as f:
        lines = f.readlines()
        with open(file, 'w') as ff:
            print(
                f'⤵️Filling the logfile with backed up data due to non-existent data...')
            for line in lines:
                ff.write(line)


def Reset_OTF(backup_file, file):
    backup = open(backup_file, 'r')
    lines = backup.readlines()
    print(f'🔄 Resetting the logfile to its standard beat content due to increased size...')
    for line in lines:
        file.write(line)
        # print(line)
    backup.close()


def WriteLines(file, lines, number):
    # file.write('\n')
    with open(file, 'a') as f:
        # f.write('\n')
        for _ in range(number):
            random_line = rd.choice(lines).strip()+'\n'
            # print(random_line.strip())
            f.write(random_line.strip()+'\n')


# Use this method to reset the contents of the initial logbeat file
# ResetFile(backup_logfile, logfile)


def LogLineWriter(file, nLines, nReps):
    logstash_init_time = 1
    lines_beat_time = 8
    print(f'⏳Wait for the logstash instance to start...')
    time.sleep(logstash_init_time)
    lines = open(file, 'r').readlines()
    if(not len(lines)):
        FillFile(backup_logfile, file)
    elif len(lines) > 1500:
        ResetFile(backup_logfile, file)
    for _ in range(nReps):
        lines = open(file, 'r').readlines()
        print(f'Writing an additional {nLines} lines to the logfile...📑 ')
        WriteLines(file, lines, nLines)
        time.sleep(lines_beat_time)
    print(f'⌛️ Finished writing the entire log batch to the logfile...')


LogLineWriter(logfile, 100, 1)
