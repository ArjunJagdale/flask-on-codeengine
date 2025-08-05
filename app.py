from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>👋 Welcome to GitHub Activity Viewer</h2>
    <p>Use the following URL format to view recent activity:</p>
    <pre>/activity/&lt;github_username&gt;</pre>
    <p>Example: <a href="/activity/ArjunJagdale">/activity/ArjunJagdale</a></p>
    """

@app.route('/activity/<username>')
def get_github_activity(username):
    url = f'https://api.github.com/users/{username}/events/public'
    headers = {'Accept': 'application/vnd.github+json'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"<h3>❌ Error: Could not fetch activity for {username}</h3>"

    events = response.json()
    activity_list = []
    for event in events[:5]:
        event_type = event.get('type', 'Unknown Event')
        repo_name = event.get('repo', {}).get('name', 'Unknown Repo')
        activity_list.append(f"{event_type} on <b>{repo_name}</b>")

    html_output = f"<h2>Recent activity for <em>{username}</em>:</h2><ul>"
    for item in activity_list:
        html_output += f"<li>{item}</li>"
    html_output += "</ul>"

    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
