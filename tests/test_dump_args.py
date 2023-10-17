import pytest
from anyio import sleep
from logrich import log

from pprint_tools.app import dump_args

skip = False
# skip = True
skipmark = pytest.mark.skipif(skip, reason="временно отключен.")


@skipmark
@pytest.mark.anyio
@pytest.mark.parametrize(
    argnames=("skip_dump",),
    argvalues=[
        pytest.param(True),
        pytest.param(False),
    ],
)
async def test_func_1(skip_dump: bool) -> None:
    """Test dump func args."""

    @dump_args(skip=skip_dump)
    def mysum(a=7, b=5, c=10):  # noqa WPS430
        log.run("run sum")
        return a + b

    # return
    resp = mysum(a=35)
    log.debug(resp)
    # return
    assert resp == 40

    resp = mysum(37)
    log.debug(resp)
    assert resp == 42

    @dump_args(skip=skip_dump)
    async def async_my_sum(a=7, b=5):  # noqa WPS430
        await sleep(1)
        log.run("run async sum")
        return a + b

    resp = await async_my_sum(a=31)
    log.info(resp)
    assert resp == 36

    resp = await async_my_sum(77, 23)
    log.info(resp)
    assert resp == 100

    @dump_args
    async def async_my_sum_2(a=7, b=15):  # noqa WPS430
        log.run("run async sum_2")
        return a + b

    resp = await async_my_sum_2(61, b=13)
    log.info(resp)
    assert resp == 74
