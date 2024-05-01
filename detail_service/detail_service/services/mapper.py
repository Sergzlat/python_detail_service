from dataclasses import dataclass
from typing import Any
from .models import DetailL
from datetime import datetime
from typing import List

@dataclass
class Mapper:
    @staticmethod
    def map(source: Any, destination: Any) -> Any:
        # Метод map из оригинального кода
        pass  # добавьте здесь свой код

class DetailLMapper(Mapper):
    def map(self, data, entity):
        for key, value in data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        return entity

class DateTimeMapper(Mapper):
    def map(self, source, destination):
        for key, value in source.items():
            setattr(destination, key, value)
