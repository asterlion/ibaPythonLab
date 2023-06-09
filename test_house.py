import pytest
from houseLab5 import House


@pytest.fixture
def my_local_house():
    my_local_house = House.getRandomHouse()
    print(my_local_house)
    return my_local_house

def test_get_number(conf_house):
    assert conf_house.get_number() == 29


def test_get_id(conf_house):
    assert conf_house.get_id() == '500/456849'


def test_get_street(conf_house):
    assert conf_house.get_street() == 'M.Bogdanovicha'

def test_get_year(conf_house):
    assert conf_house.get_year() == 2012


def test_getRandomHouse(my_local_house):
    assert  my_local_house is not None

