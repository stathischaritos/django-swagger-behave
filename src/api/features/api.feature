Feature: Todo list REST endpoints

  Scenario: Create a new todo list
    Given the web service is running
    when I do a POST request to the 'api/lists' endpoint with a new todo list object
    then a new list should be created
    and it should contain no tasks

  Scenario: Retrieve all todo lists
    Given the web service is running 
    and at least one list has previously been created
    when I do a GET request to the 'api/lists' endpoint
    then a list of todo lists should be returned

  Scenario: Retrieve a specific todo list
    Given the web service is running 
    and a list has previously been created
    when I do a GET request to the 'api/lists' endpoint followed by that specific list's name 
    then that individual list should be returned

  Scenario: Update a specific todo list
    Given the web service is running and a list has previously been created
    when I do a PUT request to the 'api/lists' endpoint followed by that specific list's name 
    then that individual list's info should be updated

  Scenario: Delete a specific todo list
    Given the web service is running and a list has previously been created
    when I do a DELETE request to the 'api/lists' endpoint followed by that specific list's name 
    then that individual list should be deleted.


Feature: Todo Task REST endpoints

  Scenario: Create a new todo task
    Given the web service is running
    when I do a POST request to the 'api/tasks' endpoint with a new todo task object
    then a new task should be created
    and the task should show up inside its parent-list's 'tasks' field

  Scenario: Retrieve all todo tasks
    Given the web service is running 
    and at least one task has previously been created
    when I do a GET request to the 'api/tasks' endpoint
    then a list of todo tasks should be returned

  Scenario: Retrieve a specific todo task
    Given the web service is running and a task has previously been created
    when I do a GET request to the 'api/tasks' endpoint followed by that specific task's name 
    then that individual tasks should be returned

  Scenario: Update a specific todo task
    Given the web service is running and a task has previously been created
    when I do a PUT request to the 'api/tasks' endpoint followed by that specific task's name 
    then that individual task's info should be updated
  
  Scenario: Delete a specific todo task
    Given the web service is running and a task has previously been created
    when I do a DELETE request to the 'api/tasks' endpoint followed by that specific task's name 
    then that individual task should be deleted.

