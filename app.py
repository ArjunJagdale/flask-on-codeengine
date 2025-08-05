from flask import Flask, request
import requests

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html>
<head>
  <title>GitHub Activity Viewer</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f2f2f2;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
    }
    .container {
      background: white;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      text-align: center;
      max-width: 500px;
      width: 90%;
    }
    input[type="text"] {
      padding: 10px;
      font-size: 16px;
      width: 70%;
      margin-bottom: 15px;
    }
    input[type="submit"] {
      padding: 10px 20px;
      font-size: 16px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
    ul {
      text-align: left;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>GitHub Activity Viewer</h2>
    <form method="get" action="/github">
      <input type="text" name="username" placeholder="e.g. ArjunJagdale" required><br>
      <input type="submit" value="View Activity">
    </form>
    {activity}
  </div>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_FORM.format(activity="")

@app.route('/github')
def github_activity():
    username = request.args.get('username')
    if not username:
        return HTML_FORM.format(activity="<p style='color:red;'>Please provide a username.</p>")

    url = f"https://api.github.com/users/{username}/events/public"
    headers = {'Accept': 'application/vnd.github+json'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return HTML_FORM.format(activity=f"<p style='color:red;'>❌ Error: Could not fetch activity for <b>{username}</b></p>")

    events = response.json()[:5]
    activity_list = [
        f"<li>{event.get('type', 'Unknown')} in <b>{event.get('repo', {}).get('name', 'Unknown')}</b></li>"
        for event in events
    ]
    html_output = f"<h3>Recent activity for <em>{username}</em>:</h3><ul>{''.join(activity_list)}</ul>"

    return HTML_FORM.format(activity=html_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
