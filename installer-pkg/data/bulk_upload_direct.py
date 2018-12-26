""" Script to import all AM data into a Curator Core architecture
"""
from os.path import join
from os import listdir
import requests
import json

# Script parameters
from rest_framework.status import HTTP_201_CREATED

user_name = "root"
user_pwd = "Temp@Win2000"

mdcs_url = "http://127.0.0.1:8000"
template_upload_url = "/rest/templates/add"
xml_upload_url = "/rest/curate"

xsd_filename = input("Please input .xsd filename: " ) #am_upload.xsd
xsd_schema = input('Please enter schema (can be found in "Record" page): ')
xsd_data_filepath = join(".", xsd_filename)
xml_data_dirpath = input("density_build")

print xsd_filename + '\n'
print xml_data_dirpath + '\n'
print xsd_data_filepath + '\n'


# Uploading all XML data
'''
for xml_filename in listdir(xml_data_dirpath):
    with open(join(xml_data_dirpath, xml_filename), "r") as xml_file:
        xml_content = xml_file.read()

        url = mdcs_url + xml_upload_url
        data = {
            "title": xml_filename,
            "schema": "5b8f6dc1ef370cda2fc1ca46",
            "content": xml_content
        }

        response_str = requests.post(url, data, auth=(user_name, user_pwd))
        response_code = response_str.status_code
        response = json.loads(response_str.text)

        if response_code == HTTP_201_CREATED:
            print response["title"] + " has been uploaded"
        else:
            print "Upload failed with status code " + str(response_code) + ": " + response["message"]
'''
