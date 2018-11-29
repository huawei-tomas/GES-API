import urllib3
import json
import certifi
from pprint import pprint
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action",
    help="which action to choose: start, stop, or test")

args = parser.parse_args()

http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())

with open("./token", "r") as f:
    token = f.read()

# Headers are how we pass through the token.
headers = {"Content-Type":"application/json"}
headers["X-Language"] = "en-us"
headers["X-Auth-Token"] = token

my_project_id = os.environ['GES_PROJECTID']
my_graph_id = os.environ['GES_GRAPHID']
my_region = os.environ['GES_REGION'].replace('iam','ges')

if args.action is None or args.action == "test":
    action = "execute-gremlin-query"
elif args.action == "start" or args.action == "stop":
    action = args.action
else:
    raise ValueError("input action should be either test, start, or stop")

base = "{}.myhuaweicloud.com".format(my_region)
url = "https://{}/v1.0/{}/graphs/{}/action?action_id={}".format(
    base, my_project_id, my_graph_id, action
    )

data = {"command":"g.V().limit(10)"}
r = http.request("POST", url, headers=headers, body=json.dumps(data))

# We don't want a JSON string. We want a python dictionary.
output = json.loads(r.data)
pprint(output)
