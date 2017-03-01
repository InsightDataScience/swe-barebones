import requests 
import itertools 
''' 
A set of tools to analyze Github repositories.
'''

def get_user_json(username):
    return requests.get('https://api.github.com/users/%s/repos' % (username)).json()

def get_contributor_json(username, repository):
    return requests.get('https://api.github.com/repos/%s/%s/contributors' % (username, repository)).json()

def get_repository_list(username):
    r = get_user_json(username)
    user_repos = [entry['name'] for entry in r]
    return user_repos

def get_contributor_list(username, repository):
    r = get_contributor_json(username, repository)
    contributors = [entry['login'] for entry in r]    
    return contributors

def get_total_contributors(username):
    all_contrib = [get_contributor_list(username, repo) for repo in get_repository_list(username)]
    all_contrib = list(itertools.chain.from_iterable(all_contrib))  
    unique_contrib = set(all_contrib)
    return len(unique_contrib)
