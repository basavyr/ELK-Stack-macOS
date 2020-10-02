import os
from numpy import random as rd
import time


from joblib import Parallel, delayed
import multiprocessing

import threading

# Path to the original log file
BACKUP_LOGFILE = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial_backup.log'

# Path to the nova compute logs backup file
BACKUP_NOVA_LOGFILE = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/nova-log_backup.log'


LOGFILE_DIRECTORY_PATH = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/'


def Generate_tutorial_log(TYPE, id):
    if(TYPE == 'nova'):
        logfile = LOGFILE_DIRECTORY_PATH+f'nova-log-{id}.log'
    else:
        logfile = LOGFILE_DIRECTORY_PATH+f'logstash-tutorial-{id}.log'
    return logfile


# The path to the logfile that must be constantly update
# logfile1 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-1.log'
# logfile2 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-2.log'
# logfile3 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-3.log'
# logfile4 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-4.log'
# logfile5 = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Resources/LOGS/logstash-tutorial-5.log'

# log_batch = [logfile1, logfile2, logfile3, logfile4, logfile5]
log_batch = []

for id in range(5):
    log_batch.append(Generate_tutorial_log('tutorial', id+1))


nova_log_batch = []

for id in range(5):
    nova_log_batch.append(Generate_tutorial_log('nova', id+1))

# for file in nova_log_batch:
#     open(file,'w+')

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
    lines_beat_time = 10
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


def Batch_ComponentWriter(backup_logfile, file, N_lines, N_reps):
    writing_freq = 10
    current_thread = threading.current_thread().ident
    current_file = file[-14:]
    count = 1
    with open(file, 'r') as loglines:
        log_content = loglines.readlines()
        if(not len(log_content)):
            FillFile(backup_logfile, file)
        elif len(log_content) > 1500:
            ResetFile(backup_logfile, file)
        for _ in range(N_reps):
            lines = open(file, 'r').readlines()
            print(
                f'Writing an additional {N_lines} lines to the logfile...📑 | thd_id-{current_thread}')
            LineWriter_mthrd(file, lines, N_lines)
            time.sleep(writing_freq)
            print(f'Finished the rep {count}')
            count = count+1


def BatchLogWriter(files, N_lines, N_reps):
    logstash_init_time = 1
    print(f'⏳Wait for the logstash instance to start...')
    time.sleep(logstash_init_time)

    # ?PARALLEL APPROACH
    nova_parallel_batch = Parallel(n_jobs=multiprocessing.cpu_count())(
        delayed(Batch_ComponentWriter)(BACKUP_NOVA_LOGFILE, file, N_lines, N_reps) for file in files)
    # log_parallel_batch = Parallel(n_jobs=multiprocessing.cpu_count())(
    #     delayed(Batch_ComponentWriter)(BACKUP_LOGFILE, file, N_lines, N_reps) for file in files)

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
    # count = count+1

    print(f'⌛️ Finished writing data in logfiles...')


start = time.time()
BatchLogWriter(nova_log_batch, 500, 2)
print(f'Total logging process took: {time.time()-start}s')
# LogLineWriter(logfile1, 150, 15)
