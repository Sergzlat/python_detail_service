from dataclasses import dataclass
from typing import Any

@dataclass
class Mapper:
    @staticmethod
    def map(source: Any, destination: Any) -> Any:
        # Метод map из оригинального кода

from .models import DetailL

class Mapper:
    def map(self, data, entity):
        for key, value in data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        return entity

from datetime import datetime
from typing import List

class Mapper:
    def map(self, source, destination):
        for key, value in source.items():
            setattr(destination, key, value)
        return destination
