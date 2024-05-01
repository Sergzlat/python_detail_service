from .models import DetailL

class Mapper:
    def map(self, data, entity):
        if isinstance(entity, DetailL):
            entity.first_name = data.get('first_name')
            entity.middle_name = data.get('middle_name')
            entity.last_name = data.get('last_name')
            entity.birth_date = data.get('birth_date')
            entity.email = data.get('email')
            return entity

from datetime import datetime
from .models import DetailL

class Mapper:
    def map(self, data, model):
        for key, value in data.items():
            if hasattr(model, key):
                if isinstance(value, dict):
                    setattr(model, key, self.map(value, getattr(model, key)))
                elif isinstance(value, str) and key == 'birth_date':
                    setattr(model, key, datetime.fromisoformat(value))
                else:
                    setattr(model, key, value)
        return model
