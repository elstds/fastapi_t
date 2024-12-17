from asyncio import current_task
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine, async_sessionmaker
from core.config import settings

class DatabaseHelper():
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind = self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


    def get_scope_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session


    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()


    async def scope_session_dependency(self) -> AsyncSession:
        session = self.get_scope_session()
        yield session
        session.close()


db_h = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)