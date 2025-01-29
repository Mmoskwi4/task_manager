from task_manager import TaskManager


class Interface():
    def __init__(self, format_choice: str):
        storage_format = "json" if format_choice == "J" else "csv"
        self.manager = TaskManager("tasks." + storage_format, storage_format)

    def show_task(self):
        tasks = self.manager.show_tasks()
        if tasks:
            for task in tasks:
                print(task)
        return print("Задач нет.")
        
    def add_task(self):
        title = input("Название: ")
        description = input("Описание: ")
        category = input("Категория: ")
        due_date = input("Дата выполнения: ")
        priority = input("Приоритет (Низкий|Средний|Высокий): ")
        self.manager.add_task(title, description, category, due_date, priority)
        print("Задача добавлена.")

    def edit_task(self):
        try:
            task_id = int(input("ID задачи: "))
            task = next(
                (task for task in self.manager.tasks if task.id == task_id), None
            )
            if not task:
                print(f"\nЗадача с указанным ID не найдена.")
                print(f"\nДавай посмотрим что есть.")
                return self.show_task()

            print("1. Изменить поля")
            print("2. Изменить статус выполнения")
            
            update_choice = input("Выберите действие: ")

            def _change_fields():
                print("Оставьте поля пустыми, если не хотите их изменять.")
                title = input("Название: ")
                description = input("Описание: ")
                category = input("Категория: ")
                due_date = input("Дата выполнения: ")
                priority = input("Приоритет (Низкий|Средний|Высокий): ")

                updated_task = self.manager.edit_task(
                    task_id=task_id,
                    title=title if title.strip() else None,
                    description=description if description.strip() else None,
                    category=category if category.strip() else None,
                    due_date=due_date if due_date.strip() else None,
                    priority=priority if priority.strip() else None,
                )

                print("Задача обновлена")

            def _update_mark():
                message = self.manager.mark_task(task_id)
                print(message)

            update_dict = {
                '1': _change_fields,
                '2': _update_mark
            }


            update_dict.get(update_choice, self.other_choice)()
                

        except ValueError:
            print("Вводимый ID должен быть числом.")

    def delete_task(self):
        print("\nВыберите тип удаления:")
        print("1. Удалить задачу по ID")
        print("2. Удалить задачи в категории")

        delete_choice = input("Выберите действие: ")

        def _delete_id():
            try:
                task_id = int(input("Введите ID: "))
                message = self.manager.delete_task_by_id(task_id)
                print(message)
            except ValueError:
                print("Вводимый ID должен быть числом.")
        
        def _delete_category():
            category = input("Введите категорию: ")
            message = self.manager.delete_tasks_by_category(category)
            print(message)

        delete_dict = {
            '1': _delete_id,
            '2': _delete_category
        }

        delete_dict.get(delete_choice, self.other_choice)()
    
    def search_task(self):
        print("Выберите тип поиска:")
        print("1. Поиск по ID")
        print("2. Поиск по категории")
        print("3. Поиск по ключевому слову")

        search_choice = input("Выберите действие: ")

        def _id():
            try:
                task_id = int(input("ID задачи: "))
                task = self.manager.search_task_by_id(task_id)
                if task:
                    print("\nРезультат:")
                    print(task)
                else:
                    print("Задача с указанным ID не найдена.")
            except ValueError:
                print("Вводимый ID должен быть числом.")
            
        def _category():
            category = input("Введите категорию для поиска: ")
            tasks = self.manager.search_tasks_by_category(category)
            if tasks:
                print("\nРезультаты поиска по категории:")
                for task in tasks:
                    print(task)
            else:
                print("Задачи в указанной категории не найдены.")
        
        def _keyword():
            keyword = input("Введите ключевое слово для поиска: ")
            tasks = self.manager.search_tasks_by_keyword(keyword)
            if tasks:
                print("\nРезультаты поиска по ключевому слову:")
                for task in tasks:
                    print(task)
            else:
                print("Задачи с указанным ключевым словом не найдены.")

        search_dict = {
            '1': _id,
            '2': _category,
            '3': _keyword
        }

        search_dict.get(search_choice, self.other_choice)()

    def other_choice(self):
        print("Неверное действие.")