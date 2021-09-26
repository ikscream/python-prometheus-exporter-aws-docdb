# Description

Little prometheus exporter for Amazon DocumentDB with default `TLS`.

### Environment

|Name|Description|Default|
| ------------- | ------------- | ------------- |
|PORT|Specify port for exporter|5000|
|DOCDB_HOST|DocumentDB host|example.com|
|DOCDB_PASSWORD|DocumentDB password|password|
|DOCDB_TLS|Enable TLS|1 (enabled)| 

### Metrics

|Name|Description|
| - | - |
|docdb_connection_current | Count of current connections |
|docdb_connection_available | Count of available connections |
|docdb_connection_totalCreated | Count of total created connections |

### Docker 

```
docker pull debugger0/exporter-docdb
```


### Local tests

```
docker-compose up --build --abort-on-container-exit
```

#### Local environment configuration

`systemd.unified_cgroup_hierarchy=0` for advisor in kernel options