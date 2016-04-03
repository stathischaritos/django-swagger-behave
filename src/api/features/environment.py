import requests

def after_tag(context, tag):
    if tag == "REST":
        requests.delete('http://localhost:8000/api/'+ context.model +'/' + str(context.response['id']))
    pass