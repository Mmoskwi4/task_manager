from cli import Interface


# Основная программа
def main():
    print("Выберите формат хранения данных:")
    print("J. JSON")
    print("C. CSV")
    format_choice = input("Введите номер формата: ")
    interface = Interface(format_choice)

    while True:
        print("\nМеню:")
        print("1. Просмотр задач")
        print("2. Добавить задачу")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("0. Выход")

        choice = input("Выберите действие: ")

        menu_dict = {
            '1': interface.show_task,
            '2': interface.add_task,
            '3': interface.edit_task,
            '4': interface.delete_task,
            '5': interface.search_task,
        }

        menu_dict.get(choice, interface.other_choice)()

        if choice == "0":
            break

if __name__ == "__main__":
    main()