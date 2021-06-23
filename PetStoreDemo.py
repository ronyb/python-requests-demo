import json
import time

import requests

# This example works against the REST API defined at: https://petstore.swagger.io/#/


def print_response(response_obj):
    print("Response headers:")
    print(response.status_code)
    print("Response headers:")
    print(response.headers)
    print("Response body:")
    print(response.text)


dog_id = 235
dog_name = "Bingo"

# POST Example


print("------------- GET pet by ID -------------")
response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{dog_id}')
print_response(response)

time.sleep(1)

print("------------- POST - add a pet -------------")

pet_data = {
  "id": dog_id,
  "category": {
    "name": "dogs"
  },
  "name": dog_name,
  "status": "available"
}

response = requests.post(url="https://petstore.swagger.io/v2/pet", data=json.dumps(pet_data), headers={'Content-Type': 'application/json'})
print_response(response)

time.sleep(1)

print("------------- GET pet by ID -------------")
response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{dog_id}')
print_response(response)

dog_obj = response.json()
dog_name_in_response = dog_obj["name"]

assert dog_name_in_response == dog_name, f"Expected dog name: {dog_name}"
