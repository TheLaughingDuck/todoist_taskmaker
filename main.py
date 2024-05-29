from helpers import zip_recycle, POST_tasks
from user_interaction import get_POST_information
from tabulate import tabulate

print("-------------------------------------------------------------------")
print("Hear ye, hear ye: The todoist taskmaker program has been initiated.")
print("Please provide the information required to create your tasks.")
print("-------------------------------------------------------------------")

# GET TASK INFORMATION FROM USER
task_info = get_POST_information()

# FILL IN missing values
if task_info["token"] == "":
    from os import getenv
    from dotenv import load_dotenv #pip install python-dotenv
    load_dotenv()
    access_token = getenv("ACCESS_KEY")

### -----------VVV----------- CREATE TASKS -----------VVV----------- ###
# Generate list of tasks, containing their respective properties
generated_tasks = []
for fill_values in zip_recycle(task_info["fill"].values()):
    # Make copy of content to replace variables with fill values
    content_i = task_info["task"]

    # Replace each variable with corresponding value
    for variable, value in zip(task_info["fill"].keys(), fill_values):
        content_i = content_i.replace(variable, value)
    
    # Save the generated task properties
    generated_tasks.append([content_i, task_info["labels"], task_info["priority"], task_info["due"]])

# Print summary of tasks
formated_tasks = [[title, ", ".join(labels), prio, due_string] for title, labels, prio, due_string in generated_tasks]
print(tabulate(formated_tasks, ["content", "label", "priority", "duestring"], tablefmt="grid"))

# Let user review and accept/cancel the task creation
print("\nPlease review the tasks in the table above before sending them to the API.")
user_input = input("Create tasks [y/n]?>")
if user_input == "y":
    # Send task POST requests
    POST_tasks(access_token, generated_tasks)
else:
    print("\nTask creation was cancelled by user.")
    quit()
### -----------^^^----------- CREATE TASKS -----------^^^----------- ###