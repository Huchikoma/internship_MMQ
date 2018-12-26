""" Script to import all AM data into a Curator Core architecture
"""
from os.path import join
from os import listdir
import requests
import json

# Script parameters
from rest_framework.status import HTTP_201_CREATED

user_name = "root"
user_pwd = "root"

mdcs_url = "http://127.0.0.1:8000"
template_upload_url = "/rest/templates/add"
xml_upload_url = "/rest/curate"

xsd_filename = "am_upload.xsd"
xsd_data_filepath = join(".", xsd_filename)
xml_data_dirpath = "xml-density"

# Uploading AM curation schema
with open(join(xsd_data_filepath), "r") as template_file:
    template_content = template_file.read()

    url = mdcs_url + template_upload_url
    data = {
        "title": "am_schema_upload",
        "filename": xsd_filename,
        "content": template_content
    }

    response = requests.post(url, data, auth=(user_name, user_pwd))
    response_code = response.status_code
    response_content = json.loads(response.text)

    template_id = str(response_content['_id']['$oid'])

    if response_code == HTTP_201_CREATED:
        print "AM schema has been uploaded"
    else:
        raise Exception("A problem occured when uploading the schema (Error " + response_code + ")")


# Uploading all XML data
for xml_filename in listdir(xml_data_dirpath):
    with open(join(xml_data_dirpath, xml_filename), "r") as xml_file:
        xml_content = xml_file.read()

        url = mdcs_url + xml_upload_url
        data = {
            "title": xml_filename,
            "schema": template_id,
            "content": xml_content
        }

        response_str = requests.post(url, data, auth=(user_name, user_pwd))
        response_code = response_str.status_code
        response = json.loads(response_str.text)

        if response_code == HTTP_201_CREATED:
            print response["title"] + " has been uploaded"
        else:
            print "Upload failed with status code " + str(response_code) + ": " + response["message"]

