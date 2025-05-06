
# import time

# def read_data():

#     print("entered into data read function")
#     time.sleep(5)
#     print("exiting from data read function")



# print("starting execution")
# read_data()
# print("calling data read function")
# print("this is tesing one")
# print("this is tesing second")
# print("this is tesing third")
# print("this is tesing fourth")
# print("this is tesing fifth")
# print("this is tesing sixth")
# time.sleep(10)

import asyncio

# async def read_data_ten():
#     print("entered into data read ten function")
#     await asyncio.sleep(10)
#     print("exiting from data read ten function")


# async def read_data():
#     print("entered into data read function")
#     await asyncio.sleep(5)
#     print("exiting from data read function")

# async def main():
#     print("starting execution")
    
#     # Start the read_data() function but don't wait immediately
#     task = asyncio.create_task(read_data())
#     task1 = asyncio.create_task(read_data_ten())

#     print("calling data read function")
#     print("this is testing one")
#     print("this is testing second")
#     print("this is testing third")
#     print("this is testing fourth")
#     print("this is testing fifth")
#     print("this is testing sixth")
    
#     # Now wait for read_data() to complete
#     await task1
#     await task

# asyncio.run(main())



import asyncio
import time

async def funct_eight():
    print("starting func eight")
    await asyncio.sleep(3)
    print("exiting  func eight")

async def funct_seven():
    print("starting func seven")
    await asyncio.sleep(3)
    print("exiting  func seven")

async def funct_six():
    print("starting func six")
    await asyncio.sleep(3)
    print("exiting  func six")

async def funct_five():
    print("starting func five")
    await asyncio.sleep(3)
    print("exiting  func five")

async def funct_four():
    print("starting func four")
    await asyncio.sleep(3)
    print("exiting  func four")

async def funct_three():
    print("starting func three")
    await asyncio.sleep(3)
    print("exiting  func three")

async def funct_two():
    print("starting func two")
    await asyncio.sleep(3)
    print("exiting  func two")

async def funct_one():
    print("starting func one")
    await asyncio.sleep(3)
    print("exiting  func one")



async def main():
    # Start both downloads at the same time

    # start_time = time.perf_counter()  # record start time
    task1 = asyncio.create_task(funct_eight())
    task2 = asyncio.create_task(funct_seven())
    task3 = asyncio.create_task(funct_six())
    task4 = asyncio.create_task(funct_five())
    task5 = asyncio.create_task(funct_four())
    task6 = asyncio.create_task(funct_three())
    task7 = asyncio.create_task(funct_two())
    task8 = asyncio.create_task(funct_one())

    # Wait for both to complete
    await task8
    await task7
    await task6
    await task5
    await task4
    await task3
    await task2
    await task1

start_time = time.perf_counter()
asyncio.run(main())
end_time = time.perf_counter()

print(end_time - start_time)


"""
Note:
key: asyncio.run(higher_function)
     create task  task = asyncio.create_task(asyn function call)
     await task
"""


# async def download_pic():

#     print("downloading pic")

# async def process_pic():

#     print("processing the download pic")

# async def main():

#     # create tasks 

#     task1 = asyncio.create_task(download_pic())
#     task2 = asyncio.create_task(process_pic)

# asyncio.run(main())
