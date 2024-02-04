import pytest
from src.tools.filename_gen import filename_gen_fun
from datetime import datetime


@pytest.fixture
def get_data():
    date = datetime.now()
    return f"{date.day}_{date.month}_{date.year}"


@pytest.mark.parametrize(("json, result"), [(True, "get_data"), (False, "get_data")])
def test_filename_gen_fun(json, result, request):
    res = request.getfixturevalue(result)
    g = filename_gen_fun(json)
    if json:
        assert next(g) == res + ".json"
    else:
        assert next(g) == res + ".txt"
