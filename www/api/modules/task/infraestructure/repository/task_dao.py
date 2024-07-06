from ...domain.entity import TaskStatus


class TaskDAO:

    def __init__(self, db):
        self.db = db

    def create(self, name: str, description: str, status: TaskStatus):
        pass
