import asyncio
from random import randint


TASKS = 50


class Counter:
    def __init__(self, counter=0):
        self.__counter = counter

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, var):
        self.__counter = var

    def increment(self):
        self.counter += 1

    def __str__(self) -> str:
        return f"{self.counter}"


async def execute_io(number: int, counter: Counter) -> int:
    counter.increment()
    await asyncio.sleep(randint(0, 2))
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum


async def main():
    taskcounter = Counter()
    tasklist = [asyncio.create_task(execute_io(i, taskcounter)) for i in range(1, TASKS + 1)]
    task_sum = await asyncio.gather(*tasklist)
    print(f"Finish processing, result {sum(task_sum)}, counter {taskcounter}")


asyncio.run(main())
