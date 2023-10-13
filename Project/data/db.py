import aiosqlite


class DataBase:
    def __init__(self):
        self.name = None
        self.conn = None

    async def create_connection(self) -> None:
        self.conn = await aiosqlite.connect('tg_users.db')

    async def create_table(self, name: str) -> None:
        self.name = name
        await self.conn.execute(f'CREATE TABLE IF NOT EXISTS {name}'
                                '(user_id TEXT,'
                                ' attemps INTEGER)')

    async def create_user(self, user_id: str, attemps: int) -> None:
        cursor = await self.conn.execute(f'SELECT user_id FROM {self.name} WHERE user_id={user_id}')
        if await cursor.fetchone() is None:
            await self.conn.execute(f'INSERT INTO {self.name} (user_id, attemps) VALUES(?, ?)', (user_id, attemps))
            await self.conn.commit()

    async def get_attemps(self, user_id: str) -> int:
        cursor = await self.conn.execute(f'SELECT attemps FROM {self.name} WHERE user_id={user_id}')
        return int(str(await cursor.fetchone()).replace('(', '').replace(',)', ''))

    async def update_user(self, user_id: str, new_attemps: int) -> None:
        await self.conn.execute(f'UPDATE {self.name} SET attemps={new_attemps} WHERE user_id={user_id}')
        await self.conn.commit()

    async def close(self) -> None:
        await self.conn.close()