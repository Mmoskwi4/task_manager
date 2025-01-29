from typing import Dict
from dataclasses import dataclass


# Класс для управления задачами
@dataclass
class Task:
    id: int  # Идентификационный номер
    title: str  # Название
    description: str  # Описание
    category: str  # Категория
    due_date: str  # Время дедлайна
    priority: str  # Приоритет выполнения
    status: str = "Не выполнена"  # Статус выполнения при создании статус "Не выполнена"
    
    def to_dict(self) -> Dict:
        """
        Конвертирует объект Task в словарь для сохранения в JSON.
        """
        return self.__dict__

    @staticmethod
    def from_dict(data: Dict) -> "Task":
        """Создаёт объект Task из словаря."""
        return Task(**data)
