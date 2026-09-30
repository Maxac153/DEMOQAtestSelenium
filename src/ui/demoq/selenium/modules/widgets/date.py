from dataclasses import dataclass


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
