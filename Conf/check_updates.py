# implement a python script that checks if any of the local config files for logstash, metricbeat and filebeat have been modified.

import filecmp
import os


def give_service_sys_path(service):
    service_path = '/usr/local/etc/'+service+'/'+service+'.yml'
    return service_path


# the config filepaths (installed on the actual system)
logstash_pipeline = '/usr/local/etc/logstash/conf/logstash-sample.conf'
logstash_conf = '/usr/local/etc/logstash/logstash.yml'
metricbeat_conf = '/usr/local/etc/metricbeat/metricbeat.yml'
filebeat_conf = '/usr/local/etc/filebeat/filebeat.yml'

# local copies of the config files
local_logstash_pipeline = 'logstash-sample.conf'
local_logstash_conf = '/Users/basavyr/Library/Mobile Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/ELK-Stack-macOS/Conf/logstash.yml'
local_metricbeat_conf = 'metricbeat.yml'
local_filebeat_conf = 'filebeat.yml'

sys_name = os.uname().nodename

print(f'Sys info...')
print(f'{os.uname().machine}')
print(
    f'Starting to check for any updates on the config pipelines available @ {sys_name}')


def absolute_path(path):
    return str(os.path.abspath(path))


def CheckFiles(files):
    for file in files:
        if(filecmp.cmp(file[0], file[1]) is True):
            print(f'✅')

files=[[logstash_conf,local_logstash_conf]]

CheckFiles(files)