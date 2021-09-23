# Description

Little prometheus exporter for Amazon DocumentDB with default `TLS`.

### Environment

|Name|Description|Default|
| ------------- | ------------- | ------------- |
|PORT|Specify port for exporter|5000|
|DOCDB_HOST|DocumentDB host|example.com|
|DOCDB_PASSWORD|DocumentDB password|password|

### Metrics

|Name|Description|
| - | - |
|docdb_connection_current | Count of current connections |
|docdb_connection_available | Count of available connections |
|docdb_connection_totalCreated | Count of total created connections |

### Docker 

```
docker pull debugger0/exporter-docdb:v1.0
```