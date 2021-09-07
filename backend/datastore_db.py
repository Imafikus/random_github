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
    

    