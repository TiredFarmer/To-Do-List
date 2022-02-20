class Assignment:
    def __init__(self, name: str, course: str, due_date: str, due_time: str):
        self.name = name
        self.course = course
        self.due_date = due_date
        self.due_time = due_time

    def __str__(self):
        return f"Assignment({self.name} {self.course} {self.due_date} {self.due_time})"


A1 = Assignment("Problem Set 1", "CPSC 100" + "2022/01/01" + "23:59")
