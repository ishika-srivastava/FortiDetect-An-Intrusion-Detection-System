from elasticsearch import Elasticsearch

# configuring ElasticSearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def logToElasticSearch(alertMessage):
    es.index(index='ids-logs', doc_type='_doc', body=alertMessage)
