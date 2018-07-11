import asyncio
import json

from poeRPC import PoeRPC

with open('config.json') as f:
    js = json.load(f)

loop = asyncio.ProactorEventLoop()
cl = PoeRPC(loop, js['name'])
#print(dir(loop))
loop.run_until_complete(cl.init())
loop.run_forever()