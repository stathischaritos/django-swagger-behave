Feature: Todo list REST endpoints
  @REST
  Scenario: Create a new todo list
    Given the web service is running
    when I do a POST request to the api/lists endpoint with a new todo list object
    then a new list should be created
    and it should contain no tasks
    and it should be returned when doing a GET request to the api/lists endpoint followed by that specific list`s name
    and it should be inside the list of results when doing a GET request to the api/lists endpoint

  @REST
  Scenario: Populate a todo list
    Given the web service is running
    and a todo list has been created
    when I create new tasks for that list
    then these tasks should appear nested inside it
  
  @REST
  Scenario: Delete a todo list
    Given the web service is running
    and a todo list has been created
    when I delete that todo list
    then the list should not appear in the api/lists list
    and all the tasks of that list should be deleted
