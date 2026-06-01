class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            return False
        self.tasks.append({"task": task, "completed": False})
        return True

    def get_tasks(self):
        return self.tasks

if __name__ == "__main__":
    print("--- Mi Lista de Tareas (ejercicio:3.0.0) ---")
    my_list = TodoList()
    my_list.add_task("Aprender GitHub Actions")
    my_list.add_task("Construir imagen Docker")
    
    for i, t in enumerate(my_list.get_tasks(), 1):
        print(f"{i}. {t['task']} - Completada: {t['completed']}")