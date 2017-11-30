import requests
import json
import re

file_id = "b658d635-258a-4f6f-8377-767a43771fe4"

data_endpt = 'https://api.gdc.cancer.gov/data/%s' % file_id

response = requests.get(data_endpt, headers={"Content-Type": "application/json"})

response_head = response.headers["Content-Disposition"]

file_name = re.findall("filename=(.+)", response_head)[0]

with open(file_name,'wb') as output_file:
    output_file.write(response.content)
