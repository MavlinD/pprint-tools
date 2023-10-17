from typing import Generator

from _pytest import nodes


import pytest
from logrich.app import console


def pytest_runtest_call(item: nodes.Item) -> None:
    # https://docs.pytest.org/en/6.2.x/reference.html
    console.rule(f"[green]{item.parent.name}[/]::[yellow bold]{item.name}[/]")  # type: ignore


@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir) -> Generator:
    """Fixture to execute asserts before and after a test is run"""
    # https://localcoder.org/run-code-before-and-after-each-test-in-py-test
    print()
    yield


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """Pointer for anyio."""
    return "asyncio"
