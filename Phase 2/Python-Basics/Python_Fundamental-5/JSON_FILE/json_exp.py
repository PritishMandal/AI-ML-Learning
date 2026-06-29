import json

py_obj = {
    "name": "Pritish Mandal",
    "username": "pritish_07",
}

# Python dictionary ko JSON string me convert kar rahe hain
json_str = json.dumps(py_obj)

print(type(json_str), json_str) 