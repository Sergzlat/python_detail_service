from models import DetailL
from datetime import datetime

class DetailLValidator:
    @staticmethod
    def validate_detail_l(data):
        errors = []

        if 'first_name' not in data or not data['first_name']:
            errors.append("First name is required.")

        if 'last_name' not in data or not data['last_name']:
            errors.append("Last name is required.")

        if 'birth_date' not in data or not data['birth_date']:
            errors.append("Birth date is required.")
        else:
            try:
                birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
                if birth_date > datetime.now():
                    errors.append("Birth date cannot be in the future.")
            except ValueError:
                errors.append("Invalid birth date format. Use YYYY-MM-DD.")

        return errors

