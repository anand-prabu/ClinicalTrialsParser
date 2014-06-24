from lxml import etree
import json
import xmltodict
import glob

def xml_to_json(xml_file):

    tree = etree.parse(xml_file)
    xml_string = etree.tostring(tree)

    json_text = xmltodict.parse(xml_string)

    json_text = json.dumps(json_text, sort_keys=True, indent=4)

    return json_text

def bulk_xml_to_json():

    key_xml_folder = 'ct_xml/'
    key_json_folder = 'ct_raw_json/'

    xmlfiles = glob.glob(key_xml_folder + '*.xml')
    
    xml_ids = []

    for filename in xmlfiles:
        filename = filename.replace('.xml','')
        filename = filename.replace('ct_xml/','')
        xml_ids.append(filename)

    for i, filename in enumerate(xmlfiles):
        json_text = xml_to_json(filename)

        with open(key_json_folder + xml_ids[i] +'_raw.json', "wb") as jt:
            jt.write(json_text)

# xml_to_json('NCT02152930.xml')

bulk_xml_to_json()
