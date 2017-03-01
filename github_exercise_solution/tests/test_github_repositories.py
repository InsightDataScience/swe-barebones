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
