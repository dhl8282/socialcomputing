#!usr/bin/env/ python
from collections import Counter

def getFriendNameAndLikes(f_api):
    f_like = f_api.get_object('me', fields='friends.fields(name,likes)')
    likes = {}
    for friend in f_like['friends']['data']:
        f_name = friend['name']
        if friend.has_key('likes'):
            likes[f_name] = friend['likes']['data']
    return likes

def getLikeCount(likes):
    return Counter([like['name']
                for friend in likes
                for like in likes[friend]
                if like.get('name')])
