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


def get_csv():
    csv = []
    csv.append(
        join_line([add_quotes("text"), add_quotes("date"), add_quotes("isCompleted")])
    )
    for item in items:
        csv.append(get_item_csv(item))
    return "\n".join(csv)


def join_line(line):
    return ",".join(line)


def get_item_csv(item):
    return join_line(
        [
            add_quotes(escape_quotes(item.text)),
            add_quotes(item.date.isoformat()),
            add_quotes(str(item.isCompleted)),
        ]
    )


def add_quotes(input):
    return '"' + input + '"'


def escape_quotes(input):
    return input.replace('"', '""')
