class Task:
    def __init__(self, id, title, priority):
        self.id = id
        self.title = title
        self.priority = priority
        self.done = False

    def __str__(self):
        return f"{self.id} | {self.title} | {self.priority} | {self.done}"