""" main document, handles IO and runs the actual matching algorithm 
to read candidates use argument "candidates"
to create the list of candidates use argument "candidateList"
to let the matching happen use argument "matching"
"""

import sys
import pandas as pd
from matching.games import HospitalResident
from reader import Reader

operation = sys.argv[1]

# insert path of doctors excel below
r = Reader("Projektprioritäten für Interviewzuteilung am Samstag.xlsx")

DOCTORS = None
HOSPITAL_PREFS = None

if operation == "candidates":
	""" reads doctors excel and writes new excel with candidates per hospital """

	r.read_doctors()


elif operation == "matching":
	DOCTORS = r.read_doctors()
	HOSPITAL_PREFS = r.read_hospital_prefs()

	capacities = r.read_hospital_capacities()

	game = HospitalResident.create_from_dictionaries(
		DOCTORS, HOSPITAL_PREFS, capacities
	)
	result = game.solve()

	turned = r.turn_dict(result)
	df_result = pd.DataFrame(turned, index=[0]).T
	df_result.to_excel("matching_result.xlsx")
