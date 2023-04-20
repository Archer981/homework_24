import re
from typing import Iterator, Optional


def filter_query(data: list[str], query: str) -> list:
    return [line for line in data if query.lower() in line.lower()]


def map_query(data: list[str], query: str) -> list:
    return list(map(lambda x: x.split(' ')[int(query)], data))


def unique_query(data: list[str], query: None = None) -> list:
    return list(set(data))


def sort_query(data: list[str], query: str = 'asc') -> list:
    flag: bool = False if query == 'asc' else True
    return sorted([line for line in data], reverse=flag)


def limit_query(data: list[str], query: str) -> list:
    return [line for line in data][:int(query)]


def regex_query(data: list[str], query: str) -> Iterator:
    pattern: re.Pattern = re.compile(query)
    return filter(lambda x: re.search(pattern, x), data)
