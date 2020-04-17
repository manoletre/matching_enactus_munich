import pandas as pd
import xlsxwriter as xw
from math import isnan

class Reader(object):
    def __init__(self, path):
        self.path = path


    def read_hackers(self):
        hackers = pd.read_excel(self.path, "Hackers")

        # trim columns
        hackers = hackers.apply(lambda x: x.str.strip())

        hackers["Name"] = hackers["Name"] + "_" + hackers["Nachname"]
        hackers = hackers.drop(columns=["Nachname"])
        
        hackersDict = hackers.set_index("Name").T.to_dict("list")
        return hackersDict


    def write_candidates(self, hackersDict):
        challenges = pd.read_excel(self.path, "Challenges").to_dict("list")["Name"]

        print(challenges)

        candidates = {c : [] for c in challenges}

        for h in hackersDict:
            for c in hackersDict[h]:
                candidates[c].append(h)

        #writing to candidates
        wb = xw.Workbook("./candidates.xlsx")
        ws = wb.add_worksheet("Candidates")

        #write headers
        col = 0
        for c in challenges:
            ws.write_string(0, col, c)
            col += 1

        #write candidate per challenge
        col = 0
        for c in candidates:
            row = 1
            for h in candidates[c]:
                ws.write_string(row, col, h)
                row += 1
            col += 1

        wb.close()


    def read_challenge_prefs(self):
        challenge_prefs = pd.read_excel("candidates.xlsx").to_dict("list")

        clean = {}
        for c in challenge_prefs:
            clean[c] = [h for h in challenge_prefs[c] if type(h) is str or not isnan(h)]

        return clean