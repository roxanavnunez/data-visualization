"""
Chapter 17 Exercise 3
"""

import requests

def test_status_code_200():
    """Test that the status code is 200"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    assert r.status_code == 200

def test_number_of_items_returned():
    """Test that the number of items returned is 30 (default for GitHub API)"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    assert len(repo_dicts) == 30

def test_total_repositories_greater_than_millions():
    """Test that the total number of Python repositories is greater than 1 million"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    total_count = response_dict['total_count']
    assert total_count > 1_000_000

def test_repositories_have_required_keys():
    """Test that each repository has the required keys"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    
    required_keys = ['name', 'owner', 'stargazers_count', 'html_url', 'description']
    
    for repo in repo_dicts:
        for key in required_keys:
            assert key in repo

def test_owner_structure():
    """Test that owner information has the expected structure"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    
    for repo in repo_dicts:
        assert 'login' in repo['owner']
        assert 'html_url' in repo['owner']

def test_star_count_positive():
    """Test that star counts are positive numbers"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    
    for repo in repo_dicts:
        assert repo['stargazers_count'] >= 0

def test_repository_names_not_empty():
    """Test that repository names are not empty"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    
    for repo in repo_dicts:
        assert repo['name'] != ''
        assert len(repo['name']) > 0