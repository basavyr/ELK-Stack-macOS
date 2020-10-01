import os
from numpy import random as rd
import time


from joblib import Parallel, delayed
import multiprocessing

# Path to the original log file
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


def LineWriter_mthrd(file, lines, N_lines):
    with open(file, 'a') as log_file:
        for _ in range(N_lines):
            line = rd.choice(lines).strip()+'\n'
            log_file.write(line)


def Batch_ComponentWriter(file, N_lines, N_reps):
    time.sleep(1)
    print(f'{file[-14:]} is working OK ✅ | {N_lines} - {N_reps}')


def BatchLogWriter(files, N_lines, N_reps):
    logstash_init_time = 0
    writing_freq = 0
    print(f'⏳Wait for the logstash instance to start...')
    time.sleep(logstash_init_time)
    count = 1
    parallel_batch = Parallel(n_jobs=multiprocessing.cpu_count())(
        delayed(Batch_ComponentWriter)(file, N_lines, N_reps) for file in files)

    #! SERIAL APPROACH
    # for file in files:
    # Batch_ComponentWriter(file, N_lines, N_reps)
    # print(f'📝 Writing logs into the file NO-{count}...')
    # with open(file, 'r') as loglines:
    #     log_content = loglines.readlines()
    #     # print(len(log_content))
    #     if(not len(log_content)):
    #         FillFile(backup_logfile, file)
    #     elif len(log_content) > 45:
    #         ResetFile(backup_logfile, file)
    #     for _ in range(N_reps):
    #         lines = open(file, 'r').readlines()
    #         print(
    #             f'Writing an additional {N_lines} lines to the logfile...📑 ')
    #         LineWriter_mthrd(file, lines, N_lines)
    #         time.sleep(writing_freq)
    
    count = count+1
    print(f'⌛️ Finished writing data in logfiles...')


start = time.time()
BatchLogWriter(log_batch, 2, 50)
print(time.time()-start)
# LogLineWriter(logfile1, 150, 15)
