import pandas as pd
import xlsxwriter as xw
from math import isnan

class Reader(object):
    def __init__(self, path):
        self.path = path


    def read_doctors(self):
        doctors = pd.read_excel(self.path, "Sheet1")
        doctors.drop(doctors.columns[[0,1,2,3,4]], axis=1, inplace=True)

        # trim columns
        doctors = doctors.apply(lambda x: x.str.strip())

        doctors["Name"] = doctors["Name"] + " " + doctors["Nachname"]
        doctors = doctors.drop(columns=["Nachname"])
        
        doctors_dict = doctors.set_index("Name").T.to_dict("list")
            
        return self.clean(doctors_dict)


    def write_candidates(self, doctors_dict):
        hospitals = pd.read_excel("hospitals.xlsx", "Sheet1").to_dict("list")["Name"]

        candidates = {c : [] for c in hospitals}

        for h in doctors_dict:
            for c in doctors_dict[h]:
                candidates[c].append(h)

        self.write_dict_to_excel("candidates", candidates)
        

    def read_hospital_capacities(self):
        hospital_dict = pd.read_excel("hospitals.xlsx", "Sheet1").to_dict("list")
        names = hospital_dict["Name"]
        capacities = hospital_dict["Capacities"]

        capacity_dict = {}
        for i in range(0, len(names)):
            capacity_dict[names[i]] = capacities[i]

        return capacity_dict


    def read_hospital_prefs(self):
        hospital_prefs = pd.read_excel("candidates.xlsx")

        hospital_prefs = hospital_prefs.apply(lambda x: x.str.strip())

        return self.clean(hospital_prefs.to_dict("list"))


    def clean(self, dict_with_nan):
        clean = {}
        for c in dict_with_nan:
            clean[c] = [h for h in dict_with_nan[c] if type(h) is str or not isnan(h)]
            
        return clean

    
    def write_dict_to_excel(self, workbook_name, dict_to_write):
        wb = xw.Workbook("./" + workbook_name + ".xlsx")
        ws = wb.add_worksheet()

        #write headers
        col = 0
        for c in dict_to_write:
            ws.write_string(0, col, c)
            col += 1

        #write candidate per hospital
        col = 0
        for c in dict_to_write:
            row = 1
            for h in dict_to_write[c]:
                ws.write_string(row, col, h)
                row += 1
            col += 1

        wb.close()