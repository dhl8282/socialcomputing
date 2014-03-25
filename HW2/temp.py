import facebook
import json
import requests

base_url = 'https://graph.facebook.com/me'
ACCESS_TOKEN = 'CAACEdEose0cBAK0GUKT2ANhH7pE2hCKIPXkctWcsz4vGwBnzIYEPQrQ8LnbkF2gDhtMEzT7VXCXmt3T5PBTXmtcWYImHuO5NuOAO4ztHqEGmUYtqMv9IfG9ZCPwvfXc7GpjfPHn6MdpljH6DWmlH0KqCEqQ6QBYmK3643ZCrT2ZBqTpRDWa8uZCR9ibysU4ZD'

fields = 'id,name'


url = '%s?fields=%s&access_token=%s' % (base_url, fields, ACCESS_TOKEN,)

content = requests.get(url).json()

#print json.dumps(content, indent=1)

def dump(content):
    print json.dumps(content, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

obj = g.get_object('me')
#print json.dumps(obj, indent=1)

friends = g.get_connections('me', 'friends')
#print json.dumps(friends, indent=1)

socialweb = g.request("search", {'q':'social web', 'type':'page'})
#dump(socialweb)

#Get tesla feeds
tsla = g.get_connections('teslamotors', 'feed')
