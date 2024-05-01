class DetailLNotFoundException(Exception):
    def __init__(self, message="DetailL not found"):
        self.message = message
        super().__init__(self.message)


class DeletedDetailLNotFoundException(Exception):
    def __init__(self, message="Deleted DetailL not found"):
        self.message = message
        super().__init__(self.message)

