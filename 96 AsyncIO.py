# It execute parallay
# It give high performance


import time
import asyncio

async def func1():
    await asyncio.sleep(1)
    print("func 1")
    
async def func2():
    await asyncio.sleep(0)
    print("func 2")
    
async def func3():
    await asyncio.sleep(4)
    print("func 3")      
    
    
async def main():
    task=asyncio.create_task(func1())
#    await func1()
    await func2()
    await func3()    
    
    
asyncio.run(main())    