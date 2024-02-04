import pytest
from src.tools.logger import init_logger


class TestLoggingInit:
    @pytest.mark.parametrize(
        "name, result",
        [("test", "test"), ("test123", "test123"), ("supername", "supername")],
    )
    def test_init_logger_name(self, name, result):
        logger = init_logger(name, "INFO")
        assert logger.name == result

    @pytest.mark.parametrize(
        "level, result",
        [("INFO", 20), ("DEBUG", 10), ("WARNING", 30)],
    )
    def test_init_logger_level(self, level, result):
        logger = init_logger("test", level)
        assert logger.level == result
