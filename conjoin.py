import json
import os

json_list = []
path = "ct_raw_json/"
for filename in os.listdir(path):
	json_list.append(path+filename)

clinical_trials_json=[]

for filename in json_list:
	json_file = open(filename).read()
	json_data = json.loads(json_file)
	clinical_trials_json.append(json_data)


clinical_output ={}
clinical_output["clinical_studies_list"]=clinical_trials_json



with open('studies_for_keshif.json', 'w') as json_txt:
	json.dump(clinical_output, json_txt, indent=4, sort_keys=True)