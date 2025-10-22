import requests
import time

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers ={"Accept": "application/vnd.github.v3+json"}

try:
    r = requests.get(url,headers=headers)
    print(f"Status code: {r.status_code}")

    # Convert the response object to a dictionary.
    response_dict = r.json()

    if r.status_code != 200:
        print(f"Error: {response_dict.get('message','Unknown error')}")
        if 'rate limit' in response_dict.get('message', '').lower():
            print("Rate limit exceeded. Wait 1 minute and try again")
    else:
        # Process results.
        print(f"Total repositories: {response_dict['total_count']}")
        print(f"Complete results: {not response_dict['incomplete_results']}")

        # Explore information about the repositories.
        repo_dicts = response_dict['items']
        print(f"Repositories returned: {len(repo_dicts)}")

        # Examine the top repositories
        print(f"\nSelected information about each repository:")
        for repo_dict in repo_dicts:
            print("\nSelected information about first repository:")
            print(f"Name: {repo_dict['name']}")
            print(f"Owner: {repo_dict['owner']['login']}")
            print(f"Stars: {repo_dict['stargazers_count']}")
            print(f"Repository: {repo_dict['html_url']}")
            print(f"Created: {repo_dict['created_at']}")
            print(f"Updated: {repo_dict['updated_at']}")
            print(f"Description: {repo_dict['description']}")

except Exception as e:
    print(f"Error inesperado: {e}")

# Delay to avoid saturating the API
time.sleep(2)
