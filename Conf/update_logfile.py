import os
from numpy import random as rd
import time


from joblib import Parallel, delayed
import multiprocessing

backup_logfile = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial_backup.log'


# The path to the logfile that must be constantly update
logfile1 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-1.log'
logfile2 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-2.log'
logfile3 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-3.log'
logfile4 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-4.log'
logfile5 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-5.log'

log_batch = [logfile1, logfile2, logfile3, logfile4, logfile5]


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
    logstash_init_time = 60
    lines_beat_time = 15
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


def BatchLogWriter(files, N_lines, N_reps):
    logstash_init_time = 1
    writing_freq = 0
    print(f'⏳Wait for the logstash instance to start...')
    time.sleep(logstash_init_time)
    count = 1
    for file in files:
        print(f'📝 Writing logs into the file NO-{count}...')
        with open(file, 'r') as loglines:
            log_content = loglines.readlines()
            # print(len(log_content))
            if(not len(log_content)):
                FillFile(backup_logfile, file)
            elif len(log_content) > 45:
                ResetFile(backup_logfile, file)
            for _ in range(N_reps):
                    lines = open(file, 'r').readlines()
                    print(f'Writing an additional {N_lines} lines to the logfile...📑 ')
                #     WriteLines(file, lines, nLines)
                    time.sleep(writing_freq)
        count = count+1
    print(f'⌛️ Finished writing data in logfiles...')


BatchLogWriter(log_batch, 150, 2)
# LogLineWriter(logfile1, 150, 15)


# def hi():
#     time.sleep(1)
#     print('🙈 hi')


# num_cores = multiprocessing.cpu_count()
# print(num_cores)

# Parallel(n_jobs=num_cores)(delayed(hi)() for _ in range(10))
# # results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
# # print(results)
