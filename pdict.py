"""
When you wnat to store data in a key value pairs, we use dictionary.
dict = {
  "key":"value",
  "key2":"value2"
}
Latest version of python dictionary is ordered where as older versions it was unordered.
Keys cannot be duplicated.
"""

contact = {
  "name": "ashish",
  "email": "ashish.panicker",
  "phone": ["412345688", "589997422"],
  "address": {
    "city": "Mumbai",
    "state": "MH"
  }
}

print(contact)
# print(contact.keys())
# print(contact.values())
contact.update({"name": "Ashish S"})
print(contact)
print(contact["name"])
print(contact["address"])

for key in contact:
  print(f"Key = {key} Value = {contact[key]}")