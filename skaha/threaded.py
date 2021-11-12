"""General purpose threaded scaler."""
import asyncio
import concurrent.futures
from functools import partial
from typing import Callable, List


async def scale(
    function: Callable,
    arguments: List[dict] = [{}],
) -> list:
    """Scales a function across multiple threads.

    Args:
        function (Callable): The function to be scaled.
        arguments (List[dict], optional): The arguments to be passed to each
            function, by default [{}]

    Returns:
        list: The results of the function.

    """
    workers = len(arguments)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, partial(function, **arguments[index]))
            for index in range(workers)
        ]
        return await asyncio.gather(*futures)
