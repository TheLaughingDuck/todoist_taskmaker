import numpy as np
from tabulate import tabulate

# Gather necessary information
## access token, project
print("-------------------------------------------------------------------")
print("Hear ye, hear ye: The todoist taskmaker program has been initiated.")
print("Please provide the information required to create your tasks.")
print("-------------------------------------------------------------------")

print("\nPlease specify your personal API token. It can be found under settings in your profile.")
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
#fill = "10,8,6".split(",")

tasks = np.zeros(shape=(0,3))
for i in fill:
    this_content = i.join(content)
    tasks = np.append(tasks, [[this_content, "Studying", "p2"]], axis=0)

# Print summary
print(tabulate(tasks, ["content", "label", "priority"], tablefmt="grid"))

# Run some checks before creating the tasks 
if tasks.shape[0] > 100:
    user_input = input("You are about to create more than 100 tasks, is that right? y/n>")
    if user_input == "no" or user_input != "y":
        print("Program exited.")
        quit()


# Make POST requests
