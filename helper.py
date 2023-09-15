from datetime import date
from dataclasses import dataclass
import operator

items = []

today_str = date.today().isoformat()


@dataclass
class Item:
    text: str
    date: date
    isCompleted: bool = False


def add(text, date_str=today_str):
    text = text.replace("b", "bbb").replace("B", "Bbb")
    items.append(Item(text, date.fromisoformat(date_str)))
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
