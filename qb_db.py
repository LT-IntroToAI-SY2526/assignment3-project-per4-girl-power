"""This database stores the data for the 2024 season NFL quarterbacks in the following format
[(String player, String team, int passing yards, int rushing yards, float completion percentage, 
int touchdowns, int interceptions thrown, int sacks)]
"""
from typing import List, Tuple

qb_db: List[Tuple[str, str, int, int, float, int, int, int]] = [
    (
        "kyler murray", #player name
        "arizona cardinals", #player's team
        3851, #passing yards
        572, #rushing yards
        68.8, #completion percentage
        21, #touchdowns
        11, #interceptions thrown
        30, #sacks
    ),
]