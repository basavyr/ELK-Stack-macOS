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

## Filebeat example

By configuring **Filebeat** to send a certain log (given a path), logstash ingests that particular lor, and then outputs it to elasticsearch server.

Check the filebeat config [here](../Conf/filebeat.yml)

The pipeline allows logstash to ingest a log file (the actual file is [this one](logstash-tutorial.log)) and send it through elasticsearch. With Kibana, it is possible to see the content of the file.

[The Kibana UI with filebeat input](filebeatKibana.pdf).

## Check the existent indices on the elasticsearch server

With the following query (done directly in the browser), while ES instance is running, one can see all the indices created on the server.

```html
http://localhost:9200/_cat/indices
```

Results for this ES instance are as follows:

```text
green  open .kibana-event-log-7.9.2-000001 fKi45-HOS5m5ajsN1yZpWA 1 0     1   0   5.5kb   5.5kb
green  open .apm-custom-link               YZAuMTEwQ2iz5oyn9npSOA 1 0     0   0    208b    208b
green  open .kibana_task_manager_1         wM8uCqDbSvGGShveCDBlwQ 1 0     6 867 297.8kb 297.8kb
green  open .kibana-event-log-7.9.1-000001 VSPVEjXmQe2efe-A6VPsdA 1 0     1   0   5.5kb   5.5kb
green  open .apm-agent-configuration       1EOMdRuWReOxbbEdErC1CQ 1 0     0   0    208b    208b
green  open .async-search                  DSEMH06FR6iGjZehiB6C2Q 1 0     0   0    12mb    12mb
green  open .kibana_2                      mGhpsWZWQPCRQVrLDQoHfg 1 0    47  96  10.4mb  10.4mb
green  open .kibana_1                      7DDvtXHoRMOpABWn0Oe56g 1 0    27  43  10.6mb  10.6mb
yellow open metricbeat-7.9.2-2020.09.27    YCef8YYGTP2aFyyyKAlFBQ 1 1  3742   0   2.9mb   2.9mb
yellow open filebeat-7.9.2-2020.09.27      YvVWNMQyQDm9xHmopgR_kQ 1 1 71851   0  31.6mb  31.6mb
```

> More info on doing ES queries [here](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/cat-indices.html).

## Issues encountered in the development stages

1. [exceptioncaught-event-was-fired](https://discuss.elastic.co/t/logstash-an-exceptioncaught-event-was-fired-and-it-reached-at-the-tail-of-the-pipeline-it-usually-means-the-last-handler-in-the-pipeline-did-not-handle-the-exception/180515)
2. [Metricbeat Failed to connect EOF](https://discuss.elastic.co/t/metricbeat-failed-to-connect-eof/210939)