from qb_db import qb_db
from match import match
from typing import List, Tuple, Callable, Any

def get_qbName(qb_db: Tuple[str, str, int, int, float, int, int, int]) -> str:
    return qb_db[0]


def get_director(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_actors(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]
