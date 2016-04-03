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

@given('the web service is running')
def step_impl(context):
    pass

@when('I do a POST request to the api/lists endpoint with a new todo list object')
def step_impl(context):
    context.model = 'lists'
    response = requests.post('http://localhost:8000/api/lists/', json=listData, headers=headers, params=params )
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
    response = requests.get('http://localhost:8000/api/lists/' + str(context.response['id']), headers=headers, params=params )
    assert response.status_code == 200
    todoList = response.json()
    assert todoList['name'] == listData['name']
    assert todoList['description'] == listData['description']
    assert len(context.response['tasks']) == 0
    
@then('it should be inside the list of results when doing a GET request to the api/lists endpoint')
def step_impl(context):
    response = requests.get('http://localhost:8000/api/lists', headers=headers, params=params )
    assert response.status_code == 200
    assert any(x['id'] == context.response['id'] for x in response.json())

taskData = {
    'title': 'Test task title',
    'details': 'Test task details',
    'parentList': None,
    'tags' : ['testTag1,testTag2']
}

@given('a todo list has been created')
def step_impl(context):
    context.model = 'lists'
    response = requests.post('http://localhost:8000/api/lists/', json=listData, headers=headers, params=params )
    assert response.status_code == 201
    context.response = response.json()

@when('I create new tasks for that list')
def step_impl(context):
    taskData['parentList'] = context.response['id']
    requests.post('http://localhost:8000/api/tasks/', json=taskData, headers=headers, params=params )

@then('these tasks should appear nested inside it')
def step_impl(context):
    response = requests.get('http://localhost:8000/api/lists/' + str(context.response['id']), headers=headers, params=params )
    assert response.status_code == 200
    todoList = response.json()
    assert todoList['name'] == listData['name']
    assert todoList['description'] == listData['description']
    assert any(x['title'] == taskData['title'] for x in todoList['tasks'])

@when('I delete that todo list')
def step_impl(context):
    requests.delete('http://localhost:8000/api/lists/' + str(context.response['id']))

@then('the list should not appear in the api/lists list')
def step_impl(context):
    response = requests.get('http://localhost:8000/api/lists', headers=headers, params=params )
    assert not any(x['id'] == context.response['id'] for x in response.json())

@then('all the tasks of that list should be deleted')
def step_impl(context):
    response = requests.get('http://localhost:8000/api/tasks', headers=headers, params=params )
    assert response.status_code == 200
    assert not any(x['parentList'] == context.response['id'] for x in response.json())
