import pytest
from src.tools.dataparser import DataParser


@pytest.fixture(scope="function")
def get_parser():
    parser = DataParser("https://yahoossfdas.com/news/rssd")
    return parser


@pytest.mark.skipif("config.getoption('--speed') == 'fast'", reason="slow test")
def test_get_data(get_parser):
    assert get_parser.get_data() is not None
