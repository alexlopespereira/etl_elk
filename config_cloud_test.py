import os
from elasticsearch import Elasticsearch

from etlelk.configbase import ConfigBase
from etlelk.settings_generic import body_settings_generic


class Config(ConfigBase):
    KIBANA_SAVED_OBJECTS_PATH = os.environ.get('KIBANA_SAVED_OBJECTS_PATH') or "."
    KIBANA_HOST = os.environ.get('ES_HOST') or 'localhost'
    KIBANA_PORT = os.environ.get('ES_PORT') or '5601'
    ES_HOST = os.environ.get('ES_HOST') or 'localhost'
    ES_PORT = os.environ.get('ES_PORT') or '9200'
    ES_USER = os.environ.get('ES_USER') or 'elastic'
    ES_PASSWORD = os.environ.get('ES_PASSWORD') or 'pass'
    ES_USE_SSL = os.environ.get('ES_USE_SSL') == "True"
    ES_SERVICOS_INDEX = os.environ.get('ES_SERVICOS_INDEX') or 'servicos'
    ES_SOURCECODE_INDEX = os.environ.get('ES_SOURCECODE_INDEX') or 'sourcecode'
    ES_TAGCLOUD_INDEX = os.environ.get('ES_TAGCLOUD_INDEX') or 'tagcloud'
    ES_CLOUD_ID = os.environ.get('ES_CLOUD_ID') or 'cloudid'

    if ES_USE_SSL:
        ES_URL = "https://{0}:{1}".format(ES_HOST, ES_PORT)
        KIBANA_URL = "https://{0}:{1}".format(KIBANA_HOST, KIBANA_PORT)
    else:
        ES_URL = "http://{0}:{1}".format(ES_HOST, ES_PORT)
        KIBANA_URL = "http://{0}:{1}".format(KIBANA_HOST, KIBANA_PORT)
    
    
    INDEXES = []
    
    
    es = Elasticsearch(
        cloud_id=ES_CLOUD_ID,
        http_auth=(ES_USER, ES_PASSWORD),
    )
    
    es = es
    
    job_tagcloud = {"index": ES_TAGCLOUD_INDEX, "settings": body_settings_generic, "prefix": "TAGCLOUD__",
                     "description": "Tag Cloud", "module_name": "ElkEtlTagCloud",
                     "class_name": "ElkEtlTagCloud", "es": es}
    
    INDEXES = [job_tagcloud]
