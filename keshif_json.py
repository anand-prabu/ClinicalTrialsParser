# sort through the osf returned json to just do the keshif we want

import requests
import json
import io

#osf_text = requests.get("http://localhost:8000/osf_api_output.json")
osf_text = open('osf_api_output.json').read()

osf_json = json.loads(osf_text)

recent_versions = []

osf_urls = []

for item in osf_json:
    recent_versions.append(sorted(item.keys())[-2])

for item in osf_json:
    osf_urls.append((item.get('osf_url')))

print osf_urls


json_for_keshif = []

# get only the recent versions in the json

for index, element in enumerate(recent_versions):
    json_for_keshif.append(osf_json[index][element])

real_json = []

for index, item in enumerate(json_for_keshif):
    json_element = {}
    json_element["nct_id"] = json_for_keshif[index]["nct_id"]
    json_element["status"] = json_for_keshif[index]["status"]["type"]
    json_element["initial_release_date"] = json_for_keshif[index]["initial_release_date"]
    json_element["description"] = json_for_keshif[index]["description"]
    json_element["condition"] = json_for_keshif[index]["condition"]
    json_element["phase"] = json_for_keshif[index]["phase"]
    json_element["title"] = json_for_keshif[index]["title"]["textblock"]
    json_element["osf_url"] = "localhost:5000" + osf_urls[index]

    real_json.append(json_element)


with io.open("generated_keshif_json.json", "w", encoding = "utf-8") as f:
    f.write(unicode(json.dumps(real_json, indent=4)))
