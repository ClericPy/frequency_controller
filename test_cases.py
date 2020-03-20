from frequency_controller import Frequency, AsyncFrequency


def test_sync_frequency():
    from concurrent.futures import ThreadPoolExecutor
    from time import time

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
    assert frequency.to_dict() == {'n': 2, 'interval': 1}
    assert frequency.to_list() == [2, 1]


def test_async_frequency():
    if AsyncFrequency is not None:
        from _test_py3_cases import test_async_frequency
        test_async_frequency()


if __name__ == "__main__":
    test_sync_frequency()
    test_async_frequency()
