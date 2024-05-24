from tabulate import tabulate
from todoist_api_python.api import TodoistAPI

# For access token
import os
from dotenv import load_dotenv #pip install python-dotenv

# Gather necessary information
## access token, project
print("-------------------------------------------------------------------")
print("Hear ye, hear ye: The todoist taskmaker program has been initiated.")
print("Please provide the information required to create your tasks.")
print("-------------------------------------------------------------------")

print("\nPlease specify your personal API token. It can be found under settings in your profile.")
print("If the access token is already specified in an .env variable; leave this empty (press ENTER).")
access_token = input("Access token>")

print("\nPlease specify the content (task name) of your tasks.")
print("If you want to make multiple tasks with a varying keyword, mark the location of the keyword with \"XXX\".")
content = input("Content (Task name)>").split("XXX")
#content = "Review XXX before lecture XXX.".split("XXX") #temporary

print("\nPlease specify what values to iteratively insert into your tasks. This will replace \"XXX\".")
print("Separate the values with a comma, no space, for example:")
print("1,2,3")
print("Adam,Bernadette,Charlie")
fill = input("fill values>").split(",")
#fill = "10,8,6".split(",") #temporary

# CREATE task content
generated_tasks = []
for i in fill:
    this_content = i.join(content)
    generated_tasks.append([this_content, ["Studying"], 1, "today"])

# Print summary
#print(tabulate(tasks, ["content", "label", "priority"], tablefmt="grid"))

# Run some checks before creating the tasks 
if len(generated_tasks) > 20:
    user_input = input("You are about to create more than 20 tasks, is that right? y/n>")
    if user_input == "n" or user_input != "y":
        print("Program exited.")
        quit()

# Get access token
if access_token == "":
    load_dotenv()
    api = TodoistAPI(os.getenv("ACCESS_KEY"))
else:
    api = TodoistAPI(access_token)

# CREATE TASKS
for task in generated_tasks:
    try:
        api.add_task(content=task[0], labels=task[1], priority=task[2], due_string=task[3])
    except Exception as error:
        print(error)

