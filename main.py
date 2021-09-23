from click.decorators import password_option
from flask import Flask, send_file, request, Response

from prometheus_client import generate_latest, Gauge
import pymongo
import logging
import os

logger = logging.getLogger(__name__)
app = Flask(__name__)
 
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
 
docdb_connection_current = Gauge(
    'docdb_connection_current',
    'Document DB connections current'
)

docdb_connection_available = Gauge(
    'docdb_connection_available',
    'Document DB connections available'
)

docdb_connection_totalCreated = Gauge(
    'docdb_connection_totalCreated',
    'Document DB connections totalCreated'
)

@app.route('/metrics', methods=['GET'])
def get_data():

    password = os.environ['DOCDB_PASSWORD']
    host = os.environ['DOCDB_HOST']

    client = pymongo.MongoClient(f"mongodb://root:{password}@{host}:27017/?tls=true&tlsCAFile=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false") 
    
    db = client.sample_databasevim 

    connections_dict = db.command("serverStatus")["connections"]

    docdb_connection_current.set(connections_dict['current'])
    docdb_connection_available.set(connections_dict['available'])
    docdb_connection_totalCreated.set(connections_dict['totalCreated'])

    client.close()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=os.environ['PORT'])