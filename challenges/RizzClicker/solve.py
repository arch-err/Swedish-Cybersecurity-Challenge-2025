from functools import wraps
import json
import jwt
import os

key_id = "../Dockerfile"

with open(f"./keys/{key_id}", "r") as f:
    key = f.read()
    print(key)

payload = {"role": "pro", "name": "apa", "rizz": 1000, "items": []}

new_token = jwt.encode(payload, key, algorithm="HS256", headers={"kid": key_id})

print(new_token)

with open(f"./keys/{key_id}", "r") as k:
    key = k.read()
print(jwt.decode(new_token, key, algorithms=["HS256"]), key_id)