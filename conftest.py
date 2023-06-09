import pytest
from houseLab5 import House


@pytest.fixture
def conf_house():
    house = House('500/456849', 29, 45, 18, 7, 1, 'M.Bogdanovicha', 'Panel', 2012)
    return house