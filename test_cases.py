import sys
if sys.version_info.major > 2:
    from _test_py3_cases import test_async_frequency
    test_async_frequency()


def test_sync_frequency():
    from concurrent.futures import ThreadPoolExecutor
    from time import time

    from frequency_controller.sync_tools import Frequency
    # limit to 2 concurrent tasks each 1 second
    frequency = Frequency(2, 1)

    def test():
        with frequency:
            return time()

    now = time()
    pool = ThreadPoolExecutor()
    tasks = []
    for _ in range(5):
        tasks.append(pool.submit(test))
    result = [task.result() for task in tasks]
    assert result[0] - now < 1
    assert result[1] - now < 1
    assert result[2] - now > 1
    assert result[3] - now > 1
    assert result[4] - now > 2


if __name__ == "__main__":
    test_sync_frequency()
