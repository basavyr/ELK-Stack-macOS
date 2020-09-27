# Configuration description

Store any relevant configuration information, issues and solutions, as well as relevant sources that help at maintaining a solid stack running.

## Paths for every service

Install dirs: mostly in `/Cellar/` (since these services are installed via the **homebrew package**).

More info [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/brew.html).

Conf dirs: 

```bash
/usr/local/etc
```

### Elasticsearch

Install path (with `/bin`, readme and so on):

```bash
/usr/local/Cellar/elasticsearch-full/7.9.2
```

Configuration file path ([`elasticsearch.yml`](../Conf/elasticsearch.yml)):

```bash
/usr/local/etc/elasticsearch
```

### Kibana

Install path (with `/bin`, readme and so on):

```bash
/usr/local/Cellar/kibana-full/7.9.2
```

Configuration file path ([`kibana.yml`](../Conf/kibana.yml)):

```bash
/usr/local/etc/kibana
```

### Logstash

Install path (with `/bin`, readme and so on):

```bash
/usr/local/Cellar/logstash-full/7.9.2
```

Configuration file path ([`logstash.yml`](../Conf/logstash.yml)):

```bash
/usr/local/etc/logstash
```

### Metricbeat

Install path (with `/bin`, readme and so on):

```bash
/usr/local/Cellar/metricbeat-full/7.9.2
```

Configuration file path ([`metricbeat.yml`](../Conf/logstash.yml)):

```bash
/usr/local/etc/metricbeat
```

## Running a test for sending metrics

Using metricbeat, it is possible to ingest logs into a logstash instance via the following configuration pipeline (managed within logstash).
With this simple pipeline, logstash can listen to any beats via the standard port, and then send the results (so far unparsed) to the elasticsearch server via the standard `9200` port.

```yml
# Sample Logstash configuration for creating a simple
# Beats -> Logstash -> Elasticsearch pipeline.

input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
    #user => "elastic"
    #password => "changeme"
  }
}
```

Running the pipeline can be done directly from a logstash executable, pointing to the default configuration as an argument.

```bash
bin/logstash -f /usr/local/etc/logstash/logstash-sample.conf
```

Output can be then seen within Kibana (see example [here](kibanaElastic.pdf)).
