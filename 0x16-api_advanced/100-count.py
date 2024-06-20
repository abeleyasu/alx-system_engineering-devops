#!/usr/bin/python3
"""
100-count module
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited by spaces).
    """
    if counts is None:
        counts = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            
            for post in children:
                title = post['data']['title'].lower()
                words = title.split()
                
                for word in words:
                    normalized_word = word.strip('.,!?_:')
                    if normalized_word in counts:
                        counts[normalized_word] += 1
                    elif normalized_word.lower() in word_list:
                        counts[normalized_word] = 1
            
            after = data['data'].get('after', None)
            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                print_results(counts, word_list)
        else:
            print_results(counts, word_list)
    except requests.RequestException:
        print_results(counts, word_list)

def print_results(counts, word_list):
    """
    Helper function to print the sorted counts of keywords.
    """
    results = []
    for word in word_list:
        count = counts.get(word.lower(), 0)
        if count > 0:
            results.append((word.lower(), count))
    
    results.sort(key=lambda x: (-x[1], x[0]))
    
    for result in results:
        print(f"{result[0]}: {result[1]}")
