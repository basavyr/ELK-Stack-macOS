#!/bin/zsh
brew services list
brew services stop metricbeat-full
brew services start elasticsearch-full
brew services start kibana-full
brew services start filebeat-full
# brew services start logstash-full