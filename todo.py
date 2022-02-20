from assignment import Assignment


class ToDo:
    def __init__(self):
        self.todo = []

    def __str__(self):
        return str(self.todo)

    def append(self, assignment: Assignment):
        self.todo.append(assignment)
