from dataclasses import dataclass


@dataclass
class Memregion:
    start: int
    end: int


@dataclass
class Memlayout:
    name: str
    mems: list[Memregion]
