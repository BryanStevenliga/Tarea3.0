from app.todo import TodoList

def test_add_task():
    todo = TodoList()
    assert todo.add_task("Estudiar para el examen") == True
    assert len(todo.get_tasks()) == 1

def test_add_empty_task():
    todo = TodoList()
    assert todo.add_task("") == False