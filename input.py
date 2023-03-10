'''
   Have a look at the constraints in optimize.py to see exactly what kind of inequality it is (==, >=, <=).
   Also check what kind of cards are present in the dataset. For example no Icons and Heroes are there in the dataset.
'''

'''INPUTS'''

FORMATION = "3-4-3"

# Currently only works for 11 players :)
NUM_PLAYERS = 11

FIX_PLAYERS  = 1 # FIX_PLAYERS = 1 => players will be picked based on the formation and 0 otherwise.
         
COUNTRY = ["England", "Spain"]
NUM_COUNTRY = 11 # Total players from above countries >= NUM_COUNTRY

MAX_NUM_COUNTRY = 5  # Maximum from same country
NUM_UNIQUE_COUNTRY = 0  # Nations: Max/Min X
MIN_NUM_COUNTRY = 5  # Same Nation Count: Min X

LEAGUE = ["Premier League", "LaLiga Santander"]
NUM_LEAGUE = 11  # Total players from above leagues >= NUM_LEAGUE

MAX_NUM_LEAGUE = 4  # Maximum from same league
NUM_UNIQUE_LEAGUE = 4  # Leagues: Max/Min X
MIN_NUM_LEAGUE = 4  # Same League Count: Min X

CLUB = ["Real Madrid"]
NUM_CLUB = 1  # Total players from above clubs >= NUM_CLUB

MAX_NUM_CLUB = 2  # Maximum from same club
NUM_UNIQUE_CLUB = 5  # Clubs: Max/Min X
MIN_NUM_CLUB = 2  # Same Club Count: Min X

RARITY_1 = [['gold', 'TOTW']]  # len(RARITY_1) == len(NUM_RARITY_1)
NUM_RARITY_1 = [1]  # This is for cases like "Gold IF: Min X (0/X)"

RARITY_2 = ["Rare", "gold"]  # len(RARITY_2) == len(NUM_RARITY_2)
NUM_RARITY_2 = [11, 11]   # This is for cases like "Rare: Min X (0/X)""
                 
SQUAD_RATING = 81      # Squad Rating: Min XX

MIN_OVERALL = [83]     # len(MIN_OVERALL) == len(NUM_MIN_OVERALL)
NUM_MIN_OVERALL = [1]  # Minimum OVR of XX : Min X

CHEMISTRY = 24  # Squad Total Chemistry Points: Min X
               # Currently doesn't work for Icons and Heroes
               # If there is no constraint on total chemistry, then set this to 0. 
               # Will work properly only if FIX_PLAYERS = 1

CHEM_PER_PLAYER = 0  # Chemistry Points Per Player: Min X

'''INPUTS'''

formation_dict = {
    "3-4-1-2": ["GK", "CB", "CB", "CB", "LM", "CM", "CM", "RM", "CAM", "ST", "ST"],
    "3-4-2-1": ["GK", "CB", "CB", "CB", "LM", "CM", "CM", "RM", "CF", "ST", "CF"],
    "3-1-4-2": ["GK", "CB", "CB", "CB", "LM", "CM", "CDM", "CM", "RM", "ST", "ST"],
    "3-4-3": ["GK", "CB", "CB", "CB", "LM", "CM", "CM", "RM", "CAM", "ST", "ST"],
    "3-5-2": ["GK", "CB", "CB", "CB", "CDM", "CDM", "LM", "CAM", "RM", "ST", "ST"],
    "4-3-3": ["GK", "LW", "ST", "RW", "CM", "CAM", "CM", "LB", "RB", "CB", "CB"],
    "3-4-3": ["GK", "CB", "CB", "CB", "LM", "CM", "CM", "RM", "LW", "ST", "RW"],
    "4-1-2-1-2": ["GK", "LB", "CB", "CB", "RB", "CDM", "LM", "CAM", "RM", "ST", "ST"],
    "4-1-2-1-2[2]": ["GK", "LB", "CB", "CB", "RB", "CDM", "CM", "CAM", "CM", "ST", "ST"],
    "4-1-4-1": ["GK", "LB", "CB", "CB", "RB", "CDM", "LM", "CM", "CM", "RM", "ST"],
    "4-2-3-1": ["GK", "LB", "CB", "CB", "RB", "CDM", "CDM", "CAM", "CAM", "CAM", "ST"],
    "4-2-3-1[2]": ["GK", "LB", "CB", "CB", "RB", "CDM", "CDM", "CAM", "LM", "ST", "RM"],
    "4-2-2-2": ["GK", "LB", "CB", "CB", "RB", "CDM", "CDM", "CAM", "CAM", "ST", "ST"],
    "4-2-4": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "LW", "ST", "ST", "RW"],
    "4-3-1-2": ["GK", "CB", "CB", "LB", "RB", "CM", "CM", "CM", "CAM", "ST", "ST"],
    "4-1-3-2": ["GK", "LB", "CB", "CB", "RB", "CDM", "LM", "CM", "RM", "ST", "ST"],
    "4-3-2-1": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "CM", "CF", "ST", "CF"],
    "4-3-3": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "CM", "LW", "ST", "RW"],
    "4-3-3[2]": ["GK", "LB", "CB", "CB", "RB", "CM", "CDM", "CM", "LW", "ST", "RW"],
    "4-3-3[3]": ["GK", "LB", "CB", "CB", "RB", "CDM", "CDM", "CM", "LW", "ST", "RW"],
    "4-3-3[4]": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "CAM", "LW", "ST", "RW"],
    "4-3-3[5]": ["GK", "LB", "CB", "CB", "RB", "CDM", "CM", "CM", "LW", "CF", "RW"],
    "4-4-1-1": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "LM", "CF", "RM", "ST"],
    "4-4-1-1[2]": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "LM", "CAM", "RM", "ST"],
    "4-4-2": ["GK", "LB", "CB", "CB", "RB", "LM", "CM", "CM", "RM", "ST", "ST"],
    "4-4-2[2]": ["GK", "LB", "CB", "CB", "RB", "LM", "CDM", "CDM", "RM", "ST", "ST"],
    "4-5-1": ["GK", "CB", "CB", "LB", "RB", "CM", "LM", "CAM", "CAM", "RM", "ST"],
    "4-5-1[2]": ["GK", "CB", "CB", "LB", "RB", "CM", "LM", "CM", "CM", "RM", "ST"],
    "5-2-1-2":["GK", "LWB", "CB", "CB", "CB", "RWB", "CM", "CM", "CAM", "ST", "ST"],
    "5-2-2-1": ["GK", "LWB", "CB", "CB", "CB", "RWB", "CM", "CM", "LW", "ST", "RW"],
    "5-3-2": ["GK", "LWB", "CB", "CB", "CB", "RWB", "CM", "CDM", "CM", "ST", "ST"],
    "5-4-1": ["GK", "LWB", "CB", "CB", "CB", "RWB", "CM", "CM", "LM", "RM", "ST"]
    }

status_dict = {
    0: "UNKNOWN: The status of the model is still unknown. A search limit has been reached before any of the statuses below could be determined.",
    1: "MODEL_INVALID: The given CpModelProto didn't pass the validation step.",
    2: "FEASIBLE: A feasible solution has been found. But the search was stopped before we could prove optimality.",
    3: "INFEASIBLE: The problem has been proven infeasible.",
    4: "OPTIMAL: An optimal feasible solution has been found."
}
