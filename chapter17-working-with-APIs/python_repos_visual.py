import requests
import time
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers ={"Accept": "application/vnd.github.v3+json"}

try:
    r = requests.get(url,headers=headers)
    print(f"Status code: {r.status_code}")

    # Process overall results.
    response_dict = r.json()

    if r.status_code != 200:
        print(f"Error: {response_dict.get('message','Unknown error')}")
        if 'rate limit' in response_dict.get('message', '').lower():
            print("Rate limit exceeded. Wait 1 minute and try again")
    else:
        print(f"Complete results: {not response_dict['incomplete_results']}")

        # Process repository information.
        repo_dicts = response_dict['items']
        repo_names, stars = [], []
        for repo_dict in repo_dicts:
            repo_names.append(repo_dict['name'])
            stars.append(repo_dict['stargazers_count'])
    
    # Make visualization
    title = "Most-Starred Python Projects on GitHub"
    labels = {'x': 'Repository', 'y': 'Stars'}
    fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

    fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                      yaxis_title_font_size=20)
    fig.show()

except Exception as e:
    print(f"Unexpected Error: {e}")

# Delay to avoid saturating the API
time.sleep(2)
