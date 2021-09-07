from google.cloud import datastore
from typing import List
from models import ChoosenComment


client = datastore.Client(namespace='random-github')

def insert_choosen_comments(data: List[ChoosenComment]):
    complete_key = client.key('ChoosenComments', 'currently_active_comments')
    task = datastore.Entity(key=complete_key)
    
    data_for_insert = []
    for d in data:
        data_for_insert.append(d.dict())
    
    task.update({
        'data': data_for_insert
    })
    client.put(task)
    

def get_choosen_comments() -> List[ChoosenComment]:
    complete_key = client.key('ChoosenComments', 'currently_active_comments')
    data = dict(client.get(complete_key))
    choosen_comments = []
    for entity in data['data']:
        entity_dict = dict(entity)
        choosen_comments.append(ChoosenComment.parse_obj(entity_dict))
    return choosen_comments