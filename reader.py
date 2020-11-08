""" This document defines the functionality to read data from the excel files """

from math import isnan

import pandas as pd
import xlsxwriter as xw

class Reader():
	"""The Reader class receives the path of the excel to be read and
	defines contains the functionality to read and process data from excel
	"""

	def __init__(self, path):
		self.path = path


	def clean(self, dict_with_nan):
		""" cleans dictionary for it to not contain NaN values """

		clean = {}
		for key in dict_with_nan:
			clean[key] = [h for h in dict_with_nan[key] if type(h) is str or not isnan(h)]

		return clean


	def read_doctors(self):
		"""doctors are read from the provided path. This function
		takes care of some of the formating.
		"""

		doctors = pd.read_excel(self.path, "Sheet1")
		doctors.drop(doctors.columns[[0,1,2,3]], axis=1, inplace=True)

		doctors = doctors.apply(lambda x: x.str.strip())

		doctors["Vorname"] = doctors["Vorname"] + " " + doctors["Nachname"]
		doctors.drop(columns=["Nachname"], axis=1, inplace=True)

		hospitals = pd.read_excel("hospitals.xlsx")["Name"].apply(lambda x: x.strip())
		hospital_dfs = []
		for hospital in hospitals:
			hospital = hospital.strip()
			hospital_overview = []
			for index, row in doctors.iterrows():
				for i, prio in enumerate(list(row[1:])):
					if prio == hospital:
						current = {}
						current["Vorname"] = row["Vorname"]
						current["Prio"] = "Prio {}".format(i+1)
						hospital_overview.append(current)
			hospital_dfs.append(pd.DataFrame(hospital_overview))

		writer = pd.ExcelWriter("candidates.xlsx", engine="xlsxwriter")
		for i, hospital_df in enumerate(hospital_dfs):
			hospital_df.to_excel(writer, sheet_name=hospitals[i])
		writer.save()

		doctors_dict = doctors.set_index("Vorname").T.to_dict("list")
		return self.clean(doctors_dict)


	def read_hospital_capacities(self):
		hospital_dict = pd.read_excel("hospitals.xlsx")
		names = hospital_dict["Vorname"].apply(lambda x: x.strip())
		capacities = hospital_dict["Capacities"]

		capacity_dict = {}
		for i in range(0, len(names)):
			capacity_dict[names[i]] = capacities[i]

		return capacity_dict


	def read_hospital_prefs(self):
		hospitals = pd.read_excel("hospitals.xlsx")["Vorname"].apply(lambda x: x.strip())
		dict_hospital_prefs = {}
		for hospital in hospitals:
			hospital_prefs = pd.read_excel("candidates.xlsx", sheet_name=hospital)["Name"]
			hospital_prefs = hospital_prefs.apply(lambda x: x.strip())
			dict_hospital_prefs[hospital] = list(hospital_prefs)

		return self.clean(dict_hospital_prefs)

	def turn_dict(self, d):
		new_d = {}
		for key in d:	
			for v in d[key]:
				new_d[v] = key
		return new_d