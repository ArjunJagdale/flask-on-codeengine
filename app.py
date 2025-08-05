from flask import Flask, request
import requests

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<title>GitHub Activity Viewer</title>
<h2>Enter GitHub Username</h2>
<form method="get" action="/github">
  <input name="username" placeholder="e.g. ArjunJagdale">
  <input type="submit" value="View Activity">
</form>
"""

@app.route('/')
def home():
    return HTML_FORM

@app.route('/github')
def github_activity():
    username = request.args.get('username')
    if not username:
        return "Please provide a username."

    url = f"https://api.github.com/users/{username}/events/public"
    headers = {'Accept': 'application/vnd.github+json'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"<h3>❌ Error: Could not fetch activity for {username}</h3>"

    events = response.json()[:5]
    activity_list = [
        f"{event.get('type', 'Unknown')} in <b>{event.get('repo', {}).get('name', 'Unknown')}</b>"
        for event in events
    ]

    html_output = f"<h2>Recent activity for <em>{username}</em>:</h2><ul>"
    for item in activity_list:
        html_output += f"<li>{item}</li>"
    html_output += "</ul>"

    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
