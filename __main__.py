import sys
import json
from matching.games import HospitalResident
from reader import Reader

operation = sys.argv[1]

# insert path of excel below
r = Reader("./Bewerber - Projekt Matching(1-13).xlsx")

doctors = None
hospital_prefs = None

if (operation == "candidates"):
    doctors = r.read_doctors()

    r.write_candidates(doctors)

elif (operation == "matching"):
    doctors = r.read_doctors()
    hospital_prefs = r.read_hospital_prefs()

    capacities = r.read_hospital_capacities()

    game = HospitalResident.create_from_dictionaries(
        doctors, hospital_prefs, capacities
    )
    result = game.solve()

    print(result)