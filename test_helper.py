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


def test_escape_quotes():
    result = helper.escape_quotes("das ist ein test")
    assert result == "das ist ein test"
    result = helper.escape_quotes('das ist "ein" test')
    assert result == 'das ist ""ein"" test'


def test_add_quotes():
    result = helper.add_quotes("das ist ein test")
    assert result == '"das ist ein test"'


def test_join_line():
    result = helper.join_line(["das", "ist", "ein", "test"])
    assert result == "das,ist,ein,test"


def test_get_item_csv():
    item = helper.Item('test "text"', datetime.date.today(), False)
    result = helper.get_item_csv(item)
    assert (
        result == '"test ""text""","' + datetime.date.today().isoformat() + '","False"'
    )


def test_get_csv(setUp):
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ('Sinn des "Lebens" entdecken', "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    for todo in todos:
        helper.add(todo[0], todo[1])

    # When: I export these items
    result = helper.get_csv()

    # Then: The following CSV string should be generated
    expectedLines = [
        '"text","date","isCompleted"',
        '"Sinn des ""Lebbbens"" entdecken","2023-09-01","False"',
        '"Universum debbbuggen","2023-09-06","False"',
        '"Superheld werden","2023-10-25","False"',
        '"Netto null","2050-01-01","False"',
    ]

    assert result == "\n".join(expectedLines)
