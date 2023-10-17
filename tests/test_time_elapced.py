from asyncio import sleep

import pytest

from logrich import log

from pprint_tools.app import timer

skip = False
# skip = True
skipmark = pytest.mark.skipif(skip, reason="временно отключен.")


@skipmark
@timer(over=1.5)
@pytest.mark.anyio
async def test_duration_1() -> None:
    await sleep(1)
    # assert False
    log.debug("run async test next NO")


@skipmark
@timer(over=0.01)
@pytest.mark.anyio
async def test_duration_1_1() -> None:
    await sleep(0.1)
    # assert False
    log.debug("run async test next show")


@skipmark
@pytest.mark.anyio
@timer
def test_duration_2() -> None:
    log.debug("run test next NO")


@skipmark
@pytest.mark.anyio
@timer
async def test_duration_3() -> None:
    await sleep(1)
    log.debug("run async test show")


@skipmark
@pytest.mark.anyio
@timer
def test_duration_4() -> None:
    log.debug("run test next NO")


@skipmark
@timer(over=0.01)
@pytest.mark.anyio
async def test_duration_5() -> None:
    await sleep(0.1)
    # assert False
    log.debug("run async test next show")
