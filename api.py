from todoist_api_python.api import TodoistAPI

def POST_tasks(access_token, task_list):
    """Takes a todoist access token (see settings > Integrations > Developer),
        and sends an "add_task" request to the TodoistAPI with parameters
        for each task in task_list, which also should contain values for some
        parameter: content, labels, priority, due_string."""
    
    api = TodoistAPI(access_token)

    # CREATE TASKS
    for task in task_list:
        try:
            # Put together and send a POST request
            api.add_task(content=task[0], labels=task[1], priority=task[2], due_string=task[3])
        except Exception as error:
            print(error)