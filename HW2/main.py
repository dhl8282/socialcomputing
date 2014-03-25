import facebook

#import custom lib
import util
ACCESS_TOKEN = 'CAACEdEose0cBAHw9wRJvncwoQUv7R2r58SEcjU779JlN7yHQsMaBI5jZAldRUTeCcgrtEfFxIfbfugBAnwzXfVYhMu1qMiIYyJpwvlng2QOYOzHvQZC5epp6TkOQZBjVdy15gOeHZA04umQC6A574ZBoBccrG4WYAG3cjzKLoZBUw4Lg84UN0Y4lfb3jpZBCHMZD'

g = facebook.GraphAPI(ACCESS_TOKEN)

obj = g.get_object('me')
#print json.dumps(obj, indent=1)

friends = g.get_connections('me', 'friends')
#print json.dumps(friends, indent=1)

socialweb = g.request("search", {'q':'social web', 'type':'page'})
#dump(socialweb)

#Get tesla feeds
tsla = g.get_connections('teslamotors', 'feed')['data']
