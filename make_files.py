import json


from ga4gh.dos.client import Client

client = Client("http://ec2-52-26-45-130.us-west-2.compute.amazonaws.com:8080/ga4gh/dos/v1")
lc = client.client
models = client.models

ListDataObjectsRequest = models.get_model('ListDataObjectsRequest')

response = models.get_model('ListDataObjectsResponse')
response.next_page_token = "0"

def write_object(data_object):
    with open('ga4gh/dos/v1/dataobjects/' + data_object['id'], 'w') as outfile:
        json.dump(data_object.marshal(), outfile)

list_response = ListDataObjectsRequest(page_token=response.next_page_token).result()
map(write_object, list_response.data_objects)
