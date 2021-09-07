from google.cloud import datastore

client = datastore.Client()

def insert_entity(data):
    print('insert entity')
    