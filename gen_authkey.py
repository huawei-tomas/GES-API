import urllib3
import codecs
import certifi
import os


http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())

headers = {"Content-Type": "text/plain;charset=UTF-8",}


region = os.environ['GES_REGION']
user_name = os.environ['GES_USER']
password = os.environ['GES_PSSWD']
domain = os.environ['GES_DOMAIN']
projectid = os.environ['GES_PROJECTID']


data = '{ \
        "auth": { \
          "identity": { \
            "methods": [ \
              "password" \
            ], \
            "password": { \
              "user": { \
                "name": "'+user_name+'", \
                "password": "'+password+'", \
                "domain": { \
                  "name": "'+domain+'" \
                } \
              } \
            } \
          }, \
          "scope": { \
            "project": { \
              "id": "'+projectid+'" \
          } \
        } \
      } \
    }'

r = http.request(
    "POST",
    "https://{}.myhuaweicloud.com/v3/auth/tokens".format(region),
    headers=headers,
    body=data
    )

# Make sure the request was received. should be 201.
print(r.status)

# Get the token that was created out of the headers.
token = r.headers.get("X-Subject-Token")

# Save us a copy.
with codecs.open("token","w", "utf-8") as f:
    f.write(token)
