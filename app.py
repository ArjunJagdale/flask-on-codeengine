from flask import Flask, request, render_template_string
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
    resp = requests.get(url)
    if resp.status_code != 200:
        return f"GitHub API error: {resp.status_code}", 400

    data = resp.json()[:5]
    events = [f"{event['type']} in <b>{event['repo']['name']}</b>" for event in data]
    return "<h3>Recent Activity for " + username + "</h3><ul>" + "".join(f"<li>{e}</li>" for e in events) + "</ul>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
