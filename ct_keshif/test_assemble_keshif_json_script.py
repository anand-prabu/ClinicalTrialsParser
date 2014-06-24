import json
conjoin = open("studies_for_keshif.json", 'r').read()
data=json.loads(conjoin)
print data["clinical_studies_list"][0]