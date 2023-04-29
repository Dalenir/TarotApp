from database.MongoDB.base_ensurance.maintainers import IndexMaintainer, StaticMaintainer


class BigBrother:
    maintainers: set[IndexMaintainer, StaticMaintainer]

    def __init__(self, *maintainers):
        self.maintainers = set(maintainers)

    async def database_setup(self, ensure_indexes: bool, refill_all: bool):
        if ensure_indexes:
            await self.ensure_indexes()
        if refill_all:
            await self.refill_all()

    async def refill_all(self):
        for maintainer in self.maintainers:
            if isinstance(maintainer, StaticMaintainer):
                await maintainer.refill()

    async def ensure_indexes(self):
        for maintainer in self.maintainers:
            if isinstance(maintainer, IndexMaintainer):
                await maintainer.ensure_indexes()
