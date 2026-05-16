import json
import os
from datetime import datetime

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({
        "id": len(tasks) + 1,
        "task": task,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_tasks(tasks)
    print(f"✅ Added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet!")
        return
    for t in tasks:
        status = "✅" if t["done"] else "⭕"
        print(f"{status} [{t['id']}] {t['task']} ({t['created']})")

def done_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            print(f"🎉 Completed: {t['task']}")
            break
    save_tasks(tasks)

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"🗑️ Deleted task {task_id}")

def show_menu():
    print("\n" + "="*40)
    print("📝 TASK TRACKER")
    print("="*40)
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark done")
    print("4. Delete task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose (1-5): ")
        
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("Task ID to mark done: "))
            done_task(task_id)
        elif choice == '4':
            task_id = int(input("Task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()