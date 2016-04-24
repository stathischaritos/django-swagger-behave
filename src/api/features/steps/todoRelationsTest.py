from behave import *
import requests
import json 

listData = {
    'name':'Test list title',
    'description': 'Test list description'
}

headers = {
    'Content-type': 'application/json'
}

params={
    'format':'json'
}

taskData = {
    'title': 'Test task title',
    'details': 'Test task details',
    'parentList': "10",
    'tags' : ['testTag1,testTag2']
}

API_URL = "http://127.0.0.1:8000/api/"

@given('the web service is running')
def step_impl(context):
    pass

@when('I do a POST request to the api/lists endpoint with a new todo list object')
def step_impl(context):
    context.model = 'lists'
    response = requests.post(API_URL+'lists/', json=listData, headers=headers, params=params )
    assert response.status_code == 201
    context.response = response.json()

@then('a new list should be created')
def step_impl(context):
    assert context.response['id']
    assert context.response['name'] == listData['name']
    assert context.response['description'] == listData['description']

@then('it should contain no tasks')
def step_impl(context):
    assert len(context.response['tasks']) == 0

@then('it should be returned when doing a GET request to the api/lists endpoint followed by that specific list`s name')
def step_impl(context):
    response = requests.get(API_URL+'lists/' + str(context.response['id']), headers=headers, params=params )
    assert response.status_code == 200
    todoList = response.json()
    assert todoList['name'] == listData['name']
    assert todoList['description'] == listData['description']
    assert len(context.response['tasks']) == 0
    
@then('it should be inside the list of results when doing a GET request to the api/lists endpoint')
def step_impl(context):
    response = requests.get(API_URL+'lists', headers=headers, params=params )
    assert response.status_code == 200
    assert any(x['id'] == context.response['id'] for x in response.json())


@given('a todo list has been created')
def step_impl(context):
    context.model = 'lists'
    response = requests.post(API_URL+'lists/', json=listData, headers=headers, params=params )
    assert response.status_code == 201
    context.response = response.json()

@given('a todo task has been created')
def step_impl(context):
    context.model = 'tasks'
    taskData['parentList'] = "10"
    response = requests.post(API_URL+'tasks/', json=taskData, headers=headers, params=params )
    assert response.status_code == 201
    context.response = response.json()
    
@when('I create new tasks for that list')
def step_impl(context):
    taskData['parentList'] = context.response['id']
    requests.post(API_URL+'tasks/', json=taskData, headers=headers, params=params )

@when('I update the task with new tags')
def step_impl(context):
    taskData['tags'] = ['testTag3,testTag4']
    requests.put(API_URL+'tasks/' + str(context.response['id']) , json=taskData, headers=headers, params=params )

@then('the tags list should be updated')
def step_impl(context):
    response = requests.get(API_URL+'tags/', headers=headers, params=params )
    assert len(response.json())
    
@then('these tasks should appear nested inside it')
def step_impl(context):
    response = requests.get(API_URL+'lists/' + str(context.response['id']), headers=headers, params=params )
    assert response.status_code == 200
    todoList = response.json()
    assert todoList['name'] == listData['name']
    assert todoList['description'] == listData['description']
    assert any(x['title'] == taskData['title'] for x in todoList['tasks'])

@when('I delete that todo list')
def step_impl(context):
    requests.delete(API_URL+'lists/' + str(context.response['id']))

@then('the list should not appear in the api/lists list')
def step_impl(context):
    response = requests.get(API_URL+'lists', headers=headers, params=params )
    assert not any(x['id'] == context.response['id'] for x in response.json())

@then('all the tasks of that list should be deleted')
def step_impl(context):
    response = requests.get(API_URL+'tasks', headers=headers, params=params )
    assert response.status_code == 200
    assert not any(x['parentList'] == context.response['id'] for x in response.json())
