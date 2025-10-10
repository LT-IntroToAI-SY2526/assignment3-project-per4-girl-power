from  quarterbacks import qb_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "quarterback" (a tuple)
def get_player(quarterback):
    return(quarterback[0])
def get_team(quarterback):
    return(quarterback[1])
def get_division(quarterback):
    return(quarterback[2])
def get_pass_yds(quarterback):
    return(quarterback[3])
def get_comp_pct(quarterback):
    return(quarterback[4])
def get_tds(quarterback):
    return(quarterback[5])
def get_inters(quarterback):
    return(quarterback[6])
def get_sacks(quarterback):
    return(quarterback[7])

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
            return [get_tds(quarterback)]
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
def qbs_with_more_tds(matches):
    result = []
    min_tds = int(matches[0])
    for quarterback in qb_db:
       if(get_tds(quarterback) > min_tds):
           result.append(get_player(quarterback))
    return result

    
# what quarterbacks had more than _ passing yards
    # qbs_with_more_pass_yds(matches[0])
    # returns List[str]
def qbs_with_more_pass_yds(matches):
    result = []
    min_pass_yds = int(matches[0])
    for quarterback in qb_db:
        if(get_pass_yds(quarterback) > min_pass_yds):
            result.append(get_player(quarterback))
    return result

# what quarterbacks had fewer than _ interceptions
    # qbs_with_fewer_inters(matches[0])
def qbs_with_fewer_inters(matches):
    result = []
    max_inters = int(matches[0])
    for quarterback in qb_db:
       if(get_inters(quarterback) < max_inters):
           result.append(get_player(quarterback))
    return result


    # returns List[str]


# what quarterbacks had fewer than _ sacks
    # qbs_with_fewer_sacks(matches[0])
    # returns List[str]
def qbs_with_fewer_sacks(matches):
    result = []
    max_sacks = int(matches[0])
    for quarterback in qb_db:
       if(get_sacks(quarterback) < max_sacks):
           result.append(get_player(quarterback))
    return result
    
            
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

# BYE ACTION
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what team did % play for"), team_by_qb),
    (str.split("how many pass yards did % have"), pass_yds_by_qb),
    (str.split("what was %'s completion percentage"), comp_pct_by_qb),
    (str.split("how many touchdowns did % have"), tds_by_qb),
    (str.split("how many interceptions did % throw"), inters_by_qb),
    (str.split("how many sacks did % take"), sacks_by_qb),
    (str.split("what quarterbacks had more than _ touchdowns"), qbs_with_more_tds),
    (str.split("what quarterbacks had more than _ passing yards"), qbs_with_more_pass_yds),
    (str.split("what quarterbacks had fewer than _ interceptions"), qbs_with_fewer_inters),
    (str.split("what quarterbacks had fewer than _ sacks"), qbs_with_fewer_sacks),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pattern, action in pa_list:
        result_matches = match(pattern, src)
        
        if result_matches is not None:
            # Found a matching pattern
            try:
                answers = action(result_matches)
                
                # Handle None return
                if answers is None:
                    return ["No answers"]
                
                # Handle empty list
                if len(answers) == 0:
                    return ["No answers"]
                
                # Convert all answers to strings
                return [str(answer) for answer in answers]
            
            except KeyboardInterrupt:
                # bye_action raises this
                raise
    
    # No pattern matched
    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the quarterback database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")
query_loop()