import datetime

import helper
import pytest


def test_sort():
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i + 1].date


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)


@pytest.fixture
def setUp():
    helper.items.clear()


def test_update(setUp):
    helper.add("test")
    assert not helper.get(0).isCompleted
    helper.update(0)
    assert helper.get(0).isCompleted
    helper.update(0)
    assert not helper.get(0).isCompleted


def test_bbbization(setUp):
    helper.add("Baden")
    assert helper.get(-1).text == "Bbbaden"
    helper.add("baden")
    assert helper.get(-1).text == "bbbaden"
