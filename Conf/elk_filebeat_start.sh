#!/bin/zsh
brew services list
brew services stop metricbeat-full
brew services start elasticsearch-full
brew services start kibana-full
brew services start filebeat-full
# /usr/local/Cellar/logstash-full/7.9.2/bin/logstash -f /usr/local/etc/logstash/conf/logstash-sample.conf
nohup /usr/local/Cellar/logstash-full/7.9.2/bin/logstash -f /usr/local/etc/logstash/conf/logstash-sample.conf &
ps -A | grep logstash | awk '{print $1}' > logstash_pids.out  
python3 update_logfile.py
python3 close_logstash.py
# brew services start logstash-full