"""
Chapter 17 Exercise 2
"""
from operator import itemgetter
import requests
import plotly.express as px

# Make an API call an check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submissions_ids = r.json()
submission_dicts = []
for submission_id in submissions_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    try:    
        # Build dictionary for each article
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants']
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        continue

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

# Get data for visualizattion
submission_comments = [submission['comments'] for submission in submission_dicts]
submission_links = [f"<a href='{submission['hn_link']}'>{submission['title']}</a>" 
                    for submission in submission_dicts]

# Make visualization
title = "Most Active Discussions on Hacker News"
labels = {'x': "Submission's Title", 
          'y': 'Number of Comments'}
fig = px.bar(x=submission_links,y=submission_comments,
             title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                      yaxis_title_font_size=20)
fig.show()
