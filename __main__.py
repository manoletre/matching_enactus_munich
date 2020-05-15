import sys
import json
from matching.games import HospitalResident
from reader import Reader

operation = sys.argv[1]

# insert path of excel below
r = Reader("./Prios der Challenges für das Projekthackathon(1-2).xlsx")

doctors = None
hospital_prefs = None

if (operation == "candidates"):
    doctors = r.read_doctors()

    r.write_candidates(doctors)


elif (operation == "candidateList"):
    hospital_prefs = r.read_hospital_prefs()
    toPrint = set()
    for h in hospital_prefs:
        for c in hospital_prefs[h]:
            toPrint.add(c)

    toPrint = sorted(toPrint)

    print()
    print("----------")
    for c in toPrint:
        print(c)
    print("----------")
    print()


elif (operation == "matching"):
    doctors = r.read_doctors()
    hospital_prefs = r.read_hospital_prefs()

    capacities = r.read_hospital_capacities()

    game = HospitalResident.create_from_dictionaries(
        doctors, hospital_prefs, capacities
    )
    result = game.solve()

    print(result)