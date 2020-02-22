def test_async_frequency():
    # for python3.6+ only
    from asyncio import ensure_future, get_event_loop
    from time import time

    from frequency_controller import AsyncFrequency

    async def test_async():
        frequency = AsyncFrequency(2, 1)

        async def task():
            async with frequency:
                return time()

        now = time()
        tasks = [ensure_future(task()) for _ in range(5)]
        result = [await task for task in tasks]
        assert result[0] - now < 1
        assert result[1] - now < 1
        assert result[2] - now > 1
        assert result[3] - now > 1
        assert result[4] - now > 2

    get_event_loop().run_until_complete(test_async())
