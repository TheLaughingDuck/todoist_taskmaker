from tabulate import tabulate

import regex
import itertools

# For api access
import api # custom module
import os
from dotenv import load_dotenv #pip install python-dotenv
load_dotenv()

### -----------VVV----------- CUSTOM FUNCTIONS -----------VVV----------- ###
def zip_recycle(iterable):
    """Takes an iterable, where each element is an iterable of elements.
    The iterables are zipped (by zip), but shorter elements are recycled.
    The longest element in fill_values will be gone through once."""
    
    # Regulate zip_recycle to stop once the longest element in fill_values has been passed once
    longest = max([len(x) for x in iterable])
    count = 0

    # Unpack list of recycled iterables.
    zipped_elements = zip(*[itertools.cycle(sublist) for sublist in iterable])
    for element in zipped_elements:
        yield element
        
        count += 1
        if count >= longest: break
### -----------^^^----------- CUSTOM FUNCTIONS -----------^^^----------- ###

### -----------VVV----------- GATHER TASK INFORMATION -----------VVV----------- ###
print("-------------------------------------------------------------------")
print("Hear ye, hear ye: The todoist taskmaker program has been initiated.")
print("Please provide the information required to create your tasks.")
print("-------------------------------------------------------------------")

print("\nPlease specify your personal API token. It can be found under settings in your profile.")
print("If the access token is already specified in an .env variable; leave this empty (press ENTER).")
access_token = input("Access token>")
access_token = os.getenv("ACCESS_KEY") if access_token == "" else access_token
print("-------------------------------------------------------------------")

print("\nPlease specify the content (task name) of your tasks.")
print("If you want to make multiple tasks with varying keywords, mark the location of the keywords with 3 identical uppercase letter, like \"XXX\", \"YYY\", or \"ZZZ\".")
print("You can use multiple keywords in order to cycle through different sets of values.")
content = input("Content (Task name)>")
print("-------------------------------------------------------------------")

# Find 3 identical uppercase letters, like AAA, BBB, but not ABA in content.
pattern = r'([A-Z])\1{2}'
fill_variables = [match.group(0) for match in regex.finditer(pattern, content)]

# Print fill variable "header"
if len(fill_variables) != 0:
    print("\nPlease specify the values of the respective fill variables below.")
    print("Separate the values with a comma, no space, for example:")
    print("1,2,3")
    print("Milk,Cheese,Bread")

# Specify fill values for each fill variable
fill_variable_values = []
for variable in fill_variables:
    print("\nPlease specify what values to iteratively replace", variable, "with.")
    fill_variable_values.append(input("fill values>").split(","))
    print("-------------------------------------------------------------------")
### -----------^^^----------- GATHER TASK INFORMATION -----------^^^----------- ###

### -----------VVV----------- CREATE TASKS -----------VVV----------- ###
# Generate list of tasks, containing their respective properties
generated_tasks = []
for fill_values in zip_recycle(fill_variable_values):
    # Make copy of content to replace variables with fill values
    content_i = content

    # Replace each variable with corresponding value
    for variable, value in zip(fill_variables, fill_values):
        content_i = content_i.replace(variable, value)
    
    # Save the generated task properties
    generated_tasks.append([content_i, ["Studying"], 1, "today"])

# Print summary of tasks
formated_tasks = [[title, ", ".join(labels), prio, due_string] for title, labels, prio, due_string in generated_tasks]
print(tabulate(formated_tasks, ["content", "label", "priority", "duestring"], tablefmt="grid"))

# Run some checks before creating the tasks 
if len(generated_tasks) > 20:
    user_input = input("You are about to create more than 20 tasks, is that right? y/n>")
    if user_input == "n" or user_input != "y":
        print("Program exited.")
        quit()

# Send task POST requests
api.POST_tasks(access_token, generated_tasks)
### -----------^^^----------- CREATE TASKS -----------^^^----------- ###