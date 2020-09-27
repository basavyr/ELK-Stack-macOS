#!/bin/zsh
brew services list
brew services stop filebeat-full
brew services start elasticsearch-full
brew services start kibana-full
brew services start metricbeat-full
# brew services start logstash-full