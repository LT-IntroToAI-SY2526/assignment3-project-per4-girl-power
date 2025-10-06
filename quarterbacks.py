"""This database stores the data for the 2024 season NFL quarterbacks in the following format:
[(str player, str team, str division, int passing yards, float completion percentage, int touchdowns, 
int interceptions thrown, int sacks)]
"""
from typing import List, Tuple

qb_db: List[Tuple[str, str, str, int, float, int, int, int]] = [
    ("kyler murray", "arizona cardinals", "nfc west", 3851, 68.8, 21, 11, 30),
    ("kirk cousins", "atlanta falcons", "nfc south", 3508, 66.9, 18, 16, 28),
    ("josh allen", "buffalo bills", "afc east", 3731, 63.6, 28, 6, 14),
    ("bryce young", "carolina panthers", "nfc south", 2403, 60.9, 15, 9, 29),
    ("caleb williams", "chicago bears", "nfc north", 3541, 62.5, 20, 6, 68),
    ("joe burrow", "cincinnati bengals", "afc north", 4918, 70.6, 43, 9, 48),
    ("jameis winston", "cleveland browns", "afc north", 2121, 61.2, 13, 12, 24),
    ("dak prescott", "dallas cowboys", "nfc east", 1978, 64.7, 11, 8, 21),
    ("bo nix", "denver broncos", "afc west", 3775, 66.3, 29, 12, 24),
    ("jared goff", "detroit lions", "nfc north", 4629, 72.4, 37, 12, 31),
    ("jordan love", "green bay packers", "nfc north", 3389, 63.1, 25, 11, 14),
    ("c.j. stroud", "houston texans", "afc south", 3727, 63.2, 20, 12, 52),
    ("anthony richardson", "indianapolis colts", "afc south", 1814, 47.7, 8, 12, 14),
    ("trevor lawrence", "jacksonville jaguars", "afc south", 2045, 60.6, 11, 7, 18),
    ("patrick mahomes", "kansas city chiefs", "afc west", 3928, 67.5, 26, 11, 36),
    ("gardner minshew", "las vegas raiders", "afc west", 2013, 66.3, 9, 10, 29),
    ("justin herbert", "los angeles chargers", "afc west", 3870, 65.9, 23, 3, 41),
    ("matthew stafford", "los angeles rams", "nfc west", 3762, 65.8, 20, 8, 28),
    ("tua tagovailoa", "miami dolphins", "afc east", 2867, 72.9, 19, 7, 21),
    ("sam darnold", "minnesota vikings", "nfc north", 4319, 66.2, 35, 12, 48),
    ("drake maye", "new england patriots", "afc east", 2276, 66.6, 15, 10, 34),
    ("spencer rattler", "new orleans saints", "nfc south", 1317, 57.0, 4, 5, 22),
    ("daniel jones", "new york giants", "nfc east", 2070, 63.3, 8, 7, 29),
    ("aaron rodgers", "new york jets", "afc east", 3897, 63.0, 28, 11, 40),
    ("jalen hurts", "philadelphia eagles", "nfc east", 2903, 68.7, 18, 5, 38),
    ("russell wilson", "pittsburgh steelers", "afc north", 2482, 63.7, 16, 5, 33),
    ("brock purdy", "san francisco 49ers", "nfc west", 3864, 65.9, 20, 12, 31),
    ("geno smith", "seattle seahawks", "nfc west", 4320, 70.4, 21, 15, 50),
    ("baker mayfield", "tampa bay buccaneers", "nfc south", 4500, 71.4, 41, 16, 40),
    ("will levis", "tennessee titans", "afc south", 2091, 63.1, 13, 12, 41),
    ("jayden daniels", "washington commanders", "nfc east", 3568, 69.0, 25, 9, 47),
]
