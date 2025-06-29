import requests
import json

# الرابط الصحيح
url = "https://api.tryoto.com/rest/v2/refreshToken"

headers = {
    "Content-Type": "application/json"
}

data = {
    "refresh_token": "AMf-vBx2INEZP3xe6EBSX5V3iElQnvpChRVMKgr_JRM5fYwhTghCOEeuRNlIq2prPFeGMCUxm4-LjrQVwEOWqEOqnDw1NxnjiB2BKlslDBN5S_7tE5J7Jw2bTI13LdOXEAtHx_UBDAYaNNu_Wd4t-wqJquUM6lfC9mHa-oQgfY76s2zOhBo1UiuxYkczg47OO5KsSdo_I-mR"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
try:
    print("Response:", response.json())
except Exception:
    print("Response (raw):", response.text)
