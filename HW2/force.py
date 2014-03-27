#!usr/bin/env python
import json
import networkx as nx
from networkx.readwrite import json_graph
import requests

#import from local
import facebook_setup as fs

def getMutualFriends(f_api):
    friends = [(friend['id'], friend['name'],)
                for friend in f_api.get_connections('me', 'friends')['data']]
    url = 'https://graph.facebook.com/me/mutualfriends/%s?access_token=%s'
    mutual_friends = {}
    for friend_id, friend_name in friends:
        print friend_name
        r = requests.get(url % (friend_id, fs.ACCESS_TOKEN,))
        response_data = json.loads(r.content)['data']
        mutual_friends[friend_name] = [data['name']
                for data in response_data]
    return mutual_friends

def getForceGraph(mutual_friends):
    nxg = nx.Graph()
    for mf in mutual_friends:
        nxg.add_edge('me', mf)
    for f1 in mutual_friends:
        for f2 in mutual_friends[f1]:
            nxg.add_edge(f1, f2)
    return nxg

def getCliquesToJson(nxg):
    nld = json_graph.node_link_data(nxg)
    json.dump(nld, open('force.json', 'w'))

def getCliqueInfo(nxg):
    cliques = [c for c in nx.find_cliques(nxg)] 
    num_cliques = len(cliques) 
    clique_sizes = [len(c) for c in cliques] 
    max_clique_size = max(clique_sizes) 
    avg_clique_size = sum(clique_sizes) / num_cliques 
    max_cliques = [c for c in cliques if len(c) == max_clique_size] 
    num_max_cliques = len(max_cliques)
