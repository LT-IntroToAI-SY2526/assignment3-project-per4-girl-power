from quarterbacks import qb_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "quarterback" (a tuple)
def get_player(quarterback):
    return(qb[0])
def get_team(quarterback):
    return(qb[1])
def get_division(quarterback):
    return(qb[2])
def get_pass_yds(quarterback):
    return(qb[3])
def get_comp_pct(quarterback):
    return(qb[4])
def get_tds(quarterback):
    return(qb[5])
def get_inters(quarterback):
    return(qb[6])
def get_sacks(quarterback):
    return(qb[7])

# STATS BY PLAYER NAME

# what team did % play for
def team_by_qb(matches):
    search_qb = matches[0]
    for quarterback in qb_db:
        if get_player(quarterback) == search_qb:
            return [get_team(quarterback)]
    return []

# how many passing yards did % have
def pass_yds_by_qb(matches):
    search_qb = matches[0]
    for quarterback in qb_db:
        if get_player(quarterback) == search_qb:
            return [get_pass_yds(quarterback)]
    return []

# what was %'s completion percentage
def comp_pct_by_qb(matches): 
    search_qb = matches[0]
    for quarterback in qb_db:
        if get_player(quarterback) == search_qb:
            return [get_comp_pct(quarterback)]
    return []

# how many touchdowns did % have
def tds_by_qb(matches):
    search_qb = matches[0]
    for quarterback in qb_db:
        if get_player(quarterback) == search_qb:
            return [get_comp_pct(quarterback)]
    return []

# how many interceptions did % throw
def inters_by_qb(matches):
    search_qb = matches[0]
    for quarterback in qb_db:
        if get_player(quarterback) == search_qb:
            return [get_inters(quarterback)]
    return []

# how many sacks did % take
def sacks_by_qb(matches):
    search_qb = matches[0]
    for quarterback in qb_db:
        if get_player(quarterback) == search_qb:
            return [get_sacks(quarterback)]
    return []

# QBS WITH THRESHOLD STATS
# what quarterbacks had more than _ touchdowns
    # qbs_with_more_tds(matches[0])
    # returns List[str]
# what quarterbacks had more than _ passing yards
    # qbs_with_more_pass_yds(matches[0])
    # returns List[str]
# what quarterbacks had fewer than _ interceptions
    # qbs_with_fewer_inters(matches[0])
    # returns List[str]
# what quarterbacks had fewer than _ sacks
    # qbs_with_fewer_sacks(matches[0])
    # returns List[str]

# DIVISION SUPERLATIVES
# who in the % had the most passing yards
    # qb_with_most_pass_yds_in_division(matches[0])
    # returns List[str]
# who in the % threw the most touchdowns
    # qb_with_most_tds_in_division(matches[0])
    # returns List[str]
# who in the % had the fewest interceptions
    # qb_with_fewest_inters_in_division(matches[0])
    # returns List[str]
