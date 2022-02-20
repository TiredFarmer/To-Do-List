import assignments

# TODO list: a list of assignments
list_todo = []

LOA0 = []
LOA1 = [assignments.A1]
LOA2 = [assignments.A1, assignments.Assignment("Problem Set 2", "CPSC 100", "Jan 2nd, 2021"), assignments.Assignment("Problem Set 3", "CPSC 100", "Jan 3rd, 2021")]

def fn_for_todo(assn) -> list_todo:
  # adds a assignments to the todo list
  list_todo.append(assn)
