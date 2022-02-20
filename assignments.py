"""
Assignment is one of:
- String (name of assignment)
- String (course)
- Month, Day, Year, & Time of due date
"""

class Assignment:
  def init(self, name, course, due_date):
    self.name = name
    self.course = course
    self.due_date = due_date

  def fn_for_assn(self):
    print(self.name + self.course + self.due_date)

A1 = Assignment("Problem Set 1", "CPSC 100" + "Jan 1st, 2021 : 23:59")
