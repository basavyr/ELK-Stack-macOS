import uuid
import datetime
import socket
import platform
import secrets
from numpy import random as rd
import numpy as np

UUIDs = []
for _ in range(6):
    UUIDs.append(uuid.uuid4())


def GenerateLogs(file, N_lines, UUIDs):
    for _ in range(N_lines):
        current_uuid = rd.choice(UUIDs)
        log_line = LogLine(current_uuid)
        for field in log_line:
            file.write(str(field)+' ')
        file.write('\n')


def LogLine(uuid):
    IPADDR = socket.gethostbyname(socket.gethostname())
    TIMESTAMP = datetime.datetime.utcnow()
    PY_VER = platform.python_version()
    USER = platform.node()
    HASH = secrets.token_hex(nbytes=20)
    JOBS = rd.randint(0, 10000)
    VM = rd.randint(1, 100)
    return [TIMESTAMP,  uuid, USER, VM, JOBS, HASH, IPADDR]


filepath = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Conf/aggr_logs_py/aggr_log.log'

file = open(filepath, 'w')

GenerateLogs(file, 100, UUIDs)
