import os
from todoist_api_python.api import TodoistAPI
from env import API_TOKEN, get_today, CHECKBOX, OUT_DIR

def limit_to_active_tasks(tasks: list) -> list:
    active_tasks: list = []
    for i in range(0, len(tasks)):
        if(tasks[i].due != None and tasks[i].due.date == get_today()):
            active_tasks.append(tasks[i])
    return active_tasks

def create_text(tasks: list, reflection=""):
    text_to_write = f"**Today: {get_today()}**\n{reflection}\n"
    for t in tasks:
        text_to_write += f"{CHECKBOX} {t.content}\n"
    
    with open(OUT_DIR, "w") as text:
        text.write(text_to_write)
            
def main():
    api = TodoistAPI(API_TOKEN)
    
    tasks = limit_to_active_tasks(api.get_tasks())
    reflection = ""
    choice = input("would you like to reflect? ")
    if(choice != "n"):
        reflection = input("write: ")
    
    create_text(tasks, reflection)

if(__name__ == "__main__"):
    main()
