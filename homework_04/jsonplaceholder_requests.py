import aiohttp
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def get_users_data():
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, USERS_DATA_URL)


async def get_posts_data():
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, POSTS_DATA_URL)


async def main():
    users_data = await get_users_data()
    posts_data = await get_posts_data()

    print("Users data:", users_data)
    print("Posts data:", posts_data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
