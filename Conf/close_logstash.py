import platform
import subprocess

current_system = platform.uname().node

pid_file = open('logstash_pids.out', 'r')
pids = pid_file.readlines()
print(
    f'There are {len(pids)} logstash instances 🔄 running currently on 💻 {current_system}')

for PID in pids:
    command = f'kill -9 {PID}'
    print(f'❌ Stopping process {PID}')
    subprocess.call(command, shell=True)
