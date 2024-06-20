#!/usr/bin/python3
"""
2-recurse module
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If the subreddit is invalid or no
    results are found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            for post in children:
                hot_list.append(post['data']['title'])
            
            after = data['data'].get('after', None)
            if after:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
