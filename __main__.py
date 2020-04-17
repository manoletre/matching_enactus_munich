import sys
from matching.games import HospitalResident
from reader import Reader

operation = sys.argv[1]

r = Reader("./matching.xlsx")

hackers = None
challenge_prefs = None

if (operation == "candidates"):
    hackers = r.read_hackers()

    r.write_candidates(hackers)

elif (operation == "matching"):
    hackers = r.read_hackers()
    challenge_prefs = r.read_challenge_prefs()

    capacities = {chal: 3 for chal in challenge_prefs}

    game = HospitalResident.create_from_dictionaries(
        hackers, challenge_prefs, capacities
    )
    result = game.solve()

    print(result)