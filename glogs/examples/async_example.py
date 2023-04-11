import asyncio

from glog import *


async def main():
    logs = ArizonaLogs('USERNAME', 'PASSWORD', 'GOOGLE_AUTH_SECRET')
    query = SearchQuery(22, player=14, types=[Type.CHECK, Type.DONATE])
    await logs.alogin()

    task1 = asyncio.ensure_future(logs.asearch(query))
    task2 = asyncio.ensure_future(logs.asearch(query))
    task3 = asyncio.ensure_future(logs.asearch(query))

    await task1
    await task2
    
    print(await task3)
    print('complete')


asyncio.run(main())
