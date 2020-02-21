# frequency_controller [![PyPI version](https://badge.fury.io/py/frequency_controller.svg)](https://badge.fury.io/py/frequency_controller)[![Downloads](https://pepy.tech/badge/frequency_controller)](https://pepy.tech/project/frequency_controller)
Limitations of frequency. Code snippets copy from [torequests](https://github.com/ClericPy/torequests).


## Intro

> 1. There are many implementations for frequency-control, the generator way is better than using a Queue
>    1. Queue instances use more memory
>    2. Queue initial process is slower than create a generator
> 2. Python3.8+ required the lock protection for async-generators.
>    1. https://bugs.python.org/issue38559
>    2. But 3.6 / 3.7 do not have this feature
> 3. Using timeit.default_timer for a better accuracy but little performance lost.
>    1. Frequency.TIMER = timeit.default_timer

## Install

> pip install -U frequency_controller

## Quick Start

### 1. Multi-Thread Demo

```python
from frequency_controller.sync_tools import Frequency
from threading import Thread
from time import strftime


def sync_demo():
    # limit to 2 concurrent tasks each 1 second
    frequency = Frequency(2, 1)

    def test():
        with frequency:
            print(strftime('%Y-%m-%d %H:%M:%S'))

    threads = [Thread(target=test) for _ in range(5)]
    for t in threads:
        t.start()


if __name__ == "__main__":
    sync_demo()
    # 2020-02-21 18:35:43
    # 2020-02-21 18:35:43
    # 2020-02-21 18:35:44
    # 2020-02-21 18:35:44
    # 2020-02-21 18:35:45
```

### 2. Coroutine Demo

```python
from asyncio import ensure_future, get_event_loop, wait
from time import strftime

from frequency_controller.async_tools import Frequency


async def async_demo():
    frequency = Frequency(2, 1)

    async def task():
        async with frequency:
            print(strftime('%Y-%m-%d %H:%M:%S'))

    tasks = [ensure_future(task()) for _ in range(5)]
    await wait(tasks)


if __name__ == "__main__":
    # python3.7 use asyncio.run
    get_event_loop().run_until_complete(async_demo())
    # 2020-02-21 18:43:51
    # 2020-02-21 18:43:51
    # 2020-02-21 18:43:52
    # 2020-02-21 18:43:52
    # 2020-02-21 18:43:53
```
