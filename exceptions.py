class IncorrectInput(Exception):
    def __str__(self):
        return 'Podano nieprawidłową wartość.'


class FieldTaken(Exception):
    def __str__(self):
        return 'Wybrane pole jest już zajęte.'
