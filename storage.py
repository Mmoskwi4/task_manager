import json
import csv
from task import Task
from typing import List


# Класс определяющий хранения
class Storage:
    def __init__(self, file_path: str, format: str):
        """
        Определяют формат хранения
        """
        self.file_path = file_path
        self.format = format.lower()
        if self.format not in ["json", "csv"]:
            raise ValueError("Доступны только JSON и CSV.")
  
    def load_tasks(self) -> List[Task]:
        """
        Загружает данные в выбранном формате
        """
        if self.format == "json":
            return self._load_json()
        elif self.format == "csv":
            return self._load_csv()

    def save_tasks(self, tasks: List[Task]):
        """
        Сохраняет данные в выбранном формате
        """
        if self.format == "json":
            self._save_json(tasks)
        elif self.format == "csv":
            self._save_csv(tasks)

    def _load_json(self) -> List[Task]:
        """
        Внутренняя функия для загрузки и
        создания пустого файла в формате JSON
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("Ошибка при загрузке данных из JSON.")

    def _save_json(self, tasks: List[Task]):
        """
        Внутренняя функия для сохранения файла в формате JSON
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4
            )

    def _load_csv(self) -> List[Task]:
        """
        Внутренняя функия для загрузки
        и создания пустого файла в формате CSV
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []
        except csv.Error:
            raise ValueError("Ошибка при загрузке данных из CSV.")

    def _save_csv(self, tasks: List[Task]):
        """
        Внутренняя функия для сохранения файла в формате CSV
        """
        with open(self.file_path, "w", encoding="utf-8", newline="") as file:
            fieldnames = [
                "id",
                "title",
                "description",
                "category",
                "due_date",
                "priority",
                "status",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
