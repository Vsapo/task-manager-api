import json
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        max_id = max([task.id for task in self.tasks], default=0)
        task = Task(max_id + 1, title, priority)
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def mark_done(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.done = True

    def delete_task(self, task_id):
        task = self.find_task(task_id)

        if task:
            self.tasks.remove(task)
            return True

        return False

    def save_to_file(self, filename):
        data = []

        for task in self.tasks:
            data.append({
                "id": task.id,
                "title": task.title,
                "priority": task.priority,
                "done": task.done
            })

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.tasks = []

            for item in data:
                task = Task(item["id"], item["title"], item["priority"])
                task.done = item["done"]
                self.tasks.append(task)

        except FileNotFoundError:
            pass

    def search_tasks(self, query):
        result = []

        for task in self.tasks:
            if query.lower() in task.title.lower():
                result.append(task)

        return result

    def get_done_tasks(self):
        return [task for task in self.tasks if task.done]

    def get_undone_tasks(self):
        return [task for task in self.tasks if not task.done]

    def sort_by_priority(self):
        return sorted(self.tasks, key=lambda task: task.priority, reverse=True)

