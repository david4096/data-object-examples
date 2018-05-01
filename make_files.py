import json


from ga4gh.dos.client import Client

client = Client("http://ec2-52-26-45-130.us-west-2.compute.amazonaws.com:8080/ga4gh/dos/v1")
lc = client.client
models = client.models

response = {}
response['next_page_token'] = "0"

def write_object(data_object):
    with open(data_object['id'], 'w') as outfile:
        json.dump(data_object.marshal(), outfile)

#while (response.get('next_page_token', None)):
ListDataObjectsRequest = models.get_model('ListDataObjectsRequest')
list_request = ListDataObjectsRequest(page_token="0")
response = lc.ListDataObjects(body=list_request).result()
map(write_object, response.data_objects)
    #break
