# implement a python script that checks if any of the local config files for logstash, metricbeat and filebeat have been modified.

import filecmp
import os
import shutil


def give_service_sys_path(service):
    service_path = '/usr/local/etc/'+service+'/'+service+'.yml'
    return service_path


project_tree = str(os.path.abspath(os.curdir))+'/'
# print(project_tree)

# the config filepaths (installed on the actual system)
logstash_pipeline = '/usr/local/etc/logstash/conf/logstash-sample.conf'
logstash_conf = give_service_sys_path('logstash')
metricbeat_conf = give_service_sys_path('metricbeat')
filebeat_conf = give_service_sys_path('filebeat')

# local copies of the config files (on the project tree)
local_logstash_pipeline = project_tree + 'logstash_pipeline.conf'
local_logstash_conf = project_tree + 'logstash.yml'
local_metricbeat_conf = project_tree+'metricbeat.yml'
local_filebeat_conf = project_tree+'filebeat.yml'

sys_name = os.uname().nodename

print(
    f'Starting to check for any updates on the config pipelines available @ {sys_name}...')
print(f'Sys info...')
print(f'{os.uname().machine}')


def absolute_path(path):
    return str(os.path.abspath(path))


def CheckFiles(files):
    for file in files:
        if(filecmp.cmp(file[1], file[2]) is True):
            print(f'{file[0]} | ✅')
        else:
            print(f'{file[0]} | ⛔️')
            shutil.copy(file[1], file[2])
            print(f'The config for {file[0]} was updated...| 📂')


files = [['logstash', logstash_conf, local_logstash_conf], ['metricbeat', metricbeat_conf, local_metricbeat_conf], [
    'filebeat', filebeat_conf, local_filebeat_conf], ['logstash-pipeline', logstash_pipeline, local_logstash_pipeline]]

CheckFiles(files)
