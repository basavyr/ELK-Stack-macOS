# ELK Stack on macOS

## Configuration and overall management of an ELK stack running on a MacBook Pro

This project aims at running a working [ELK](https://www.elastic.co/) stack fully customizable and configurable by the user. The entire service is configured on macOS Catalina, on a 16'' MacBookPro.

System metrics will be collected to a **logstash** server, and the parsed data will be sent to the elasticsearch server. 

Using Kibana UI, one can see the entire index pattern and create any queries on the collected data.

## ELK stack

![Alt text](./Resources/Images/elk-stack-elkb-diagram.svg)
<!-- <img src="./Resources/Images/elk-stack-elkb-diagram.svg"> -->

> *"ELK" is the acronym for three open source projects: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics engine. Logstash is a server‑side data processing pipeline that ingests data from multiple sources simultaneously, transforms it, and then sends it to a "stash" like Elasticsearch. Kibana lets users visualize data with charts and graphs in Elasticsearch.*

## Running environment

Elasticsearch will be installed on a MacBook Pro running macOS Catalina.
Configuration of the machine:

![syspref](Resources/Images/2020-09-27-09-40-16.png)

System info:

```bash
uname-a
Darwin Roberts-MacBook-Pro.local 19.6.0 Darwin Kernel Version 19.6.0: Mon Aug 31 22:12:52 PDT 2020; root:xnu-6153.141.2~1/RELEASE_X86_64 x86_64
```

## ELK information

The versions which are currently running on the machine are as follow:

* Elasticsearch: v 7.9.2

```json
{
  "name" : "Roberts-MacBook-Pro.local",
  "version" : {
    "number" : "7.9.2",
    "build_flavor" : "default",
    "lucene_version" : "8.6.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

* Kibana: v 7.9.2
* Logstash: 7.9.2
* Metricbeat: 7.9.2
* Filebeat: 7.9.2

> Release date for `7.9.2`: September 24, 2020.

## Worklfow

**Main goal**: View the MacBook Pro's system metrics in realtime with Kibana. Data will be stored in a Elasticsearch index.