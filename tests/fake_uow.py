from app.db.uow import UnitOfWork


class FakeAsyncSession:
    async def add(self, obj):
        pass

    async def execute(self, query, *args, **kwargs):
        pass


class FakeUnitOfWork(UnitOfWork):
    def __init__(self, session=FakeAsyncSession()):
        self.session = session

    def commit(self):
        pass

    def rollback(self):
        pass
