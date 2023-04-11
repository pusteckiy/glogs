![](https://i.imgur.com/Kfck70e.png)

## Info
A small script to interact with [arizonarp.logsparser.info](arizonarp.logsparser.info) more easily.
## Usage/Examples


You can use both synchronous:
```python
from glog import *

logs = ArizonaLogs('USERNAME', 'PASSWORD', 'GOOGLE_AUTH_SECRET')
query = SearchQuery(server=22, player=14, types=[Type.ADMIN_SALARY])
logs.login()
result = logs.search(query)
```

And asynchronous options:
```python
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
    await task3


asyncio.run(main())

```
