import asyncio
import aiomysql
from aiomysql import OperationalError


# 全局连接池（可提出放在单独的模块中）
async def create_global_pool():
    "创建连接池"
    return await aiomysql.create_pool(
        host="192.168.128.130",
        port="3306",
        user="root",
        password="root",
        db="test_db",
        mainsize=2,
        maxsize=10,
        autocommit=True,
    )


class AsyncMySQLManager:
    def __init__(self, pool):
        self.pool = pool

    async def __acenter__(self):
        """从全局连接池中获取连接"""
        self.conn = await self.pool.acquire()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """释放连接"""
        await self.pool.release(self.conn)
        if exc_type:
            print(f"异常：{exc_type}，信息：{exc_val}")
        return False


async def query_users(pool):
    async with AsyncMySQLManager(pool) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users")
            result = await cursor.fetchall()
            return result


async def main(): ...
