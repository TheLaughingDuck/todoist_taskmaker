from todoist_api_python.api import TodoistAPI

def POST_tasks(access_token, task_list):
    api = TodoistAPI(access_token)

    # CREATE TASKS
    for task in task_list:
        try:
            api.add_task(content=task[0], labels=task[1], priority=task[2], due_string=task[3])
        except Exception as error:
            print(error)