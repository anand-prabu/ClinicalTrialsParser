import json
import os

def get_status_phase(jsonFile):
	"""Gets the status and phase of a single trial"""
	json_file = open(jsonFile).read()
	json_data = json.loads(json_file)
	return json_data['clinical_study']['overall_status'],json_data['clinical_study']['phase']


def bulk_get_status_phase(json_list):
	"""Prints out count of how many trials in each status / phase"""
	status_list= {}
	phase_list = {}
	for trial in json_list:
		status, phase = get_status_phase(trial)
		if status in status_list:
			status_list[status]+=1;
		else:
			status_list[status]=1;
		if phase in phase_list:
			phase_list[phase]+=1
		else:
			phase_list[phase]=1
	return status_list, phase_list

json_list = []
path = "ct_raw_json/"
for fname in os.listdir(path):
	json_list.append(path+fname)

print bulk_get_status_phase(json_list)[0]
print bulk_get_status_phase(json_list)[1]