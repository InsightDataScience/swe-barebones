from github import repos
import pytest
from voluptuous import REMOVE_EXTRA, Schema, Url
from datetime import datetime

"""
This script tests methods in a Github repository class
"""

def test_repo_schema():
    js = repos.get_user_json('bmregner')
    def date_format(fmt='%Y-%m-%dT%XZ'):
        return lambda v: datetime.strptime(v, fmt)
    user_schema = Schema([{'full_name': str,
                        'updated_at': date_format(),
                        'url': Url(),
                        'size': int,
                        'private': bool}],
                         extra=REMOVE_EXTRA)
    assert user_schema(js)

def test_contrib_schema():
    js = repos.get_contributor_json('bmregner','finance_prediction')
    contrib_schema = Schema([{'login': str,
                        'html_url': Url(),
                        'contributions': int}],
                         extra=REMOVE_EXTRA) 
    assert contrib_schema(js)

# Uses monkeypatch to return results without sending a request to github
def test_total_contrib(monkeypatch):
    def repo_list(username):
        return ['me.github.io', 'myproject', 'mydemo']
    def contrib_list(username,repo):
        if repo == 'me.github.io':
            return ['me']
        elif repo == 'myproject':
            return ['John', 'Bob', 'Gary', 'me']
        elif repo == 'mydemo': 
            return ['me']
    monkeypatch.setattr(repos,'get_contributor_list',contrib_list)
    monkeypatch.setattr(repos,'get_repository_list',repo_list)
    unique_contrib = repos.get_total_contributors('me')
    assert unique_contrib == 4
