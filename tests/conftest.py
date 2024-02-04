import pytest


def pytest_addoption(parser):
    parser.addoption("--speed", default="fast", choices=("fast", "full"))


@pytest.fixture
def speed(request):
    request.config.getoption("--speed")
